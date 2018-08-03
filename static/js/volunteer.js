$(function(){
var interva1 = setInterval(increment1,40); 
var interva2 = setInterval(increment2,20); 
var interva3 = setInterval(increment3,10); 
var current1=0;
var current2=0;
var current3=0;
function increment1(){ 
  
if(current1<30){
	current1++;
	$('.percent-1').html(current1+'%'); 
}
$('.box_show').mouseover(function(){ 
clearInterval(interva1); 
})
$('.box_show').mouseout(function(){
interva1 = setInterval(increment1,100); 
}); 
}
 	
function increment2(){ 
  
if(current2<70){
	current2++;
	$('.percent-2').html(current2+'%'); 
}

}
function increment3(){ 
  
if(current3<100){
	current3++;
	$('.percent-3').html(current3+'%'); 
}

} 
$("#waiting_check").click(function(){
	$(".check_box").css("display","block");
	$(".check_background").css("display","block");
});
$(".returnToLast").click(function(){
	$(".check_box").css("display","none");
	$(".check_background").css("display","none");
});


});