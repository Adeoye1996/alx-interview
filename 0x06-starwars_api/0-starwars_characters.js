#!/usr/bin/env node
const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}/`;

function printMovieCharacters(url) {
  request(url, async (error, response, body) => {
    if (error) {
      console.log('An error occurred');
      return;
    }

    const characters = JSON.parse(body).characters;
    if (!characters) return;

    const promises = characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.log('Error fetching character');
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });

    try {
      const characterNames = await Promise.all(promises);
      characterNames.forEach((name) => console.log(name));
    } catch (error) {
      console.log('Error handling promises');
    }
  });
}

printMovieCharacters(url);
