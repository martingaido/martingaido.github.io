/*  Real time Object Detection using Webcam

    ML5 Project
    https://ml5js.org/

    P5.js Project
    https://p5js.org/

    ImageNet Repo
    http://www.image-net.org/
*/

let video;
let yolo;
let status;
let objects = [];
let canvas;

// const video = document.getElementById('video');
// const divLabel = document.getElementById('label');
// const divConfidence = document.getElementById('confidence');
const frontCam = document.getElementById('frontcam');
const rearCam = document.getElementById('rearcam');

// const divLabel = document.getElementById('label');
// const divConfidence = document.getElementById('confidence');

function setup(selectedMode) {

	const options = {
		video: {
			facingMode: {
				exact : selectedMode
			}
		}
	};

	canvas = createCanvas(windowWidth, windowHeight);
	// canvas.style('z-index','9999999');
	// canvas.position(100,100);
    video = createCapture(options);
    video.hide();
    background(0);

	// const stream = await navigator.mediaDevices.getUserMedia({
	// 	audio: false,
	// 	video: {
	// 		facingMode : selectedMode
	// 	}
	// });

	// video.srcObject = stream;

    /* Create a YOLO method */
    yolo = ml5.YOLO(video, startDetecting);

    /* Hide the original video */
    // video.hide();
    // status = select('#status');
}

function draw() {

    image(video, 0, 0, width, height);

    for (let i = 0; i < objects.length; i++) {

        noStroke();
        fill(0, 255, 0);
        text(objects[i].label, objects[i].x * width, objects[i].y * height - 5);
        noFill();
        strokeWeight(4);
        stroke(0, 255, 0);
        rect(objects[i].x * width, objects[i].y * height, objects[i].w * width, objects[i].h * height);
    }
}

function startDetecting() {
    console.log('Model is ready.');
    detect();
}

function detect() {
    yolo.detect(function(err, results) {
        objects = results;
        detect();
    });
}

frontCam.addEventListener('click', () => {
	video.remove();
	setup('user');
});

rearCam.addEventListener('click', () => {
	video.remove();
	setup('environment');
});
