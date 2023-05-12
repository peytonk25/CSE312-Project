function sendRegister() {
    const username = document.getElementById("username").value.toUpperCase();
    const password = document.getElementById("password").value.toUpperCase();
    const display = document.getElementById("display").value.toUpperCase();
    const c_pass = document.getElementById("c_pass").value.toUpperCase();
    var data = new FormData();
    data.append('username', username);
    data.append('password', password);
    data.append('display', display);
    data.append('c_pass', c_pass);
    const request = new XMLHttpRequest();
    request.open("POST", "/register");
    request.send(data);
}

function sendLogin() {
    const username = document.getElementById("username").value.toUpperCase();
    const password = document.getElementById("password").value.toUpperCase();
    var data = new FormData();
    data.append('username', username);
    data.append('password', password);
    const request = new XMLHttpRequest();
    request.open("POST", "/login");
    request.send(data);

    
}

function edit() {
    const new_pass = document.getElementById("password").value;
    const new_display = document.getElementById("display").value;
    const c_pass = document.getElementById("c_pass").value;
    var data = new FormData();
    if (new_pass != "") {
        data.append('password', new_pass);
    }
    if (new_display != "") {
        data.append('display', new_display);
    }
    if (c_pass != "") {
        data.append('c_pass', c_pass);
    }
    const request = new XMLHttpRequest();
    request.open("POST", "/profile");
    request.send(data);
}