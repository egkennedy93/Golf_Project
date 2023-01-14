$(document).ready(function(){
  $("tr").not(':first').hover(
    function () {
      $(this).css("background","gray");
      $(this).css("cursor", "pointer");
    }, 
    function () {
      $(this).css("background","");
    }
  )});

$(document).ready(function(){
      $('table tr').click(function(){
        window.location = $(this).data('google.com');
        return false;
      });
    });
