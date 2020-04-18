/*  Image Classification from Webcam using Ml5, P5 and MobileNet

    Model is loaded form MobileNet based on ImageNet repo.

    ML5 Project
    https://ml5js.org/

    P5.js Project
    https://p5js.org/

    ImageNet Repo
    http://www.image-net.org/
*/

let mobilenet;
// let video;

const video = document.getElementById('video');
// const canvas = document.getElementById('canvas');
// const context = canvas.getContext('2d');

const divLabel = document.getElementById('label');
const divConfidence = document.getElementById('confidence');

const frontcam = document.getElementById('frontcam');
const rearcam = document.getElementById('rearcam');

function modelReady() {
    console.log('Model is ready.');
    mobilenet.predict(gotResults);
}

function gotResults(error, results) {

    if(error) {

        console.error(error);

    } else {

        divLabel.innerHTML = `${results[0].label}`;
        divConfidence.innerHTML = `${results[0].confidence}`;

        /* Predict Again */
        mobilenet.predict(gotResults);
    }
}

async function setup(selectedMode) {

    const stream = await navigator.mediaDevices.getUserMedia({
		audio: false,
		video: {
			facingMode : selectedMode
		}
	});

	video.srcObject = stream;

    //createCanvas(300, 300);
    //video = createCapture(VIDEO);
    //video.hide();
    //background(0);
    mobilenet = ml5.imageClassifier('MobileNet', video, modelReady);
}

frontcam.addEventListener('click', () => {
	setup('user');
});

rearcam.addEventListener('click', () => {
	setup('environment');
})
// function draw() {
//     image(stream, 0, 0);
// }
