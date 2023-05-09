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

@socketio.on('ping')
def handle_ping():
    emit('pong', {'data': 'Pong!'})

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

@app.route('/match')
def match():
    return render_template('match.html')


if __name__ == '__main__':
    socketio.run(app, port=8000, allow_unsafe_werkzeug=True, host='0.0.0.0')
