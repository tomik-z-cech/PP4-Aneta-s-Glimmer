/*
This script ensures functionality of styles liking, trying and commenting
*/
$(document).ready(function () {
    // if canComment true, hide the initial comment form
    if (canComment == 'True') {
        $('#comments, #commentForm').hide();
    }
    // if this button clicked, run try function
    $('#tryButton').click(function () {
        $('#tryForm').submit();
    });
    // if this button clicked, run like function
    $('#likeButton').click(function () {
        $('#likeForm').submit();
    });
    // if this button clicked, show comments
    $('#showComments').click(function (event) {
        event.preventDefault();
        $('#comments, #commentForm').show();
    });
});