#!/usr/bin/node

const fs = require('fs');

const path = process.argv[2];

fs.readeFile(path, 'utf-8', (error, data) => {
    if (error) {
        console.log(error);
        return;
    }
    console.log(data);

})