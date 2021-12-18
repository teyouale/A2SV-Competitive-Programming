"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", function (inputStdin) {
	inputString += inputStdin;
});

process.stdin.on("end", function () {
	inputString = inputString.split("\n");

	main();
});

function readLine() {
	return inputString[currentLine++];
}

/*
 * Complete the 'countSwaps' function below.
 *
 * The function accepts INTEGER_ARRAY a as parameter.
 */

function countSwaps(a) {
	// Write your code here
	var count = 0;
	for (var i = 0; i < a.length; i++) {
		for (var j = 0; j < i; j++) {
			// console.log(a[i]);
			// console.log(a[j]);
			if (a[i] < a[j]) {
				var temp = a[i];
				a[i] = a[j];
				a[j] = temp;
				count++;
			}
		}
	}
	// console.log(a)
	console.log("Array is sorted in " + count + " swaps.");
	console.log("First Element: " + a[0]);
	console.log("Last Element: " + a[a.length - 1]);
}

function main() {
	const n = parseInt(readLine().trim(), 10);

	const a = readLine()
		.replace(/\s+$/g, "")
		.split(" ")
		.map((aTemp) => parseInt(aTemp, 10));

	countSwaps(a);
}
