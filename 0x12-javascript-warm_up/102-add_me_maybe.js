#!/usr/bin/node

const { add } = require("./13-add")

function addMeMaybe(number, theFunction){
    theFunction(number+1)

}

module.exports.addMeMaybe = addMeMaybe