/**
 * Created by aditya on 7/20/17.
 */


// this function is used to remove transparency from navbar when scrolled down.
$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    if (scroll >= 60) {
        $(".navbar").removeClass("navbar-transparent");
    } else {
        $(".navbar").addClass("navbar-transparent");
    }
});
