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
	  console.log(i);
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

	var components = findComponent(json, idTarget);
	const optionJson = components[0];
	const x = components[1];

	const j = parseInt(x)+1;
	if (limit > j){
		nextElement = json[j]['selector'];
	}
	const element = $('<section class="close-Tip" style="background: red" >'+optionJson['content']+'<p class="close-div">close</p>  <p class="next-div" >apasa pe next</p></div>');
	
	// close popUp button listener
	element.find( ".close-div" ).click(function(){
		element.remove();
	});
	
	// set up the next activ tip div
	element.find( ".next-div" ).click(function(){
		if (nextElement !== null){
			console.log(nextElement);
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

function findComponent(json, IdToMatch){
	for (var i in json) {
		if (IdToMatch == json[i]['id']){
			return [json[i], i];
		}
	}
} 

