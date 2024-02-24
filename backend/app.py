from flask import Flask, request, jsonify, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'WILL::BE::REPLACED::BY::INSTALLER' ## WILL::BE::REPLACED::BY::INSTALLER

app.config['MYSQL_HOST'] = 'localhost' ## DEFAULT::HOST
app.config['MYSQL_USER'] = 'root' ## DEFAULT::USER
app.config['MYSQL_PASSWORD'] = 'default' ## DEFAULT::PASSWORD
app.config['MYSQL_DB'] = 'default' ## DEFAULT::DATABASE

mysql = MySQL(app)

def hash_password(password):
    return generate_password_hash(password)

def create_test_users():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        count = cur.fetchone()[0]
        if count == 0:
            hashed_password = hash_password("password")
            cur.execute("INSERT INTO users (email, password) VALUES (%s, %s)", ("first@example.com", hashed_password))
            cur.execute("INSERT INTO users (email, password) VALUES (%s, %s)", ("second@example.com", hashed_password))
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

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, email, password FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()

    if user:
        stored_password_hash = user[2]
        password_check_result = (stored_password_hash == password)
        if password_check_result:
            session['user_id'] = user[0]
            return jsonify(message="200: The login was successful!"), 200
        else:
            return jsonify(message="401: The user exists, but the password entered is incorrect!"), 401
    else:
        print("The user is not known to us.")
        return jsonify(message="401: The user is not known to us."), 401

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return jsonify(message="200: Logging out was successful!"), 200

@app.route('/check-login')
def check_login():
    if 'user_id' in session:
        return jsonify(logged_in=True), 200
    else:
        return jsonify(logged_in=False), 401

if __name__ == '__main__':
    app.run(debug=True)