#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  if (error) {
    console.log(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
