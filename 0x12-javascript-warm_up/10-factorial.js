#!/usr/bin/node

const {argv} = require('process');

if(!parseInt(argv[2])){
    console.log(1);
}
else {
    console.log(factorial(parseInt(argv[2])));
}

function factorial(a){
    
    if(a<1){
        return 1;
    }
    else {
        return a*factorial(a-1);
}
}

