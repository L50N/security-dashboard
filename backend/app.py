from flask import Flask, request, jsonify, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Enable CORS with supports_credentials=True to allow credentials (cookies)

app.secret_key = 'b_5#y2L"F4Q8z\n\xec]/'

users = {
    'user1@example.com': {'password': 'password1'},
    'user2@example.com': {'password': 'password2'}
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if email in users and users[email]['password'] == password:
        session['email'] = email
        return jsonify({'message': 'Login successful', 'loggedIn': True}), 200
    else:
        return jsonify({'message': 'Invalid email or password', 'loggedIn': False}), 401

@app.route('/check-login')
def check_login():
    loggedIn = 'email' in session
    return jsonify({'loggedIn': loggedIn})

@app.route('/logout')
def logout():
    session.pop('email', None)
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/')
def hello():
    return 'Hello, World! This is your dashboard backend.'

if __name__ == '__main__':
    app.run(debug=True)
