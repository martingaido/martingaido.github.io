// scripts that will keep live in background, listening all the time

// debug background scripts in extensions
// it will open a new console

'use strict';

console.log('Background script running!');

chrome.browserAction.onClicked.addListener(buttonClicked);

function buttonClicked(tab) {

	// alert('Button Clicked');

	// show information about the current tab
	console.log(tab);

	// send a message to content script
	let msg = {
		txt: "hello message from background"
	};

	chrome.tabs.sendMessage(tab.id, msg);
}

