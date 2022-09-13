#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];
const completed = {};
let user = '';

axios
  .get(url)
  .then(res => {
    for (const task of res.data) {
      user = task.userId;
      if (task.completed === true) {
        if (completed[user] !== undefined) {
          completed[user] += 1;
        } else {
          completed[user] = 1;
        }
      }
    }
    console.log(completed);
  })
  .catch(error => {
    console.error(error);
  });
