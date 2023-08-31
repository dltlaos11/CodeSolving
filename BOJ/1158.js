// 1번부터 N
// 양의 정수 K(≤ N)
// 순서대로 K번째 사람을 제거
// 이 과정은 N명의 사람이 모두 제거될 때까지 계속
const fs = require("fs");
const [N, K] = fs.readFileSync("./BOJ/input.txt").toString().trim().split(" ").map(el => +el);

const arr = Array.from({ length: N }, (_, i) => i + 1);
const ans = [];
let cnt = 1;
while (arr.length) {

  let data = arr.shift();
  if (cnt % K == 0) {
    ans.push(data);
  } else {
    arr.push(data);
  }
  cnt++;
}

console.log(`<${ans.join(", ")}>`);

// 큐를 사용한 풀이
// 계속 
// M = 7, K = 3
// 1234567 
// [1, 2, 3, 4, 5, 6, 7]
// [2, 3, 4, 5, 6, 7, 1]
// [3, 4, 5, 6, 7, 1, 2]
// [ 4, 5, 6, 7, 1, 2 ] -> 3번째 idx % 3 === 0 삭제
// [ 5, 6, 7, 1, 2, 4 ]
// [ 6, 7, 1, 2, 4, 5 ] -> 6번째 idx % 3 === 0 삭제
// [ 7, 1, 2, 4, 5 ]
// [ 1, 2, 4, 5, 7 ]
