from ntpath import join
from flask import Flask, render_template
from flask_socketio import *
import rps 
from random import *

class playerChoices: 
    player1 = ""
    player2 = ""
    roomID = 0

newGame = playerChoices
rooms = {} # Dictionary format is: { roomID: [list of users in the room] }


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)





@socketio.on('connectionEstablished')
def handle_ping(data):
    print(data['data'])



@socketio.on('createRoom')
def makeLobby(data):
    roomID = data['roomID']
    username = data['data']
    room = roomID
    join_room(room)
    rooms[roomID] = ['User']
    print("User has joined room "+ str(room))


@socketio.on('joinRoom')
def joinLobby(data):
    roomID = int(data['roomID'])
    user = data['user']
    print(roomID)
    if int(roomID) in rooms:
        print("ID MATCHES")
        print(rooms)
        join_room(roomID)
        rooms[roomID].append("User2")
        print("User2 has joined room " + str(roomID))
    print("Nothing")


@socketio.on('battle')
def handle_battle1(data):
    username = data['user']
    newGame.player1 = data['data']
    print(newGame.player1)
    print(newGame.player2)
    if newGame.player1 and newGame.player2:
        result = rps.rps(newGame.player1, newGame.player2)
        for room in rooms:
            for user in rooms[room]:
                if user == username:
                    roomID = room
        print(room)
        if result == 1:
            emit('p1win', {"player1": newGame.player1, "player2": newGame.player2}, room=roomID)
        elif result == 2:
            emit('p2win', {"player1": newGame.player1, "player2": newGame.player2}, room=roomID)
        else:
            emit('tie', {"player1": newGame.player1, "player2": newGame.player2}, room=roomID)
        newGame.player1 = ""
        newGame.player2 = ""



@socketio.on('battle2')
def handle_battle2(data):
    username = data['user']
    newGame.player2 = data['data']
    print(newGame.player1)
    print(newGame.player2)
    if newGame.player1 and newGame.player2:
        result = rps.rps(newGame.player1, newGame.player2)
        for room in rooms:
            for user in rooms[room]:
                if user == username:
                    print("User found in match")
                    roomID = room
                    if result == 1:
                        emit('p1win', {"player1": newGame.player1, "player2": newGame.player2}, room=roomID)
                    elif result == 2:
                        emit('p2win', {"player1": newGame.player1, "player2": newGame.player2}, room=roomID)
                    else:
                        emit('tie', {"player1": newGame.player1, "player2": newGame.player2}, room=roomID)
        newGame.player1 = ""
        newGame.player2 = ""


@socketio.on('checkLobbies')
def checkLobbies():
    print(rooms)



    

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/match')
def match():
    return render_template('match.html')


if __name__ == '__main__':
    socketio.run(app, port=8001)
