$(function() {
  $('.iban input').on('input', function() {
    var len = $(this).val().length;
    if (len === 4) {
      $(this).next().focus();
    } else if (len === 0) {
      var $prev = $(this).prev();
      if ($prev.length) {
        $prev.focus();
        $prev[0].setSelectionRange(4, 4);
      }
    }
  });
});
