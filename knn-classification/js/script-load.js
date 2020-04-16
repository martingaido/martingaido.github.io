/*  KNN Classification

    Load model from JSON file.

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
let loadModel;
let position;

let x, y;

const divLabel = document.getElementById('label');
const divConfidence = document.getElementById('confidence');

function modelReady() {
    console.log('MobileNet loaded.');

    knn = ml5.KNNClassifier();
    knn.load('models/model.json', () => {
        console.log('KNN Custom model loaded.');
        goClassify();
    });
}

function videoReady() {
    console.log('Video is ready!');
}

function setup() {
    createCanvas(640, 480);
    video = createCapture(VIDEO);
    // video.size(640, 480);
    // video.style("transform", "scale(-1,1)")
    video.hide();
    background(0);

    x = width / 2;
    y = height / 2;

    features = ml5.featureExtractor('MobileNet', () => {

        loadModel = createButton('--- LOAD MODEL ---');
        loadModel.mousePressed(() => {
            modelReady();
        });
    });  
}

function goClassify() {
    const logits = features.infer(video);
    knn.classify(logits, function (error, result) {
        
        if(error) {
        
            console.error(error);
        
        } else {

            position = result.label;
            divLabel.innerHTML = `Label: ${result.label} // X: ${x}, Y: ${y}`;
            goClassify();
        }
    });
}

// train with left and right keys
// function keyPressed() {
//     // digita fingerprints of the captured video frame or image
//     const logits = features.infer(video);
    
//     if(key == 'l') {
    
//         knn.addExample(logits, 'left');
//         console.log('left');
    
//     } else if (key == 'r'){
    
//         knn.addExample(logits, 'right');
//         console.log('right');
    
//     } else if (key == 'u') {
    
//         knn.addExample(logits, 'up');
//         console.log('up');
    
//     } else if (key == 'd') {

//         knn.addExample(logits, 'down');
//         console.log('down');
//     } else if (key == 's') {

//         knn.save('model.json');
//         console.log('Model Saved');
//     }

//     //console.log(logits);
// }

function draw() {

    image(video, 0, 0);
    
    // horizontal axis
    line(0, 240, 640, 240);
    strokeWeight(2);
    
    // vertical axis
    line(320, 0, 320, 480);
    strokeWeight(2);

    // line colors
    stroke('rgb(0,255,0)');

    if(position == 0) {
        x-=2;
    } else if (position == 1) {
        x+=2;
    } else if (position == 2) {
        y-=2;
    } else if (position == 3) {
        y+=2;
    }

    // draw elipsis
    ellipse(x, y, 20);
    fill(255);
}