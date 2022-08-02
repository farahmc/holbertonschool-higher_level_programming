#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);

const map = list.map((element, index) => { return element * index; });
console.log(map);
