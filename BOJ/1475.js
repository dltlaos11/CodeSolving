// 한 세트 0~9숫자가 한개씩, 필요한 세트의 개수의 최솟값
// 6은 9를 뒤집어서 사용가능, 9는 6을 뒤집어서 사용가능
// 69: 2개이사일떄 1개 더하기
// 나머지: 2개 이상일떄 2개 더하기
const fs = require("fs");
const input = fs.readFileSync("./BOJ/input.txt").toString().trim().split("").map(el => +el);
// console.log(input);
const counts = new Array(10).fill(0);
input.forEach((e) => counts[e]++);
console.log(counts);
let cnt = 0;

for(let i = 0; i < counts.length; i++){
    if(counts[i] > 1){
        if(i == 6){
            cnt += Math.floor(counts[i]/2)
        }
        if(i == 9){
            cnt += Math.floor(counts[i]/2);
        }
        if(i != 6 & i!= 9) cnt += counts[i];
    }
}
console.log(cnt > 0 ? cnt : 1);
