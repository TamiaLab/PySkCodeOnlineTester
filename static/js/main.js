/* Back to top button */

$(document).ready(function () {
    $(window).scroll(function () {
        var back_to_top = $('#back-to-top');
        if ($(this).scrollTop() > 50) {
            back_to_top.fadeIn();
        } else {
            back_to_top.fadeOut();
        }
    });
    // scroll body to 0px on click
    var back_to_top = $('#back-to-top');
    back_to_top.click(function () {
        back_to_top.tooltip('hide');
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
    back_to_top.tooltip('show');
});


/* Spoiler box */

$(".spoiler").each(function(index) {
    var t = $(this);
    t.hide();
    var l = $('<div><input type="button" value="Voir le texte caché"></div>');
    l.insertBefore($(this));
    l.click(function() {
        t.show();
        $(this).hide();
    });
});


/* Spoiler inline */

$(".ispoiler").each(function(index) {
    var t = $(this);
    t.hide();
    var l = $('<input type="button" value="Voir le texte caché">');
    l.insertBefore($(this));
    l.click(function() {
        t.show();
        $(this).hide();
    });
});
