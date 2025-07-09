import os
os.environ["EVENTLET_NO_GREENDNS"] = "yes"

from flask import Flask, request, jsonify, send_from_directory
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from encryption import generate_rsa_keys

# Setup Flask app to serve from current directory
app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# In-memory user storage
users_db = {}

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    if username in users_db:
        return jsonify({'status': 'fail', 'message': 'User already exists'})
    pub, priv = generate_rsa_keys()
    users_db[username] = {
        'password': data['password'],
        'avatar': data.get('avatar', ''),
        'rsa_pub': pub,
        'rsa_priv': priv
    }
    return jsonify({'status': 'success'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    if username not in users_db or users_db[username]['password'] != data['password']:
        return jsonify({'status': 'fail', 'message': 'Invalid credentials'})
    return jsonify({'status': 'success', 'avatar': users_db[username]['avatar']})

@socketio.on('send_message')
def handle_message(data):
    emit('receive_message', data, broadcast=True)

if __name__ == '__main__':
    # Replace this with your IPv4 address if hosting on local network
    socketio.run(app, host='192.168.10.96', port=5050, debug=True)
