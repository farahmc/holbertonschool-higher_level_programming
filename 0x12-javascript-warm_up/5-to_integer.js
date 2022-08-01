#!/usr/bin/node

const arg = parseInt(process.argv[2], 10);

if (typeof arg === 'number' && isNaN(arg) !== true) {
  console.log('My number is: ' + arg);
} else {
  console.log('Not a number');
}
