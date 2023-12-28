/*
This file ensures messages, aren't stuck on screen and close after 3s
*/

$(document).ready(function () {
    // set time out for bootstrap message function
    setTimeout(function () {
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        // close alert after 3000ms = 3s
        alert.close();
    }, 3000);
});