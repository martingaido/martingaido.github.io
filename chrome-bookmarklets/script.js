'use strict';

(function() {

	console.log('Starting Bookmarklet...');

	let paragraphs = document.getElementsByTagName('p');

	for(let i=0; i<=paragraphs.length; i++) {
		paragraphs[i].innerHTML = "testing change paragraphs...";
	}

})();
