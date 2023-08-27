const fs = require("fs");
const input = fs.readFileSync("./BOJ/input.txt").toString().trim().split("\n");

let n = Number(input[0]);
let x = Number(input[2]);
let Nums = input[1].split(" ").map(Number);

let cnt = 0;
for(let i of Nums){
    if(i == x) cnt +=1;
}

console.log(cnt);