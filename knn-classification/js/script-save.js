/*  KNN Classification

    Save model from JSON file.

    Interesting material to read:
    https://observablehq.com/@nsthorat/how-to-build-a-teachable-machine-with-tensorflow-js

    ML5 Project
    https://ml5js.org/

    P5.js Project
    https://p5js.org/

    ImageNet Repo
    http://www.image-net.org/
*/

let features;
let video;
let classifier;
let knn;
let ready = false;

const divLabel = document.getElementById('label');
const divConfidence = document.getElementById('confidence');

function modelReady() {
    console.log('Model is ready!');
}

function videoReady() {
    console.log('Video is ready!');
}

function setup() {

    createCanvas(640, 480);
    video = createCapture(VIDEO);
    video.hide();
    background(0);

    features = ml5.featureExtractor('MobileNet', modelReady);
    knn = ml5.KNNClassifier();
}

function goClassify() {
    
    const logits = features.infer(video);
    
    knn.classify(logits, function (error, result) {
        
        if(error) {

            console.error(error);
        
        } else {
        
            divLabel.innerHTML = `${result.label}`;
            goClassify();
        }
    });
}

function keyPressed() {

    /* Digital fingerprints of the captured video frame or image */
    const logits = features.infer(video);
    
    if(key == 'l') {
    
        knn.addExample(logits, 'left');
        console.log('left');
    
    } else if (key == 'r'){
    
        knn.addExample(logits, 'right');
        console.log('right');
    
    } else if (key == 'u') {
    
        knn.addExample(logits, 'up');
        console.log('up');
    
    } else if (key == 'd') {

        knn.addExample(logits, 'down');
        console.log('down');
    } else if (key == 's') {

        knn.save('model.json');
        console.log('Model Saved');
    }
}

function draw() {

    image(video, 0, 0);
    
    /* Horizontal Axis (x) */
    line(0, 240, 640, 240);
    strokeWeight(2);
    
    /* Vertical Axis (y) */
    line(320, 0, 320, 480);
    strokeWeight(2);

    stroke('rgb(0,255,0)');

    if(!ready && knn.getNumLabels() > 0) {
        goClassify();
        ready = true;
    }
}

