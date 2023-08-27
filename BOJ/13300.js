// 한 방에는 같은 학년의 학생들, 한 방에 한 명만 배정 가능
// 한방 최대 인원 수 : K, 조건에 맞게 모든 학생을 배정하기 위해 필요한 최소 방의 개수
// K = 2, 12개의 방, 3학년 남 방 2개, 4학년 여학생 방 X

// 입력
// 첫 쨰줄: N(수학여행 참가하는 학생수), M(한 방에 배정할 수 있는 최대 인원 수) 1<N,K<1000
// 다음 줄: S(학생의 성별(0:여 1:남)), Y(1<= x<=6, 학년)

// 출력
// 1:{0,0,1}
// 학년별 key: value 형태로 만들어 
// 학년별로 방을 구하는 방식
const fs = require("fs");
const input = fs.readFileSync("./BOJ/input.txt").toString().trim().split("\n");

let count = input[0].split(" ").map(el => +el);
let M = count[1];
let numbers = [];

for (let i = 1; i < input.length; i++) {
  if (input[i] !== '') {
    numbers.push(input[i].split(' ').map((el) => +el));
  }
} // 여러 줄 입력

let grade = {}
for(let i in numbers) {
    let key = numbers[i][1];
    let value = numbers[i][0];

    if (grade[key]) {
        grade[key].push(value);
    } else {
        grade[key] = [value];
    }
} // 학년별: 학생수

let res = 0;
for(let i in grade) {
    const cnt = new Array(2).fill(0);
    for(let j of grade[`${i}`]){
        if(j == 0) cnt[0]++;
        if(j == 1) cnt[1]++;
    }
    res += cnt.reduce((acc, val) => acc += Math.ceil(val/M), 0)
}
console.log(res);

// object에 값이 배열인 경우 
// for(let i in numbers) {
//     let key = numbers[i][1];
//     let value = numbers[i][0];

//     if (grade[key]) {
//         grade[key].push(value);
//     } else {
//         grade[key] = [value]; 없다면 배열을 넣어주고
//     }
// }

// obj에서의 for문 
// let i in grade 사용