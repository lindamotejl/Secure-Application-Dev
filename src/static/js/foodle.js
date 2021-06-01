
$(document).ready(function () {

    $('#hamburger').click(function () {
        $(this).toggleClass('open');
        $('nav').toggleClass('show');
    });

});

$(document).ready(function(){
     $(window).scroll(function(){
         $("#hero").css("opacity", 1 - $(window).scrollTop() /1200);
     });
 });

 $(document).ready(function() {
    const heart = document.querySelectorAll(".fa-heart");
	heart.forEach(heart => {
  heart.addEventListener('click',  function() {
    heart.classList.toggle('red');
  });
});
 });