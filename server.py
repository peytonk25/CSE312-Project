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
from flask import Flask, render_template, request, redirect, url_for, session
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

    

@app.route('/', methods=['GET'])
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
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
                hash = bcrypt.hashpw(str(password).encode('utf-8'), i['salt'])
                if hash == i['password']:
                    #Logged In
                    session['username'] = username
                    return redirect(url_for('index'))
                else:
                    return render_template('login.html', error="Incorrect Login")
        else:
            return render_template('login.html', error="Incorrect Login")
    else:
        return render_template('login.html', error="")

@app.route('/register', methods=["GET", "POST"])
def register():
    data = request.form.to_dict()
    if request.method == "POST" and 'redirect' in data:
        if data['redirect'] == 'true':
            return redirect(url_for('login'))
    elif request.method == "POST" and 'username' in data and 'password' in data and 'display' in data and 'c_pass' in data:
        print(data)
        username = data['username']
        username = username.replace("&", '&amp;')
        username = username.replace("<", '&lt;')
        username = username.replace(">", '&gt;')
        check = False
        for i in database.users_coll.find({'username': str(username)}):
            check = True
        if check:
            return render_template('register.html', error="Username Already In Use")
        else:
            password = data['password']
            c_pass = data['c_pass']
            password = password.replace("&", '&amp;')
            password = password.replace("<", '&lt;')
            password = password.replace(">", '&gt;')
            c_pass = c_pass.replace("&", '&amp;')
            c_pass = c_pass.replace("<", '&lt;')
            c_pass = c_pass.replace(">", '&gt;')
            print(password, c_pass)
            if c_pass != password:
                return render_template('register.html', error="Invalid Password")
            else:
                display = data['display']
                display = display.replace("&", '&amp;')
                display = display.replace("<", '&lt;')
                display = display.replace(">", '&gt;')
                salt = bcrypt.gensalt()
                hash = bcrypt.hashpw(bytes(password, 'utf-8'), salt)
                letters = string.ascii_letters
                token = ''.join(random.choice(letters) for i in range(10))
                token_hash = bcrypt.hashpw(bytes(token, 'utf-8'), salt)
                database.users_coll.insert_one({'display': display, 'username': username, 'password': hash, 'salt': salt, 'auth': token_hash})
                session['username'] = username
                return redirect(url_for('index'))

    return render_template('register.html', error="")

@app.route('/profile', methods=["GET", "POST"])
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        for i in database.users_coll.find({'username': str(session['username'])}):
            username = i['username']
            display = i['display']
        data = request.form.to_dict()
        print(data)
        if request.method == "POST":
            if 'password' in data:
                if 'c_pass' in data:
                    new_pass = data['password']
                    c_pass = data['c_pass']
                    if c_pass == new_pass:
                        new_hash = bcrypt.hashpw(new_pass.encode('utf-8'), i['salt'])
                        for i in database.users_coll.find({'username': str(username)}):
                            database.users_coll.update_one({"_id": i['_id']},{"$set":{"password": new_hash}})
                    else:
                        return render_template('profile.html', username=username, display=display, error="Passwords Do Not Match")
                else:
                    return render_template('profile.html', username=username, display=display, error="Please Confirm New Password")
            if 'display' in data:
                new_display = data['display']
                for i in database.users_coll.find({'username': str(username)}):
                    database.users_coll.update_one({"_id": i['_id']},{"$set":{"display": str(new_display)}})

            
        return render_template('profile.html', username=username, display=display, error="")

@app.route('/match')
def match():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        return render_template('match.html')


if __name__ == '__main__':
    socketio.run(app, port=8000, allow_unsafe_werkzeug=True, host='0.0.0.0')
