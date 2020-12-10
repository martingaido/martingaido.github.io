'use strict';

let clearButton;
let canvas;

function setup() {
	canvas = createCanvas(400, 400);
	clearButton = createButton('clear');
	clearButton.mousePressed(clearCanvas);
	background(255);
}

function clearCanvas() {
	background(255);
}

function draw() {
	if (mouseIsPressed) {
		strokeWeight(8);
		line(mouseX, mouseY, pmouseX, pmouseY);
	}
}
