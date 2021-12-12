'use strict';

const childProc = require('child_process');
const CHILD_PROCESSES = 200;
const URL = 'https://www.sweeppea.com';

(async () => {

	let times = [];
	let children = [];

	for (let i = 0; i < CHILD_PROCESSES; i++) {
		let childProcess = childProc.spawn('node', ['child.js', `--url=${URL}`]);
		children.push(childProcess);
	}

	let responses = children.map(function wait(child) {
		return new Promise((res) => {

			child.stdout.on('data', (data) => {
				console.log(`child stdout: ${data}`);
				times.push(parseInt(data));
			});

			child.on('exit', (code) => {
				if(code === 0) {
					res(true);
				} else {
					res(false);
				}
			});
		});
	});

	responses = await Promise.all(responses);

	if(responses.filter(Boolean).length == responses.length) {
		const sum = times.reduce((a, b) => a + b, 0);
		const avg = (sum / times.length) || 0;
		console.log(`Average time: ${avg}ms`);
		console.log('(*) Success!');
	} else {
		console.log('(x) Failure!');
	}

})();
