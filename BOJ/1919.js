// 두 영어 단어가 철자의 순서를 뒤바꾸어 같아질 수 있을 때, 그러한 두 단어를 서로 애너그램 
// dared bread
// ared read
// 애너그램 관계에 있도록 만들기 위해서 제거해야 하는 최소 개수

// 입력
// 첫째줄과 둘 쨰줄에 영어단어 소문자

const fs = require("fs");
const input = fs.readFileSync("./BOJ/input.txt").toString().trim().split("\n");

let fir = input[0];
let sec = input[1];

const countAlphabets = (string) => {
    const counts = new Array(26).fill(0);
  
    string.split('').forEach((char) => {
      counts[char.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
    });
  
    return counts;
  };
  
  const arrayDifferenceCount = (arr1, arr2) => {
    let count = 0;
  
    arr1.forEach((value, index) => {
      count += Math.abs(value - arr2[index]);
    });
  
    return count;
  };
  
  const counts1 = countAlphabets(fir);
  const counts2 = countAlphabets(sec);
  
  console.log(arrayDifferenceCount(counts1, counts2));

//   'a'.charCodeAt(0), a의 유니코드 값 출력
// 입력 문자열을 하나씩 전체 알파벳 횟수를 기록하는 배열에 저장 
// 두 배열 간 값을 뺸다.
