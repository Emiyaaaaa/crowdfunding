var $arrowLeft,$arrowRight,$imgs,$points,num=0;//var声明变量
$(function(){
	$arrowLeft=$('.arrow-left');//获取要操作的元素
	$arrowRight=$('.arrow-right');
	$imgs=$('.images .item');
	$points=$('.poinetr-box li');
	
//右箭头点击事件
$arrowRight.click(function(e){
//	e.preventDefault();//阻止默认事件
	
	num++;
	if(num===3){
		num=0
	}
	changeNum(num);
	
})
$arrowLeft.click(function(e){
//	e.preventDefault();//阻止默认事件
	num--;
	if(num===-1){
		num=2
	}
	changeNum(num);
	
})
//指示器切换
$points.click(function() {
	num=$(this).index()//获取点击的索引值
	changeNum(num);
})
//定时器
var timer=setInterval(function() {
	num++;
	if(num===3){
		num=0
	}
	changeNum(num);
},3000)	//5s自动切换
//鼠标移入停止自动播放，鼠标移开自动播放
$('.banner').mouseenter(function(){
	clearInterval(timer)
	
})
$('.banner').mouseleave(function(){
	clearInterval(timer)
	timer=setInterval(function(){
	num++;
	if(num===3){
		num=0
	}
	changeNum(num);
},3000)	//5s自动切换
})
})
//封装函数
function changeNum(num) {
	$imgs.eq(num).fadeIn().siblings().hide();
	$points.eq(num).addClass('active').siblings().removeClass('active');//圆点样式的切换
	
}