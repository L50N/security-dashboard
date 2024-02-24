from flask import Flask, request, jsonify, session
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.secret_key = 'your_secret_key_here'

users = {
    'leon@example.com': {'password': 'changeme'},
    'john@example.com': {'password': 'changeme'}
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
    logged_in = 'email' in session
    user = session.get('email', None)
    return jsonify({'loggedIn': logged_in, 'user': user})

@app.route('/logout')
def logout():
    session.pop('email', None)
    return jsonify({'message': 'Logged out successfully'}), 200

@app.route('/')
def home():
    return 'It works.'

if __name__ == '__main__':
    app.run(debug=True)
