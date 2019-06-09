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
		  clearOpenElements();
		  popUpGuide($(this), jsonStep);
		});
  }
  createMainMenu(jsonStep);
  $('.right-menu-G').click(function(){
	  showGiudMenu($('.menu-guid'));
  });
}).catch(function(error) {
  console.log(error.message);
});

function clearOpenElements(){
	$('.close-Tip').remove(); // clear all others pop Up's open
} 

function createMainMenu(jsonStep){
	const section = $( "<section class='menu-guid' open-menu='close'></section>" );
	const tagContainerLeft = $( "<span class='left-menu-G'></span>" )
	const tagContainerRight = $( "<span class='right-menu-G'>Click Here</span>" )
	const tagHead = $( "<b> Click the number of step to start, or click one of page elements.</b>" )
	tagContainerLeft.append(tagHead);
	for (var i in jsonStep) {
		const step = $( "<p class='menu-tiem' jump-to='"+jsonStep[i]['selector']+"'>Click here to jump to step "+(parseInt(i)+1)+".</p>" );
		step.click(function(event) {
			clearOpenElements();
			const jumpElement = $(this).attr("jump-to");
		    $(jumpElement).trigger( "click" );
		});
		hoverEvent(step)
		tagContainerLeft.append(step);
	}
	section.append(tagContainerLeft);
	section.append(tagContainerRight);
	section.css({
		"width": "200px",
		"margin": "0px",
		"position": "absolute",
		"background": "lightskyblue",
		"left": "-160px",
		"top": "30%"
	});
	section.find('.left-menu-G').css({
		"width": "80%",
		"float": "left",
		"background": "lightskyblue"
	});
	section.find('.right-menu-G').css({
		"width": "15%",
		"padding-right": "5%",
		"float": "right",
		"cursor": "pointer",
		"background": "dodgerblue",
		"height": "230px",
		"writing-mode": "vertical-rl",
		"text-orientation": "upright",
		"text-align": "center"
	});
	$( "body" ).append( section );
}

function showGiudMenu(section){
	const openAttr = section.attr('open-menu');
	if (openAttr == 'close'){
		section.animate({ left: "+=160" });
		section.attr('open-menu', 'open');
	}else {
		section.animate({ left: "-=160" });
		section.attr('open-menu', 'close');
	}
} 

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

function hoverEvent(button){
	button.mouseenter(function(event) {
		$(event.target).css({ "background-color": "cornflowerblue" });
	}).mouseleave(function() { 
		$(this).css({ "background-color": "cadetblue" });
	});
	button.css({
		"background-color": "cadetblue",
		"cursor": "pointer"
	});
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
	element.css({
	"background-color": "POWDERBLUE", 
	"border-radius": "10px", 
	});
	
	// set hover action on button
	hoverEvent(button);
	
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