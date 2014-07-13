$(document).ready(function(){
	$('.main-nav-wrapper>ul>li>a.js-main-category').click(function() {
		$clicked = $(this);		
		// console.log($clicked);
		// console.log($clicked.hasClass('active'));
		if($clicked.hasClass('active')){
			inactive();
			subNavUp();
			clickOff($clicked);
			hideSubNavContent();
		}else{
			inactive();
			showSubNavContent($clicked);			
			subNavDown();
			clickOn($clicked);
		}
		closeClick();
	});
});

function subNavUp(){
	$subNav = $('.sub-nav');	
	$subNav.removeClass('active');
	$subNav.slideUp(200);	
}

function subNavDown(){
	$subNav = $('.sub-nav');	
	$subNav.addClass('active');
	$subNav.slideDown(200);	
}

function clickOn(clicked){
	clicked.addClass('active');
}

function clickOff(clicked){
	clicked.removeClass('active');
}

function inactive(){
	$('.main-nav-wrapper>ul>li>a.js-main-category').removeClass('active');
}

function hideSubNavContent(){
	$('.sub-nav-content-wrapper').hide();
	// $('.sub-nav-content-wrapper').each(function(){
	// 	$(this).hide();
	// });
}

function showSubNavContent(clicked){
	var toShow = clicked.data('category');
	hideSubNavContent();
	$("#"+toShow).addClass('shown');
	$("#"+toShow).show();

}

function closeClick(){
	$('html').click(function(e){
		// console.log($(e.target).parents('.nav-wrapper'));
		// console.log($(e.target).parents('.main-nav'));
		if($(e.target).parents('.nav-wrapper').length >= 1){
			// 
			// console.log("Is Nav.");
		}else{
			e.preventDefault();
			subNavUp();
			inactive();
			// console.log("Not Nav.");
		}
	});
}


//   DIVIDING LINE - Menu Works Above This

// function activeMenuCheck(clicked){
// 	$('.main-nav-wrapper>ul>li>a.js-main-category').each(function(){

// 		if(clicked.hasClass('active')){
			// subNaver();			
// 			return false;
// 		}else{
// 			// if($(this).hasClass('active')){
// 			// 	$(this).removeClass('active')
// 			// 	return false;
// 			// }else{
// 			// 	// subNaver();
// 			// }
// 		}
// 	});
// }

// function subNaver(){
// 	$subNav = $('.sub-nav');
// 		if($subNav.hasClass('active')){
// 			$subNav.removeClass('active');
// 			$subNav.slideUp();
// 		}else{
// 			$subNav.addClass('active');
// 			$subNav.slideDown();
// 		}
// }

// if($this.hasClass('active')){
// 	$this.removeClass('active');
// }else{
// 	$this.addClass('active');
// }