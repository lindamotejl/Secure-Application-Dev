$(document).ready(function () {

    $('#hamburger').click(function () {
        $(this).toggleClass('open');
        $('nav').toggleClass('show');
    });

});
