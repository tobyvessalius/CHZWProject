// JavaScript Document

  var obtn=document.getElementById('video');
  var ovideo=document.getElementById('video-btn');
  var oatn=document.getElementById('video-area');
  var oshut=document.getElementById('video-shut');
  var oshadow=document.getElementById('shadow');
  obtn.onclick=function () {
    ovideo.style.display='block';
    oshadow.style.display='block';
    oatn.innerHTML='<iframe width="560" height="315" src="https://www.youtube.com/embed/FB625fTHfa8" frameborder="0" allowfullscreen></iframe>';
  }
  oshut.onclick= function () {
    ovideo.style.display='none';
    oshadow.style.display='none';
  }
