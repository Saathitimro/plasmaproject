

function displayButton(){
  var button = document.querySelector('#agreeButton');
  if( button.style.display == "block"){
    button.style.display = "none";
  }
  else{
    button.style.display = "block";
  }
}

// donor form display
function displayForm(){
  var screenObj = document.querySelector('#screen');
  var formObj = document.querySelector('#donorform-container');
  screenObj.style.display = 'flex';
  formObj.style.top = "-68px";
  formObj.style.opacity = "1";
}

// donor form close
function closeForm(){
  var screenObj= document.querySelector('#screen');
  screenObj.style.display = 'none';
}
// timeout for message notifications
function closeMessage(){
  var alertM = document.getElementsByClassName('alert');
  setTimeout(function(){
   for(i=0; alertM.length>0; i++){
    alertM[i].style.display = "none";
    alertM[i].style.transition = '0.2s ease-out';
   }
 }, 100); 
}

