from ntpath import join
from flask_socketio import *
from random import *

class playerChoices: 
    player1 = ""
    player2 = ""

newGame = playerChoices
rooms = []

import random
import string
from urllib import request
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO, emit
import database
import rps
import bcrypt

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

@app.route('/login', methods=["GET", "POST"])
def login():
    
    data = request.form.to_dict()
    if request.method == "POST" and 'redirect' in data:
        if data['redirect'] == 'true':
            return redirect(url_for('register'))
    elif request.method == "POST" and 'username' in data and 'password' in data:
        username = data['username']
        username = username.replace("&", '&amp;')
        username = username.replace("<", '&lt;')
        username = username.replace(">", '&gt;')
        password = data['password']
        password = password.replace("&", '&amp;')
        password = password.replace("<", '&lt;')
        password = password.replace(">", '&gt;')
        check = False
        for i in database.users_coll.find({'username': str(username)}):
            check = True
        if check:
            for i in database.users_coll.find({'username': str(username)}):
                print(i)
                hash = bcrypt.hashpw(bytes(password, 'utf-8'), i['salt'])
                if hash == i['password']:
                    #Logged In
                    print("WOOOOOOO")
        else:
            print("Not found")
    
    return render_template('login.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    data = request.form.to_dict()
    if request.method == "POST" and 'redirect' in data:
        if data['redirect'] == 'true':
            return redirect(url_for('login'))
    elif request.method == "POST" and 'username' in data and 'password' in data:
        username = data['username']
        username = username.replace("&", '&amp;')
        username = username.replace("<", '&lt;')
        username = username.replace(">", '&gt;')
        check = False
        for i in database.users_coll.find({'username': str(username)}):
            check = True
        if check:
            print("wha")
        else:
            password = data['password']
            password = password.replace("&", '&amp;')
            password = password.replace("<", '&lt;')
            password = password.replace(">", '&gt;')
            display = data['display']
            display = display.replace("&", '&amp;')
            display = display.replace("<", '&lt;')
            display = display.replace(">", '&gt;')
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(bytes(password, 'utf-8'), salt)
            letters = string.ascii_letters
            token = ''.join(random.choice(letters) for i in range(10))
            token_hash = bcrypt.hashpw(bytes(token, 'utf-8'), salt)
            print(password, display, token)
            database.users_coll.insert_one({'display': display, 'username': username, 'password': hash, 'salt': salt, 'auth': token_hash})
            for i in database.users_coll.find({}):
                print(i)
    
    return render_template('register.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/match')
def match():
    return render_template('match.html')


if __name__ == '__main__':
    socketio.run(app, port=8000, allow_unsafe_werkzeug=True, host='0.0.0.0')
