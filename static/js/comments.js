$(document).ready(function () {
    if (canComment == 'True') {
        $('#comments, #commentForm').hide();
    }
    $('#tryButton').click(function () {
        $('#tryForm').submit();
    });
    $('#likeButton').click(function () {
        $('#likeForm').submit();
    });
    $('#showComments').click(function () {
        $('#comments, #commentForm').show();
    });
});