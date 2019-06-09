fetch('guide_v.json')
.then(function(response) {
  if (!response.ok) {
	throw new Error("HTTP error, status = " + response.status);
  }
  return response.json();
})
.then(function(json) {
  var jsonStep = json.steps;
  for (var i in jsonStep) {
	  $(jsonStep[i]['selector']).attr('step_attr', jsonStep[i]['id']);
	  $(jsonStep[i]['selector']).click(function() {
		  popUpGuide($(this), jsonStep);
		});
  }
}).catch(function(error) {
  console.log(error.message);
});

function popUpGuide(target, json) {
	var limit = json.length;
	const idTarget = target.attr('step_attr');
	var nextElement = null;

	const curentPopUpOptions = findComponent(json, idTarget);
	if(curentPopUpOptions === null){
		throw new Error("  " + response.status);
	}
	const nextPopUpOptions = findComponent(json, curentPopUpOptions['next']);
	
	if(nextPopUpOptions !== null){
		nextElement = nextPopUpOptions['selector'];
	}
	// construct new popUp 
	const element = buildPopUpSection(curentPopUpOptions);
	buildPopUpSection(element);
	// close popUp button listener
	element.find( ".close-div" ).click(function(){
		element.remove();
	});
	
	// set up the next activ tip div
	element.find( ".next-div" ).click(function(){
		if (nextElement !== null){
			$( nextElement ).trigger( "click" );
			element.remove();
		}
	});
	
	// set new element position on page
	var position = target.position();
	var height = target.outerHeight();
	element.css({top: position.top+height, left: position.left, position:'absolute'});
	target.after(element);
}

function buildPopUpSection(curentPopUpOptions){
	var nextButton = curentPopUpOptions['next'] !== null? '<p style="width: 50%; float: right; border-radius:  0 0 10px;" class="button next-div" >next</p>' : "";
	var withButton = curentPopUpOptions['next'] !== null? "50%; border-radius: 0 0 0 10px;" : "100%; border-radius: 0 0 10px 10px;";
	const element = $('<section class="close-Tip"><p class="pop-up-text">'+curentPopUpOptions['content']+'</p><spam class="container-buttons"><p style="width: '+withButton+'  float: left;" class="button close-div">close</p>'+nextButton+'</spam></section>');
	const button = element.find(".button");
	
	// add the css for the popUp container
	element.find("p").css({
		"padding": "0px",
		"margin": "0px"
	});
	element.find(".pop-up-text").css({
		"padding": "10px"
	});	
	element.find(".container-buttons").css({
		"text-align": "center",
		"position": "relative"
	});
	button.css({
		"background-color": "cadetblue",
		"cursor": "pointer"
	});
	element.css({
	"background-color": "POWDERBLUE", 
	"border-radius": "10px", 
	});
	
	// set hover action on button
	button.mouseenter(function(event) {
		$(event.target).css({ "background-color": "cornflowerblue" });
	}).mouseleave(function() { 
		$(this).css({ "background-color": "cadetblue" });
	});
	
	return element;
}

function findComponent(json, IdToMatch){
	for (var i in json) {
		if (IdToMatch == json[i]['id']){
			return json[i];
		}
	}
	return null;
} 
