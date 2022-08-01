#!/usr/bin/node

const arg = parseInt(process.argv[2], 10);
const x = 'x';

if (isNaN(arg)) {
  console.log('Missing size');
} else {
    let i = 0;
    for (i; i < arg; i++) {
	console.log(x.repeat(arg));
    }
}
