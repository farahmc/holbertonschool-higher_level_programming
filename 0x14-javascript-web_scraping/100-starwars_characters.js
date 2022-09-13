#!/usr/bin/node

const axios = require('axios');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios
  .get(url)
  .then(res => {
    const dict = res.data.characters;
    for (const characterAPI of dict) {
      axios.get(characterAPI)
        .then(resCharacter => {
          console.log(resCharacter.data.name);
        });
    }
  })
  .catch(error => {
    console.error(error);
  });
