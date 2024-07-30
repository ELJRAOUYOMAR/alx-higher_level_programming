#!/usr/bin/node

const request = require('request');
const path = 'https://swapi-api.alx-tools.com/api/films/'+ process.argv[2];

request(path, function (error, response, data) {
    data = JSON.parse(data);
    console.log(body.title);
});
