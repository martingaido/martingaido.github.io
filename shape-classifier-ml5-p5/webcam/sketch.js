'use strict';

let shapeClassifier;
let canvas;
let resultsDiv;
let inputImage;
let clearButton;
let video;

function setup() {
    
    canvas = createCanvas(400, 400);
    video = createCapture(VIDEO);
    video.size(64, 64);
    
    let options = {
        inputs : [64, 64, 4],
        task   : 'imageClassification'
    };
    
    shapeClassifier = ml5.neuralNetwork(options);
    
    const modelDetails = {
        model    : 'model/model.json',
        metadata : 'model/model_meta.json',
        weights  : 'model/model.weights.bin'
    };

    background(255);
    resultsDiv = createDiv('loading model');
    inputImage = createGraphics(64, 64);
    shapeClassifier.load(modelDetails, modelLoaded);
}

function modelLoaded() {
    console.log('Model Ready!');
    classifyImage();
}

function classifyImage() {

    shapeClassifier.classify(
    {
        image: video
    }, gotResults);
}

function gotResults(err, results) {
    
    if (err) {
        console.error(err);
        return;
    }
    
    let label = results[0].label;
    let confidence = nf(100 * results[0].confidence, 2, 0);

    if(confidence > 90) {
        resultsDiv.html(`${label} ${confidence}%`);
    }

    classifyImage();
}

function draw() {
    
    image(video, 0, 0, width, height);
    // if (mouseIsPressed) {
    //   strokeWeight(8);
    //   line(mouseX, mouseY, pmouseX, pmouseY);
    // }

    // stroke(0);
    // noFill();
    // strokeWeight(4);
    // rectMode(CENTER);
    // rect(width/2, height/2, 40);
}