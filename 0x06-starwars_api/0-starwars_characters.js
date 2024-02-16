#!/usr/bin/node

// Importing the 'request' module for making HTTP requests
const request = require('request');

// Constructing the URL for the Star Wars movie based on the provided Movie ID
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

// Making an HTTP request to fetch movie data
request(url, async function (error, response, body) {
  // Checking for errors in the request
  if (error) {
    return console.error('Error fetching movie data:', error);
  } else {
    // Parsing the JSON response to extract character URLs
    const characters = JSON.parse(body).characters;

    // Iterating through each character URL
    for (const characterUrl of characters) {
      try {
        // Making an asynchronous request to fetch individual character data
        const characterData = await new Promise((resolve, reject) => {
          request(characterUrl, (err, res, html) => {
            if (err) {
              reject(err);
            } else {
              resolve(JSON.parse(html));
            }
          });
        });

        // Extracting and printing the character name
        const characterName = characterData.name;
        console.log(characterName);
      } catch (error) {
        // Handling errors in fetching individual character data
        console.error(`Error fetching character data for ${characterUrl}: ${error}`);
      }
    }
  }
});
