/*  Pose Estimation from Webcam using Ml5, P5 and PoseNet

    Model is loaded form MobileNet based on ImageNet repo.

    ML5 Project
    https://ml5js.org/

    P5.js Project
    https://p5js.org/

    Pose Estimation
    https://www.tensorflow.org/lite/models/pose_estimation/overview
*/

let video;
let poseNet;
let pose;
let skeleton;

const divLabel = document.getElementById('label');
const divConfidence = document.getElementById('confidence');

function setup() {
    createCanvas(640, 480);
    video = createCapture(VIDEO);
    video.hide();
    poseNet = ml5.poseNet(video, modelLoaded);
    poseNet.on('pose', gotPoses)
}

function gotPoses(poses){
    if(poses.length > 0) {
        pose = poses[0].pose;
        skeleton = poses[0].skeleton;
    }
}

function modelLoaded() {
    console.log('PoseNet is loaded');
}

function draw() {

    image(video, 0, 0);

    if(pose) {

        /* Nose */
        // fill(255, 0, 0);
        // ellipse(pose.nose.x, pose.nose.y, 15);

        /* Right Wrist */
        // fill(255, 0, 0);
        // ellipse(pose.rightWrist.x, pose.rightWrist.y, 15);

        /* Left Wrist */
        // fill(255, 0, 0);
        // ellipse(pose.leftWrist.x, pose.leftWrist.y, 15);

        for(let i = 0; i < pose.keypoints.length; i++){
            let x = pose.keypoints[i].position.x;
            let y = pose.keypoints[i].position.y;
            fill(0, 255, 0);
            ellipse(x, y, 10, 10);
        }

        for(let e = 0; e < skeleton.length; e++){
            let a = skeleton[e][0];
            let b = skeleton[e][1];
            strokeWeight(1);
            stroke(255);
            line(a.position.x, a.position.y, b.position.x, b.position.y);
        }
    }
}