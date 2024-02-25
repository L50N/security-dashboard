import random
import string
from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL
import os
import yaml

app = Flask(__name__)

def generate_secret_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def save_secret_key_to_file(secret_key):
    with open('./backend/secret_key.yml', 'w') as file:
        yaml.dump({'SECRET_KEY': secret_key}, file)

if os.path.exists('./backend/secret_key.yml'):
    with open('./backend/secret_key.yml', 'r') as file:
        secret_data = yaml.safe_load(file)
        app.secret_key = secret_data.get('SECRET_KEY', generate_secret_key())
else:
    app.secret_key = generate_secret_key()
    save_secret_key_to_file(app.secret_key)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_PORT'] = os.getenv('MYSQL_PORT', 3306)
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'default')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'default')
app.config['SESSION_TYPE'] = os.getenv('SESSION_TYPE', 'filesystem')
app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(), 'sessions')

mysql = MySQL(app)

def create_test_users():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        count = cur.fetchone()[0]
        if count == 0:
            default_password = generate_default_password()
            cur.executemany("INSERT INTO users (email, password) VALUES (%s, %s)", [("first@example.com", default_password), ("second@example.com", default_password)])
            mysql.connection.commit()
        cur.close()

def generate_default_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def is_logged_in():
    return 'user_id' in session

@app.route('/')
def hello():
    return 'Welcome to your Flask application!'

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    with mysql.connection.cursor() as cur:
        cur.execute("SELECT id, email, password FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        if user:
            stored_password = user[2]
            
            if stored_password == password:
                session['user_id'] = user[0]
                app.logger.info(f"User logged in. User ID: {user[0]}")
                return jsonify(message="200: The login was successful!"), 200
            else:
                return jsonify(message="401: The user exists, but the password entered is incorrect!"), 401
        else:
            app.logger.info("The user is not known to us.")
            return jsonify(message="401: The user is not known to us."), 401

@app.route('/logout')
def logout():
    if is_logged_in():
        session.pop('user_id')
        return jsonify(message="200: Logging out was successful!"), 200
    else:
        return jsonify(message="401: You are not logged in."), 401

@app.route('/check-login')
def check_login():
    if is_logged_in():
        return jsonify(logged_in=True), 200
    else:
        return jsonify(logged_in=False), 401

if __name__ == '__main__':
    create_test_users()
    app.run(debug=True)
