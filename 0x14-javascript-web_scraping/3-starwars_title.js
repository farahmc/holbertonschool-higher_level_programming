#!/usr/bin/node

const axios = require('axios');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios
  .get(url)
  .then(res => {
    console.log(res.data.title);
  })
  .catch(error => {
    console.error(error);
  });
