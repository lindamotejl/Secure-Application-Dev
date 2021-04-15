<script src="js/uikit.min.js"></script>
<script src="js/uikit-icons.min.js"></script>

$(document).ready(function () {

    $('#hamburger').click(function () {
        $(this).toggleClass('open');
        $('nav').toggleClass('show');
    });

});
