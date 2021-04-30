jQuery(document).ready(function($) {
	"use strict";
	//Search
	$('#search .search-btn').on('click', function(event) {
		event.preventDefault();
		$('body').prepend('<div id="search-full" class="fadeIn"> <button id="exit-search-box"><i class="fas fa-times"></i></button> <div class="search-box"> <form action="" method="get" class="animated fadeInDown"> <input type="text" placeholder="Search"> <button><i class="fas fa-arrow-right"></i></button> </form> </div></div>').fadeIn('300', function() {
			
		});
		$('#exit-search-box').on('click', function(event) {
			event.preventDefault();
			$('#search-full').fadeOut('300', function() {
				$(this).remove();
			});;
		});
	});
	//Navigation
	$(window).on('scroll', function(event) {
	    var scroll = $(window).scrollTop();
	    if (scroll >= 100) {
	        $("header .header-wrapper").css({
	        	padding: '10px 0',
	        });
	    }
	    else {
	        $("header .header-wrapper").css({
	        	padding: '25px 0',
	        });
	    }
	});
	// Mobile submenu open
	$('.submenu-opener').on('click', function(event) {
		event.preventDefault();
		$(this).toggleClass('fa-plus fa-minus');
		$(this).next().slideToggle()
	});
	// Click to open sidebar menu
	$('#showMenu').on('click', function(event) {
		event.preventDefault();
		$('header').append('<div id="overlay"></div>')
		$('.navigation').css({
			left: '0%',
			visibility: 'visible',
		});
		$('#overlay').on('click', function(event) {
			$(this).remove();
			$('.navigation').css({
				left: '-100%',
				visibility: 'hidden',
			});
		});
	});
	// Mobile Navigation
	(function($) {
		function mediaSize() { 
			if (window.matchMedia('(min-width: 1200px)').matches) {
				$('.navigation').removeAttr('style')
				$('.navigation .sub-menu').removeAttr('style')
				$('#overlay').remove()
				$('header').removeClass('mobile')
			}
			else {
				$('header').addClass('mobile')
			}
		};
	 	mediaSize();
		window.addEventListener('resize', mediaSize, false);  
	})(jQuery);
	/************************************
   		Masonry layout init
	*************************************/
	var $container = $('.blog-masonry_wrapper')

	$container.imagesLoaded(function() {
	  	$container.masonry({
	  		itemSelector: '.post-block',
		})
	});
	/************************************
   		Scroll up init
	*************************************/
	$.scrollUp({
		scrollDistance: 300,
		scrollText: '<i class="fas fa-chevron-up"></i>',
		easingType: 'easeOutCubic',
		scrollSpeed: 1500,
	});
});