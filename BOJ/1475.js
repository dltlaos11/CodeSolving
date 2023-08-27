// 한 세트 0~9숫자가 한개씩, 필요한 세트의 개수의 최솟값
// 6은 9를 뒤집어서 사용가능, 9는 6을 뒤집어서 사용가능
// 69: 2개이사일떄 1개 더하기
// 나머지: 2개 이상일떄 2개 더하기
const fs = require("fs");
const input = fs.readFileSync("./BOJ/input.txt").toString().trim().split("").map(el => +el);

const counts = new Array(10).fill(0);
// input.forEach((e) => counts[e]++);

for(let n of input){
    if(n === 6){
        if(counts[n] > counts[9]) counts[9]++;
        else counts[n]++;
    } else if(n === 9) {
        if(counts[n] > counts[6]) counts[6]++;
        else counts[n]++;
    } else counts[n]++;
}
let result = 0;
for (let c of counts) result = Math.max(result, c);
console.log(result);

// console.log(counts);
// let cnt = 0;

// for(let i = 0; i < counts.length; i++){
//     if(counts[i] > 1){
//         if(i == 6){
//             cnt += Math.floor(counts[i]/2)
//         }
//         if(i == 9){
//             cnt += Math.floor(counts[i]/2);
//         }
//         if(i != 6 & i!= 9) cnt += counts[i];
//     }
// }
// console.log(cnt > 0 ? cnt : 1);

// 이전 풀이는 11223344 ->  문제에서 세트라는 개념을 망각하고 푼 결과 8이라는 결과가 나오는 풀이
// 세트수를 고려하여 6이 하나 찼을 떄 6이 한번 더 들어온다면 9의 idx에 값 추가