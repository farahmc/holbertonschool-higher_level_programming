#!/usr/bin/node

function factorial (a) {
  if (a > 0) {
    return a * factorial(a - 1);
  } else { return 1; }
}

const arg = parseInt(process.argv[2], 10);
console.log(factorial(arg));
