$(document).ready(function () {
    if (canComment == 'True') {
        $('#comments, #commentForm').hide();
    }
    $('#likeButton').click(function () {
        $('#likeForm').submit();
    });
    $('#showComments').click(function () {
        $('#comments, #commentForm').show();
    });
});