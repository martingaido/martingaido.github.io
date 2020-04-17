const toxicity = require('@tensorflow-models/toxicity');

// https://medium.com/tensorflow/text-classification-using-tensorflow-js-an-example-of-detecting-offensive-language-in-browser-e2b94e3565ce

// The minimum prediction confidence.
const threshold = 0.88;

// Load the model. Users optionally pass in a threshold and an array of
// labels to include.
toxicity.load(threshold).then(model => {
    const sentences = ["Every state is different when it comes to sweepstakes rules and regulations. I want to fuck you like an animal"];

    model.classify(sentences).then(predictions => {
        // `predictions` is an array of objects, one for each prediction head,
        // that contains the raw probabilities for each input along with the
        // final prediction in `match` (either `true` or `false`).
        // If neither prediction exceeds the threshold, `match` is `null`.

        // console.log(predictions);

        predictions.forEach((item) => {
            console.log('Label: ', item.label);
            console.log('Match: ', item.results[0].match);
        })
        /*
        prints:
        {
        "label": "identity_attack",
        "results": [{
            "probabilities": [0.9659664034843445, 0.03403361141681671],
            "match": false
        }]
        },
        {
        "label": "insult",
        "results": [{
            "probabilities": [0.08124706149101257, 0.9187529683113098],
            "match": true
        }]
        },
        ...
        */
    });
});