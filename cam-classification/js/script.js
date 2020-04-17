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
let video;

const divLabel = document.getElementById('label');
const divConfidence = document.getElementById('confidence');

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

function setup() {
    createCanvas(640, 480);
    video = createCapture(VIDEO);
    video.hide();
    background(0);
    mobilenet = ml5.imageClassifier('MobileNet', video, modelReady);
}

function draw() {
    image(video, 0, 0);
}