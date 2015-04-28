function WeLyon(){
	var self = this;

	self.setup = function(){
		google.maps.event.addDomListener(window, 'load', self.initializeMap);
	};

	self.initializeMap = function(){
			var markers = [];
		// var pins = [{type : 'velov',
		// 			lat : 45.7601676,
		// 			lng :  4.8328885 },
		// 			{ type : 'normal',
		// 			lat : 45.7436,
		// 			lng :  4.87011 }];
		var pins = [];
		var map; // object containing the map
		var cordinateLyon = new google.maps.LatLng(45.7601676, 4.8328885);

		// image de marker
		var imageVelov = './images/iconeVelov.png';
		var imageNormal = './images/marker.PNG';

		
			 var mapOptions = {
				zoom: 13,
				center: cordinateLyon
		    };
		    map = new google.maps.Map(document.getElementById('map'),
		    							mapOptions);

		    
		    //pins = doGet("/pins")

		    //pins.forEach(function(pin , index) {  	
		    //	addMarker(pin);
		    //});
		    // var x = 0;
		

		// function addMarker(aPin) {
		// 	// ToDo : gerer les différents types de marker
			
		// 	var type = aPin.type;
		// 	var image;
		// 	switch (type) { 
		// 		case "velov" : 
		// 			image = imageVelov;
		// 			break;
		// 		default :
		// 			image = imageNormal
		// 		}

		// 	var aMarker = new google.maps.Marker({
		// 		position: new google.maps.LatLng(aPin.lat, aPin.lng),
		// 		map: map,
		// 		icon: image
		// 	});
		// 	markers.push({pin : aPin,
		// 					marker : aMarker})
		// }
	};
}

var weLyon = new WeLyon();
weLyon.setup();
