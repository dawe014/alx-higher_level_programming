#!/usr/bin/node

const { argv } = require('process');

// print process.argv
argv.forEach((val, index) => {
  console.log(`${index}: ${val}`);
});
console.log(argv.length);