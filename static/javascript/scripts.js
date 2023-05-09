
var socket = io();

socket.on('connect', function() {
    socket.emit('connectionEstablished', {data: 'I\'m connected!'});
});





socket.on('choice1', function(x) {
    console.log("Choice made")
    var row = document.getElementById("optionRow")
    row.innerHTML = '<img class="battleOption" src="static/images/'+x+'.png">'
});

socket.on('choice2', function(x) {
    console.log("Choice made")
    var row = document.getElementById("optionRow2")
    row.innerHTML = '<img class="battleOption" src="static/images/'+x+'.png">'
});

socket.on('p1win', function() {
    console.log("Choice made")
    var text = document.getElementById("middleMatchText")
    text.innerHTML = "PLAYER 1 WINS"
});

socket.on('p2win', function() {
    console.log("Choice made")
    var text = document.getElementById("middleMatchText")
    text.innerHTML = "PLAYER 2 WINS"
});

socket.on('tie', function() {
    console.log("Choice made")
    var text = document.getElementById("middleMatchText")
    text.innerHTML = "TIE"
});


function createRoom() {
    socket.emit('createRoom', {data: 'user'})
    var p1 = document.getElementById("player1Name")
    p1.innerHTML = "User"
}

function joinRoom() {
    var idCheck = document.forms["joinForm"]["idBox"].value
    console.log(idCheck)
    socket.emit('joinRoom', {user: 'user2', id: idCheck})
    var p2 = document.getElementById("player2Name")
    p2.innerHTML = "User2"
}





function rock1() {
    socket.emit('battle', {data: "rock"});
}

function paper1() {
    socket.emit('battle', {data: "paper"});
}

function scissors1() {
    socket.emit('battle', {data: "scissors"});
}

function rock2() {
    socket.emit('battle2', {data: "rock"});
}

function paper2() {
    socket.emit('battle2', {data: "paper"});
}

function scissors2() {
    socket.emit('battle2', {data: "scissors"});
}