function menuOn() {
	if($('body').hasClass('page-template-work-php')) {
	    $('#menu').animate({
	        opacity : 1,
	        'height' : '110px'
	    }, 300, function() {
	        $('a', this).fadeIn(300);
	    });
	}
	else{
	    $('#menu').animate({
	        opacity : 1,
	        'margin-right' : '-1px',
	        width : '250px'
	    }, 500, function() {
	        $('a', this).fadeIn(500);
	    });
	}
}

// Just for fun
function funOn() {
	$('#fun').animate({
		top : '0px'
		}, 'slow');
}
function funOff() {
	$('#fun').animate({
		top : '-900px'
		}, 'slow');
}

// About section
function aboutOn() {
	$('#about').animate({
		top : '50%',
		'margin-top' : '-290px'
		}, 500);
	$('#card footer nav span:first-child').fadeOut(300);
}
function aboutOff() {
	$('#about').animate({
		top : '100%',
		'margin-top' : '80px'
		}, 500);
	$('#card footer nav span:first-child').fadeIn(300);
}

// Help section
function helpOn() {
	$('#help').fadeIn(500);
}
function helpOff() {
	$('#help').fadeOut(300);
}

// Contact form
function contactOn() {
	$('#contact').animate({
		top : '17%',
		'margin-top' : '0'
		}, 500);
	$('#card footer nav span:last-child').fadeOut(300);
}
function contactOff() {
	$('#contact').animate({
		top : '0',
		'margin-top' : '-770px'
		}, 500);
	$('#card footer nav span:last-child').fadeIn(300);
}

function clock(){
	setInterval( function() {
	var seconds = new Date().getSeconds();
	var sdegree = seconds * 6;
	var srotate = "rotate(" + sdegree + "deg)";

	$("#sec").css({"-moz-transform" : srotate, "-webkit-transform" : srotate});

	}, 1000 );


	setInterval( function() {
	var hours = new Date().getHours();
	var mins = new Date().getMinutes();
	var hdegree = hours * 30 + (mins / 2);
	var hrotate = "rotate(" + hdegree + "deg)";

	$("#hour").css({"-moz-transform" : hrotate, "-webkit-transform" : hrotate});

	}, 1000 );


	setInterval( function() {
	var mins = new Date().getMinutes();
	var mdegree = mins * 6;
	var mrotate = "rotate(" + mdegree + "deg)";

	$("#min").css({"-moz-transform" : mrotate, "-webkit-transform" : mrotate});

	}, 1000 );

}

$(document).ready(function() {
	clock();
	$('#res').load('resources/res.html');
	$('.open-res').toggle(function() {
		$('#res').fadeIn(300);
	}, function() {
		$('#res').fadeOut(300);
	});

	$('#about').rotate({angle:15});
	// Rotate the Help section
	$('#help').rotate({angle:15});
	// Rotate the Settings section
	$('#settings').rotate({angle:15});
	// Rotate the Contact form
	$('#contact').rotate({angle:-25});
	// Hide the drawer
	$('#fun').css('top', '-900px');

	// Just for fun
	$('#menu span').click(function() {
		funOn();
	});

	// About section interaction
	$('#card footer nav span:first-child').click(function() {
		$('#about').rotate({animateTo:0});
		aboutOn();
	});

	// Help section interaction
	$('.help').click(function() {
		$('#help').rotate({animateTo:0});
		helpOn();
	});

	// Contact form interaction
	$('#card footer nav span:last-child').click(function() {
		$('#contact').rotate({animateTo:0});
		contactOn();
	});

	// Close button
	$('span.close').html('X');
	$('#fun span.close').click(function(){ funOff(); });
	$('#about span.close').click(function(){ aboutOff(); $('#about').rotate({animateTo:15}); });
	$('#help').click(function(){ helpOff(); $('#help').rotate({animateTo:15}); });
	$('#contact span.close').click(function(){ contactOff(); $('#contact').rotate({animateTo:-25}); });

	// Drag'em around!
	$( "#contact , #settings , #about , #work ul li").draggable();

    // Start up the menu
    menuOn();

    $('#search-me input').keyup(function(){
        var sortQuery = $(this).val();
        $('article').each(function(){
            var dataSortValue = $(this).attr('data-sort');

            reg = new RegExp('\('+sortQuery+'\)' , 'gi');
            //alert(reg);

            if (dataSortValue.match(reg)) { 
                $(this).fadeIn(300);
            }
            else{
                $(this).fadeOut(300);
            }

        });
    });

	$('#work li .view-case-study').click(function(){
		$('body.page-template-work-php').animate({backgroundPosition: '50% -590px'}, 1000);
		$('.before').animate({ 'margin-top': '-590px' }, 1000);
		$('#work').animate({ 'top': '190px' }, 300);
		$('footer').fadeOut(300);
		$('body.page-template-work-php #start').fadeOut(300);
		$('body.page-template-work-php #menu').fadeOut(300);
		$('body.page-template-work-php #card').animate({ 'top': '0' }, 600);
		$(this).parent().animate({ 
			'top' : '0',
			'left' : '0',
			'width' : '100%'
		}, 500);
		$(this).parent().draggable('disable').css({ 'cursor' : 'default', 'position' : 'static' , 'margin-top' : '630px' , 'margin-bottom' : '250px' });
		$(this).parent().siblings().fadeOut(200);
		var workload = $(this).attr('data-ajax');
		$(this).siblings('h4').fadeOut(200);
		$(this).siblings('p').fadeOut(200);
		$(this).fadeOut(200);
		$(this).siblings('.workload').load(workload);
	});


 });

