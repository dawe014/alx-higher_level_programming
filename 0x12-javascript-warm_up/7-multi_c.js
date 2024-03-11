#!/usr/bin/node

const {argv} = require('process');

if(!parseInt(argv[2]) || parseInt(argv[2]) < 0){
    console.log("Missing number of occurrences")
}
else {
    let x = parseInt(argv[2]);
    for (let i = 0; i < x; i++){
        console.log("C is fun")
    }
}