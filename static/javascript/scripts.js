
var socket = io();




socket.on('connect', function() {
    socket.emit('connectionEstablished', {data: 'I\'m connected!'});
    var battleSpace1 = document.getElementById('optionRow')
    var battleSpace2 = document.getElementById('optionRow2');
    battleSpace1.style.display = "none"
    battleSpace2.style.display = "none"
});


function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
      if ((new Date().getTime() - start) > milliseconds){
        break;
      }
    }
  }

socket.on('initialize', function(data) {
    var battleSpace1 = document.getElementById('optionRow')
    var topName = data["top"]
    var bottomName = data["bottom"]
    document.getElementById("player1Name").innerHTML = topName
    document.getElementById("player2Name").innerHTML = bottomName


});


socket.on('reinitialize', function(data) {
    var topName = data["top"]
    var bottomName = data["bottom"]
    document.getElementById("player1Name").innerHTML = topName
    document.getElementById("player2Name").innerHTML = bottomName
    document.getElementById("optionRow").style.display = "flex"
    document.getElementById("optionRow2").style.display = "flex"


});






socket.on('p1win', function(data) {
    console.log("Choice made")
    var text = document.getElementById("middleMatchText");
    var player1Choice = document.getElementById("optionRow");
    player1Choice.innerHTML = '<img class="battleOption" src="static/images/'+data["player1"]+'.png">';
    var player2Choice = document.getElementById("optionRow2");
    player2Choice.innerHTML = '<img class="battleOption" src="static/images/'+data["player2"]+'.png">';
    player2Choice.style.display = "flex"
    text.innerHTML = data["users"][0]+" Wins";

    sleep(500)
    
    console.log("Done")
    socket.emit("reInitialize", {room: data['roomID']});

});

socket.on('p2win', function(data) {
    console.log("Choice made");
    var text = document.getElementById("middleMatchText");
    var player1Choice = document.getElementById("optionRow");
    player1Choice.innerHTML = '<img class="battleOption" src="static/images/'+data["player1"]+'.png">';
    var player2Choice = document.getElementById("optionRow2");
    player2Choice.innerHTML = '<img class="battleOption" src="static/images/'+data["player2"]+'.png">';
    player2Choice.style.display = "flex"
    text.innerHTML = data["users"][1]+" Wins";

    sleep(500)
    
    console.log("Done")
    socket.emit("reInitialize", {room: data['roomID']});

    

});

socket.on('tie', function() {
    console.log("Choice made");
    var text = document.getElementById("middleMatchText");
    text.innerHTML = "TIE";
});

function leaveRoom() {
    var ogUser = document.getElementById('player1Name').innerHTML
    console.log(ogUser)
    var room = document.getElementById('lobbyBanner').innerHTML.split("-")[1];
    socket.emit('leaveRoom', {roomID: room, user: ogUser});
    document.getElementById('lobbyBanner').innerHTML = "Lobby Menu"
    var battleSpace1 = document.getElementById('optionRow');
    var battleSpace2 = document.getElementById('optionRow2');
    battleSpace1.style.display = "none"
    battleSpace2.style.display = "none"
    document.getElementById("player1Name").innerHTML = ""
    document.getElementById("player2Name").innerHTML = ""

}


function createRoom() {
    var room = Math.floor(Math.random() * (999 - 100 + 1) + 100);   /* Insert user using cookie? */
    var p1 = document.getElementById("player1Name");
    socket.emit('createLobby', {roomID: room});
}

socket.on('createRoom', function(data) {
    document.getElementById('lobbyBanner').innerHTML = "Room - " + String(data["room"]) + " - Match In Progress";
    var battleSpace = document.getElementById('optionRow');
    battleSpace.style.display = "flex";
    document.getElementById("optionRow2").style.display = "flex";
    document.getElementById("player1Name").innerHTML = data["user"]
});


function joinRoom() {
    var idCheck = document.forms["joinForm"]["idBox"].value; /* Room number to check */
    console.log(idCheck);
    socket.emit('joinRoom', {roomID: idCheck});
}

socket.on('joinSuccess', function(data) {
    document.getElementById('lobbyBanner').innerHTML = "Room - " + data["room"] + " - Match In Progress";
    var p1 = document.getElementById("player1Name");
    p1.innerHTML = data["user"];
    var p2 = document.getElementById("player2Name");

    var battleSpace = document.getElementById('optionRow');
    battleSpace.style.display = "flex";
    document.getElementById("optionRow2").style.display = "flex";

    socket.emit("initialize", {room: data["room"]})
});




function rock() {
    var room = document.getElementById('lobbyBanner').innerHTML.split("-")[1]
    console.log(room)
    socket.emit('battle', {data: "rock", user: document.getElementById("player1Name").innerHTML, roomID: room});
}

function paper() {
    var room = document.getElementById('lobbyBanner').innerHTML.split("-")[1]
    console.log(room)
    socket.emit('battle', {data: "paper", user: document.getElementById("player1Name").innerHTML, roomID: room});
}

function scissors() {
    var room = document.getElementById('lobbyBanner').innerHTML.split("-")[1]
    console.log(room)
    socket.emit('battle', {data: "scissors", user: document.getElementById("player1Name").innerHTML, roomID: room});
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

