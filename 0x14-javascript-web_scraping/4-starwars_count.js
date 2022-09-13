#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];
const wedge = 18;
let count = 0;

axios
  .get(url)
  .then(res => {
    const dict = res.data.results;
    for (const movies of dict) {
      for (const character of movies.characters) {
        if (character.includes(wedge)) {
          count++;
        }
      }
    }
    console.log(count);
  })
  .catch(error => {
    console.error(error);
  });
