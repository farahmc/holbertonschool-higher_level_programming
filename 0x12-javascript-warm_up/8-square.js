#!/usr/bin/node

const arg = parseInt(process.argv[2], 10);
const x = 'x';
let i = 0;

if (isNaN(arg)) {
  console.log('Missing size');
}

for (i; i < arg; i++) {
  console.log(x.repeat(arg));
}
