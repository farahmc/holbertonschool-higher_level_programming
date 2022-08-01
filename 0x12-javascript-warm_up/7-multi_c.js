#!/usr/bin/node

const arg = parseInt(process.argv[2], 10);
let i = 0;

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
}

for (i; i < arg; i++) {
  console.log('C is fun');
}
