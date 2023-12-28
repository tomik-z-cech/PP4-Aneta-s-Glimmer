/*
This file ensures displaying onStars and offStars defined in html template
over rating stars div
*/
$(document).ready(function() {
    // Triggers mouseover function
    $(".review .star-rating").mouseover(function() {
        let starIndex = $(this).index();
        let spanIndex = $('.review').index($(this).closest('.review'));
        console.log("In" + spanIndex + "---" + starIndex)
        // display onStars in current review div on star index less and equal to index
        // display offStar on each index greater than index
        $(".review:eq(" + spanIndex + ") a:lt(" + starIndex + ")").html(onStar);
        $(".review:eq(" + spanIndex + ") a:eq(" + starIndex + ")").html(onStar);
        $(".review:eq(" + spanIndex + ") a:gt(" + starIndex + ")").html(offStar);
    });
    $(".review .star-rating").mouseout(function() {
        let starIndex = $(this).index();
        let spanIndex = $('.review').index($(this).closest('.review'));
        //display offStars on lesser, equal and greater review index
        //all star index
        $(".review:lt(" + spanIndex + ") a:lt(" + starIndex + ")").html(offStar);
        $(".review:lt(" + spanIndex + ") a:eq(" + starIndex + ")").html(offStar);
        $(".review:lt(" + spanIndex + ") a:gt(" + starIndex + ")").html(offStar);
        $(".review:eq(" + spanIndex + ") a:lt(" + starIndex + ")").html(offStar);
        $(".review:eq(" + spanIndex + ") a:eq(" + starIndex + ")").html(offStar);
        $(".review:eq(" + spanIndex + ") a:gt(" + starIndex + ")").html(offStar);
        $(".review:gt(" + spanIndex + ") a:lt(" + starIndex + ")").html(offStar);
        $(".review:gt(" + spanIndex + ") a:eq(" + starIndex + ")").html(offStar);
        $(".review:gt(" + spanIndex + ") a:gt(" + starIndex + ")").html(offStar);
    });
});