import random
import string
from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.secret_key = os.getenv('REPLACE::SECRET::KEY', 'REPLACE::DEFAULT::SECRET::KEY')

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost') ##REPLACE::ON::NEED::HOST
app.config['MYSQL_PORT'] = os.getenv('MYSQL_PORT', 3306)  #REPLACE::ON::NEED::PORT
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root') ##REPLACE::ON::NEED::USER
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'default') ##REPLACE::ON::NEED::PASSWORD
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'default')
app.config['SESSION_TYPE'] = os.getenv('SESSION_TYPE', 'filesystem')
app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(), 'sessions')

mysql = MySQL(app)

def generate_default_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

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

with app.app_context():
    cur = mysql.connection.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(200) NOT NULL
        )
    """)
    cur.close()
create_test_users()

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
    session.pop('user_id', None)
    return jsonify(message="200: Logging out was successful!"), 200

@app.route('/check-login')
def check_login():
    user_id = session.get('user_id')
    
    if user_id:
        return jsonify(logged_in=True), 200
    else:
        return jsonify(logged_in=False), 401

@app.route('/')
def hello():
    return 'It works.'

if __name__ == '__main__':
    app.run(debug=True)
