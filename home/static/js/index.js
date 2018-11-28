var Index =0;
    var interval;
function IntervalRun(){
	if(interval){
		return;
	}
	interval = setInterval(function(){
		$('.case_box').eq(Index).addClass('box_active');
		$('.case_box').eq(Index).siblings('.case_box').removeClass('box_active');
		$('.case_choose').eq(Index).addClass('active');
		$('.case_choose').eq(Index).siblings('.case_choose').removeClass('active');
		Index++;
		if(Index==$('.case_box').length){
			Index =0;
		}
	},3000)
}
IntervalRun();
$('.case_choose').click(function(){
	Index = $(this).index();
	$('.case_box').eq(Index).addClass('box_active');
	$('.case_box').eq(Index).siblings('.case_box').removeClass('box_active');
	$('.case_choose').eq(Index).addClass('active');
	$('.case_choose').eq(Index).siblings('.case_choose').removeClass('active');
	console.log($(this).index())
})
$('.case_boxes').mouseleave(function(){
	IntervalRun();
})
$('.case_boxes').mouseenter(function(){
	clearInterval(interval);
	interval = undefined;
})

//  案例 

function imgReload(){
	var imgHeight = 0;
	var wtmp = $("body").width();
	$("#b06 ul li").each(function(){
        $(this).css({width:wtmp + "px"});
    });
	$(".sliderimg").each(function(){
		$(this).css({width:wtmp + "px"});
		imgHeight = $(this).height();
	});
}
$(window).resize(function(){imgReload();});
$(document).ready(function(e) {
	imgReload();
    var unslider06 = $('#b06').unslider({
		dots: true,
		fluid: true,
		speed : 2000,
		delay : 2000,
	}),
	data06 = unslider06.data('unslider');
	$('.unslider-arrow06').click(function() {
        var fn = this.className.split(' ')[1];
        data06[fn]();
    });
});

// 轮播图