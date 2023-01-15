$(document).ready(function(){
  $(".course-row").not(':first').hover(
    function () {
      $(this).css("background","gray");
      $(this).css("cursor", "pointer");
    }, 
    function () {
      $(this).css("background","");
    }
  )});


$(document).ready(function(){
  $('.course-row').not(':first').click(function(){
    window.location = $(this).data('href');
    return false;
  });
});
