/*  Save custom MODEL to JSON using Ml5, P5 and MobileNet

    ML5 Project
    https://ml5js.org/

    P5.js Project
    https://p5js.org/
*/

let mobilenet;
let video;
let classifier;

let happy;
let sad;
let neutral;
let saveButton;
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
        console.log('Training complete');
        classifier.classify(gotResults);
    } else console.log(loss);
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

    happy = createButton('Happy');
    happy.mousePressed(() => {
        classifier.addImage('Happy');
    });

    sad = createButton('Sad');
    sad.mousePressed(() => {
        classifier.addImage('Sad');
    });

    neutral = createButton('Neutral');
    neutral.mousePressed(() => {
        classifier.addImage('Neutral');
    });

    saveButton = createButton('--- SAVE ---');
    saveButton.mousePressed(() => {
        classifier.save();
    });

    trainButton = createButton('--- TRAIN ---');
    trainButton.mousePressed(() => {
        classifier.train(whileTraining);
    });
}

function draw() {
    image(video, 0, 0);
}