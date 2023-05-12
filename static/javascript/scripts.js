
var socket = io();


socket.on('connect', function() {
    socket.emit('connectionEstablished', {data: 'I\'m connected!'});
    var battleSpace = document.getElementById('battleground');
    battleSpace.style.display = "none"
});




socket.on('p1win', function(data) {
    console.log("Choice made")
    var text = document.getElementById("middleMatchText");
    var player1Choice = document.getElementById("optionRow");
    player1Choice.innerHTML = '<img class="battleOption" src="static/images/'+data["player1"]+'.png">';
    var player2Choice = document.getElementById("optionRow2");
    player2Choice.innerHTML = '<img class="battleOption" src="static/images/'+data["player2"]+'.png">';
    text.innerHTML = "PLAYER 1 WINS";
});

socket.on('p2win', function() {
    console.log("Choice made");
    var text = document.getElementById("middleMatchText");
    var player1Choice = document.getElementById("optionRow");
    player1Choice.innerHTML = '<img class="battleOption" src="static/images/'+data["player1"]+'.png">';
    var player2Choice = document.getElementById("optionRow2");
    player2Choice.innerHTML = '<img class="battleOption" src="static/images/'+data["player2"]+'.png">';
    text.innerHTML = "PLAYER 2 WINS";
});

socket.on('tie', function() {
    console.log("Choice made");
    var text = document.getElementById("middleMatchText");
    text.innerHTML = "TIE";
});


function createRoom() {
    var room = Math.floor(Math.random() * (999 - 100 + 1) + 100);
    socket.emit('createRoom', {data: 'user', roomID: room});
    var p1 = document.getElementById("player1Name");
    p1.innerHTML = "User";
    document.getElementById('matchHeader').innerHTML = "Room " + String(room) + " - Match In Progress"
    var battleSpace = document.getElementById('battleground');
    battleSpace.style.display = "block"
}



function joinRoom() {
    var idCheck = document.forms["joinForm"]["idBox"].value;
    console.log(idCheck);
    socket.emit('joinRoom', {user: 'user2', roomID: idCheck});
    var p2 = document.getElementById("player2Name");
    p2.innerHTML = "User2";
    document.getElementById('matchHeader').innerHTML = "Room " + idCheck + " - Match In Progress"
    var battleSpace = document.getElementById('battleground');
    battleSpace.style.display = "block"
}

function toMatch() {
    location.href = 'match';
}
function toProfile() {
    location.href = 'profile';
}
function toLeaderboard() {
    location.href = 'leaderboard';
}

function rock1() {
    socket.emit('battle', {data: "rock", user: "User"});
}

function paper1() {
    socket.emit('battle', {data: "paper", user: "User"});
}

function scissors1() {
    socket.emit('battle', {data: "scissors", user: "User"});
}

function rock2() {
    socket.emit('battle2', {data: "rock", user: "User2"});
}

function paper2() {
    socket.emit('battle2', {data: "paper", user: "User2"});
}

function scissors2() {
    socket.emit('battle2', {data: "scissors", user: "User2"});
}



