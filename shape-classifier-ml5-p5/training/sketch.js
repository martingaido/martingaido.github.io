'use strict';

let circles = [];
let squares = [];
let triangles = [];

function preload() {

    for (let i = 0; i < 500; i++) {
        
        let index = nf(i + 1, 4, 0);
        circles[i] = loadImage(`../data/circle${index}.png`);
        squares[i] = loadImage(`../data/square${index}.png`);
        triangles[i] = loadImage(`../data/triangle${index}.png`);
    }
}

let shapeClassifier;

function setup() {

    createCanvas(400, 400);
    //background(0);
    //image(squares[0], 0, 0, width, height);

    let options = {
        inputs : [64, 64, 4],
        task   : 'imageClassification',
        debug  : true
    };

    shapeClassifier = ml5.neuralNetwork(options);

    for (let i = 0; i < circles.length; i++) {
        shapeClassifier.addData({ image: circles[i] }, { label: 'Circle' });
        shapeClassifier.addData({ image: squares[i] }, { label: 'Square' });
        shapeClassifier.addData({ image: triangles[i] }, { label: 'Triangle' });
    }

    shapeClassifier.normalizeData();
    shapeClassifier.train({ epochs: 50 }, finishedTraining);
}

function finishedTraining() {
    console.log('Finished Training!');
    shapeClassifier.save();
}