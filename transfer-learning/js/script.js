/*  Transfer Learning from Webcam using Ml5, P5 and MobileNet

    ML5 Project
    https://ml5js.org/

    P5.js Project
    https://p5js.org/

*/

let mobilenet;
let video;
let classifier;

let firstObjButton;
let secondObjButton;
let trainButton;

const divLabel = document.getElementById('label');
const divConfidence = document.getElementById('confidence');

function modelReady() {
    console.log('Model is ready.');
}

function videoReady() {
    console.log('Video is ready.');
}

function whileTraining(loss) {
    if(loss === null) {
        console.log('Training complete!');
        classifier.classify(gotResults);
    } else {
        console.log(loss);
    }
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

    firstObjButton = createButton(' --- First Object --- ');
    firstObjButton.mousePressed(() => {
        classifier.addImage('First Object');
    });

    secondObjButton = createButton(' --- Second Object --- ');
    secondObjButton.mousePressed(() => {
        classifier.addImage('Second Object');
    });

    trainButton = createButton(' --- TRAIN MODEL --- ');
    trainButton.mousePressed(() => {
        classifier.train(whileTraining);
    });
}

function draw() {
    image(video, 0, 0);
}