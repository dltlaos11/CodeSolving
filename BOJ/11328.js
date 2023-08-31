// strfry 함수는 입력된 문자열을 무작위로 재배열하여 새로운 문자열을 만듦
// 2번째 문자열이 1번째 문자열에 strfry 함수를 적용하여 얻어질 수 있는지 판단
// 영어 소문자들로만 이루어진 두 개의 문자열이 한 개의 공백으로 구분되어 주어진다. 각각의 문자열의 길이는 최대 1000

const fs = require("fs");
const input = fs.readFileSync("./BOJ/input.txt").toString().trim().split("\n");

let count = +input[0];
let numbers = [];
let answer = [];

for (let i = 1; i < input.length; i++) {
    if (input[i] !== '') {
      numbers.push(input[i].split(' ').map((el) => el));
    }
  } // 여러 줄 입력

  for(let i =0; i< count; i++){
    let check;
    let arr = numbers[i][0].split("").sort();
    let length = numbers[i][0].split("").length;
    let secParam = numbers[i][1].split("").sort();

    if(arr.length !== secParam.length){
        console.log("Impossible");
        continue;
    }
    for(let j = 0; j < length;j++){
        if(arr[j] != secParam[j]){
            check = false;
            break;
        }
        else check = true;
    }
    if(check) console.log("Possible");
    else console.log("Impossible");
  }
  // 정렬 후 처음 부터 비교
  // 길이가 다를 경우 예외처리
 // 애너그램(1919)과 동일 

//   answer.map((el) => console.log(el));

//   const getPermutations = (arrays, selectNum) => {
//     let res = [];
//     if (selectNum === 1) return arrays.map((el) => [el]);
  
//     arrays.forEach((fixed, index, origin) => {
//       let rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
//       let combinations = getPermutations(rest, selectNum - 1);
//       // res.push([fixed, ...combinations]);
//       const attached = combinations.map((el) => [fixed, ...el]);
//       res.push(...attached);
//     });
//     return res;
//   };


// for(let i =0; i< count; i++){
//     let check = 0;
//     let arr = numbers[i][0].split("");
//     let length = numbers[i][0].split("").length;
//     let secParam = numbers[i][1].split("");
//     getPermutations(arr, length).map(el => {
//         if(JSON.stringify(el) === JSON.stringify(secParam)){
//             answer.push("Possible");
//             check +=1;
//         }
//     });
//     if(check == 0) answer.push("Impossible")
// }
// answer.map((el) => console.log(el));
//  js 두 배열 간 메모리 주소를 비교 => JSON.stringify()


