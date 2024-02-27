import random
import string
from datetime import timedelta
import os
import yaml
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_mysqldb import MySQL

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

limiter = Limiter(key_func=get_remote_address)
limiter.init_app(app)


def generate_secret_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))


def save_secret_key_to_file(secret_key):
    with open('./backend/secret_key.yml', 'w') as file:
        yaml.dump({'SECRET_KEY': secret_key}, file)


if os.path.exists('./secret_key.yml'):
    with open('./secret_key.yml', 'r') as file:
        secret_data = yaml.safe_load(file)
        app.secret_key = secret_data.get('SECRET_KEY', generate_secret_key())
else:
    app.secret_key = generate_secret_key()
    save_secret_key_to_file(app.secret_key)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_PORT'] = os.getenv('MYSQL_PORT', 3307)
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'default')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'default')
app.config['SESSION_TYPE'] = os.getenv('SESSION_TYPE', 'filesystem')
app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(), 'sessions')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=14)

mysql = MySQL(app)


def create_test_users():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SHOW TABLES LIKE 'users'")
        result = cur.fetchone()

        if not result:
            cur.execute("""
                CREATE TABLE users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    email VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """)
            default_password = generate_default_password()
            cur.executemany("INSERT INTO users (email, password) VALUES (%s, %s)",
                            [("first@example.com", default_password), ("second@example.com", default_password)])
            mysql.connection.commit()

        cur.close()


def generate_default_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))


def is_logged_in():
    return 'user_id' in session


@app.route('/', methods=['GET'])
def hello():
    return 'It works.'


@app.route('/login', methods=['POST'])
@limiter.limit("3 per minute")
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


@app.route('/check-login', methods=['GET'])
def check_login():
    if is_logged_in():
        return jsonify(logged_in=True), 200
    else:
        return jsonify(logged_in=False), 401


if __name__ == '__main__':
    create_test_users()
    app.run(debug=True)
