$(document).ready(function() {
    $(".review .star-rating").mouseover(function() {
        
        let starIndex = $(this).index();
        let spanIndex = $('.review').index($(this).closest('.review'));
        console.log("In" + spanIndex + "---" + starIndex)
        $(".review:eq(" + spanIndex + ") a:lt(" + starIndex + ")").html(onStar);
        $(".review:eq(" + spanIndex + ") a:eq(" + starIndex + ")").html(onStar);
        $(".review:eq(" + spanIndex + ") a:gt(" + starIndex + ")").html(offStar);
    });
    $(".review .star-rating").mouseout(function() {
        let starIndex = $(this).index();
        let spanIndex = $('.review').index($(this).closest('.review'));
        console.log("Out" + spanIndex + "---" + starIndex)
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