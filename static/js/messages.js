$(document).ready(function () {
    setTimeout(function () {
        console.log('message')
        let messages = document.getElementById('msg');
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }, 3000);
});