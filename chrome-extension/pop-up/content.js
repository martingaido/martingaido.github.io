// https://developer.chrome.com/extensions/manifest

// remember to reload the extension on every change

// this will load after the complete page loads

// load unpacked as extension in chrome

'use strict';

console.log('Extension ready to go!');

let paragraphs = document.getElementsByTagName('p');

for(let a=0; a<paragraphs.length; a++) {
	paragraphs[a].style['background-color'] = '#000000';
}

// receive the message from background
chrome.runtime.onMessage.addListener(gotMessage);

function gotMessage(message, sender, sendResponse) {
	console.log(message.txt);

	// do some magic with this

	// go api, do anything with the dom
}
