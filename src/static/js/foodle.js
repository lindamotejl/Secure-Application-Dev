
$(document).ready(function () {

    $('#hamburger').click(function () {
        $(this).toggleClass('open');
        $('nav').toggleClass('show');
    });

});

$(document).ready(function(){
     $(window).scroll(function(){
         $("#hero").css("opacity", 1 - $(window).scrollTop() /1500);
     });
 });