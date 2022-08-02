#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};

for (const [key, value] of Object.entries(dict)) {
  if (newDict[dict[key]] === undefined) {
    Object.assign(newDict, { [value]: [key] });
  } else {
    newDict[dict[key]].push(key);
  }
}

console.log(newDict);
