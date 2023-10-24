#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  if (response && response.statusCode === 200) {
    const filmsData = JSON.parse(body).results;
    let wedgeAntillesFilms = 0;

    filmsData.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        wedgeAntillesFilms++;
      }
    });

    console.log(wedgeAntillesFilms);

  const films = JSON.parse(body).results;
  const count = films.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;

  console.log(count);
});
