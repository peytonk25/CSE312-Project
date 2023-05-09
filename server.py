from ntpath import join
from flask import Flask, render_template
from flask_socketio import *
import rps 
from random import *

class playerChoices: 
    player1 = ""
    player2 = ""

newGame = playerChoices
rooms = []


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)





@socketio.on('connectionEstablished')
def handle_ping(data):
    print(data['data'])



@socketio.on('createRoom')
def makeLobby(data):
    gameID = randint(100, 999) 
    username = data['data']
    room = gameID
    join_room(room)
    rooms.append(room)
    print("User has joined room "+ str(room))


@socketio.on('joinRoom')
def joinLobby(data):
    id = data['id']
    user = data['user']
    print(user)
    if int(id) in rooms:
        print("Good to join room")
    print("Nothing")


@socketio.on('battle')
def handle_battle1(data):
    newGame.player1 = data['data']
    print(newGame.player1)
    print(newGame.player2)
    if newGame.player1 and newGame.player2:
        result = rps.rps(newGame.player1, newGame.player2)
        newGame.player1 = ""
        newGame.player2 = ""
        if result == 1:
            emit('p1win')
        elif result == 2:
            emit('p2win')
        else:
            emit('tie')

    emit('choice1', data['data'])


@socketio.on('battle2')
def handle_battle2(data):
    newGame.player2 = data['data']
    print(newGame.player1)
    print(newGame.player2)
    if newGame.player1 and newGame.player2:
        result = rps.rps(newGame.player1, newGame.player2)
        newGame.player1 = ""
        newGame.player2 = ""
        if result == 1:
            emit('p1win')
        elif result == 2:
            emit('p2win')
        else:
            emit('tie')
    emit('choice2', data['data'])

    

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/match')
def match():
    return render_template('match.html')


if __name__ == '__main__':
    socketio.run(app, port=8001)
