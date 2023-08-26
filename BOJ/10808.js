const fs = require("fs");
const input = fs.readFileSync("./BOJ/input.txt").toString().trim().split("");

let str = "";
const alphabet = "abcdefghijklmnopqrstuvwxyz";
const counts = new Array(26).fill(0);

input.forEach((i) => counts[alphabet.indexOf(i)]++);

console.log(counts.join(" "));
