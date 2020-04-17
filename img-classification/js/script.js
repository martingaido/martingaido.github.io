/*  Image Classification using Ml5, P5 and MobileNet

    ML5 Project
    https://ml5js.org/

    P5.js Project
    https://p5js.org/
*/

'use strict';

const divLabel = document.getElementById('label');
const divConfidence = document.getElementById('confidence');

/* Initialize the Image Classifier method with MobileNet */
const classifier = ml5.imageClassifier('MobileNet', modelLoaded);

function modelLoaded() {
    console.log('Model loaded from MobileNet.');
}

/* Make a prediction based on the given image */
classifier.classify(document.getElementById('image'), (err, results) => {

    divLabel.innerHTML = `[0]: ${results[0].label}, [1]: ${results[1].label}, [2]: ${results[2].label}`;
    divConfidence.innerHTML = `[0]: ${results[0].confidence}`;
    
});