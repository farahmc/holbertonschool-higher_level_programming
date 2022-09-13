#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];
const fs = require('fs');

axios
  .get(url)
  .then(res => {
    const content = res.data;
    fs.writeFile(process.argv[3], content, err => {
      if (err) {
        console.error(err);
      }
    });
  })
  .catch(error => {
    console.error(error);
  });
