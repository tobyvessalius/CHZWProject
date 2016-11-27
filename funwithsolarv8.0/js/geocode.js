// JavaScript Document

var address = document.getElementById("address").value;
var geocoder = new google.maps.Geocoder();  
//alert(address);
function showAddress() { 
	var address2 = document.getElementById("address").value;
	//alert(1);
	 geocoder.geocode( 
    {'address' : address2}, function(results, status) { 
    	 
		 document.getElementById("1").innerHTML =results[0].geometry.location.lat()+","+results[0].geometry.location.lng();}
		 
    	 );
  }