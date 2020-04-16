/*  Extractor Regression from Webcam using Ml5, P5 and MobileNet

    ML5 Project
    https://ml5js.org/

    P5.js Project
    https://p5js.org/

    How to use this script
    ----------------------

    1) Set the slider position
    2) Press "Record" to record slider position
    3) Repeat step 1 and 2 to construct the model
    4) Hit "Train Model" to complete
    5) Move objects horizontally
*/

let mobilenet;
let video;
let predictor;
let slider;
let record;
let value = 0;

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
        console.log('Training Complete');
        predictor.predict(gotResults);
    } else {
        console.log(loss);
    }
}

function gotResults(error, results) {

    if(error) {

        console.error(error);

    } else {        

        divLabel.innerHTML = `...`;
        divConfidence.innerHTML = `${results.value}`;
        value = results.value;
        predictor.predict(gotResults);
    }
}

async function setup() {

    createCanvas(640, 480);
    video = createCapture(VIDEO);
    video.hide();
    background(0);

    mobilenet = ml5.featureExtractor('MobileNet', modelReady);
    predictor = await mobilenet.regression(video, videoReady);

    slider = createSlider(0, 1, 0.5, 0.01);

    record = createButton('Record');
    record.mousePressed(() => {
        predictor.addImage(slider.value());
        console.log(slider.value());
    });

    trainButton = createButton(' TRAIN MODEL ');
    trainButton.mousePressed(() => {
        predictor.train(whileTraining);
    });
}

function draw() {    
    image(video, 0, 0);
    rectMode(CENTER);
    fill(255, 0, 200);
    rect(value*width, height/2, 50, 50);
}