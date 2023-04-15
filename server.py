from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('ping')
def handle_ping():
    emit('pong', {'data': 'Pong!'})

if __name__ == '__main__':
    socketio.run(app, port=8001)
