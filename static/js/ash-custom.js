$(function () {
    $(document).scroll(function () {
        var $nav = $(".navbar-fixed");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
      });
  });