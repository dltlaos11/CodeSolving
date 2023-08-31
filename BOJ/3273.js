// n개의 서로 다른 양의 정수로 이루어진 수열
// 각 수는 1 < a < 1000000의  범위

const fs = require("fs");
const input = fs.readFileSync("./BOJ/input.txt").toString().trim().split("\n");

let n = Number(input[0]);
let x = Number(input[2]);
let Nums = input[1].split(" ").map(Number);

Nums.sort((a, b) => a - b);

let cnt = 0;
let left = 0;
let right = n-1;

while(left != right) {
    if((Nums[left]+Nums[right]) == x){
        cnt +=1;
        left +=1
    }
    else if((Nums[left]+Nums[right]) > x) right -= 1;
    else left +=1
}
console.log(cnt);

// 연속된 주소 메모리 크기가 주어진다 -> 배열

// const path = './BOJ/input.txt' // 제출시 삭제 

// const readline = require('readline')
// const rl = readline.createInterface({
// 	// input: process.stdin, // 제출시 활성화  
// 	input: fs.createReadStream(path), // 제출시 삭제 
// 	output: process.stdout,
// })

// let input = []

// rl.on('line', function (line) {
// 	input.push(line)
// }).on('close', function () {
// let log = console.log;

// const size = input[0];
// const nums = input[1].split(" ").map(el => Number(el));
// const x = Number(input[2]);

// let result = [];

// const getCombination = (arrays, selectedNum) => {
//     let res = [];

//     if (selectedNum === 1) return arrays.map((el) => [el]);
  
//     arrays.forEach((fixed, index, origin) => {
//       let rest = origin.slice(index + 1);
//       let combinations = getCombination(rest, selectedNum - 1);
//       const attached = combinations.map((el) => [fixed, ...el]);
//       res.push(...attached);
//     });
//     return res;
//   };

// const MakeTwoSum = (size, nums, x) => {
//     getCombination(nums, 2).map((el) => {
//         if(el.reduce((acc,val) => acc+=val) === x){
//             result.push(el);
//         }
//     })

//     return result.length;
// }

// log(MakeTwoSum(size, nums, x));
//     process.exit()
// })

// 모든 순열의 조합을 구하고 진행하였을 떄 메모리 초과 문제 발생, 
// 투 포인터 활용