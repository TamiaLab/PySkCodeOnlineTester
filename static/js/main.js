$(".spoiler").each(function(index) {
	var t = $(this);
	t.hide();
	var l = $('<div><input type="button" value="Show spoiler"></div>');
	l.insertBefore($(this));
	l.click(function() {
		t.show();
		$(this).hide();
	});
});

$(".ispoiler").each(function(index) {
	var t = $(this);
	t.hide();
	var l = $('<input type="button" value="Show spoiler">');
	l.insertBefore($(this));
	l.click(function() {
		t.show();
		$(this).hide();
	});
});
