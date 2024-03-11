#!/usr/bin/node

const {argv} = require('process');

if(!parseInt(argv[2])){
    console.log("Missing size")
}

else {
    let n = parseInt(argv[2]);
    let i, j;
    
    for(i=0; i<n; i++){
        let str = ""
        for(j=0;j<n;j++){
            str += "X";
            // console.log("X"+" ");
        }
        console.log(str);
    }
}