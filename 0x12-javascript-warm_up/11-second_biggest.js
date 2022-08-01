#!/usr/bin/node

const numOfArgs = process.argv.length;
const args = process.argv;
let i = 2;
const newArray = [];

if (numOfArgs <= 3) {
  console.log('0');
} else {
  for (i; i < numOfArgs; i++) {
    newArray.push(args[i]);
  }
  newArray.sort(function (a, b) { return b - a; });
  console.log(newArray[1]);
}
