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

const video = document.getElementById('video');
const divLabel = document.getElementById('label');
const divConfidence = document.getElementById('confidence');
const frontCam = document.getElementById('frontcam');
const rearCam = document.getElementById('rearcam');

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
    mobilenet = ml5.imageClassifier('MobileNet', video, modelReady);
}

frontCam.addEventListener('click', () => {
	setup('user');
});

rearCam.addEventListener('click', () => {
	setup('environment');
});
