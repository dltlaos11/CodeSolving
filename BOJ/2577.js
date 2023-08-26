// a,b,c 곱한 결과에 0~9까지 숫자가 몇번 적혔는지
//  17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번
// 출력: 첫째 줄에는 0의 횟수,
const fs = require("fs");
const input = fs.readFileSync("./BOJ/input.txt").toString().split("\n").map((val) => +val);

let result = input.reduce((acc, e) => {
    return acc * e;
  }).toString().split("").map((val) => +val);

let counts = new Array(10).fill(0);

result.forEach((el) => {counts[el]++;});

counts.map((el) => console.log(el));

