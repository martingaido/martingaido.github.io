/*  Load custom MODEL from JSON using Ml5, P5 and MobileNet

    ML5 Project
    https://ml5js.org/

    P5.js Project
    https://p5js.org/
*/

let mobilenet;
let video;
let classifier;

let loadModel;

const divLabel = document.getElementById('label');
const divConfidence = document.getElementById('confidence');

function modelReady() {
    console.log('Model is ready.');
    classifier.load('models/model.json', customModelReady);
}

function customModelReady() {
    console.log('Custom model is ready.');    
}

function videoReady() {
    console.log('Video is ready.');
    classifier.classify(gotResults);
}

function gotResults(error, results) {

    if(error) {

        console.error(error);

    } else {

        divLabel.innerHTML = `${results[0].label}`;
        divConfidence.innerHTML = `${results[0].confidence}`;

        /* Classify Again */
        mobilenet.classify(gotResults);
    }
}

function setup() {

    createCanvas(640, 480);
    video = createCapture(VIDEO);
    video.hide();
    background(0);

    mobilenet = ml5.featureExtractor('MobileNet', modelReady);
    classifier = mobilenet.classification(video, videoReady);
}

function draw() {
    image(video, 0, 0);
}