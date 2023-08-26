// n개의 서로 다른 양의 정수로 이루어진 수열
// 각 수는 1 < a < 1000000의  범위
const fs = require("fs");
const input = fs.readFileSync("./BOJ/input.txt").toString().trim().split("\n");

let log = console.log;

const size = input[0];
const nums = input[1].split(" ").map(el => Number(el));
const x = Number(input[2]);

let result = [];

const getCombination = (arrays, selectedNum) => {
    let res = [];

    if (selectedNum === 1) return arrays.map((el) => [el]);
  
    arrays.forEach((fixed, index, origin) => {
      let rest = origin.slice(index + 1);
      let combinations = getCombination(rest, selectedNum - 1);
      const attached = combinations.map((el) => [fixed, ...el]);
      res.push(...attached);
    });
    return res;
  };

const MakeTwoSum = (size, nums, x) => {
    getCombination(nums, 2).map((el) => {
        if(el.reduce((acc,val) => acc+=val) === x){
            result.push(el);
        }
    })

    return result.length;
}

log(MakeTwoSum(size, nums, x));