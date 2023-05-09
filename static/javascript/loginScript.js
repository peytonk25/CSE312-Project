function sendRegister() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const display = document.getElementById("display").value;
    var data = new FormData();
    data.append('username', username);
    data.append('password', password);
    data.append('display', display);
    const request = new XMLHttpRequest();
    request.open("POST", "/register");
    request.send(data);
}

function sendLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    var data = new FormData();
    data.append('username', username);
    data.append('password', password);
    const request = new XMLHttpRequest();
    request.open("POST", "/login");
    request.send(data);
}