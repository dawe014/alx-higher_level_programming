#!/usr/bin/node

const {argv} = require('process');

let arr = [];
let i;
if(argv.length<=3){
    console.log(1);
}
else {
    for (i =0,j=2 ;i<=j-2,j<argv.length;i++,j++){

        arr[i] =parseInt(argv[j]);

    }
    arr.sort(function(a, b) {
        return a - b;
    });
    arr.reverse(function(a,b){
        return a-b;
    });
    console.log(arr[1]);
}