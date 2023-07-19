# RegExp2

```js
// 1. shifh, unshift(앞에 삽입)
if (direction == "right") {
  numbers.unshift(numbers.pop());
} else {
  // numbers.push(numbers.shift());
  numbers = [...numbers.slice(1), numbers.shift()];
  // slice 시작과 끝
}
// 2. nullush
//널 병합 연산자 (??) 는 왼쪽 피연산자가 null 또는 undefined일 때
//오른쪽 피연산자를 반환하고, 그렇지 않으면 왼쪽 피연산자를 반환하는 논리 연산자

// return order.toString().match(/[369]/g).length ?? [];
// xxxx.length -> cannot read undefined or Null🔥

let val = order.toString().match(/[369]/g) ?? [];
return val.length;

// 3. 일반적인 Set과 js Set
const set = [...new Set(my_string.split(""))];

console.log(set.values().next().value);
// 파이선에서 Set은 순서 보장 ❌, js에서는 보장.
// 4. Json.stringify

// JavaScript에서 배열과 객체는 값을 비교하는게 아니라 객체의 주소를 비교하기 때문입니다.

return JSON.stringify(after.split("").sort()) ===
  JSON.stringify(before.split("").sort())
  ? 1
  : 0;

// 5. Infinity
function solution(array, n) {
  array.sort((a, b) => a - b);
  // 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 하기 위해 sort
  var answer = 0;
  let temp = Infinity;
  for (let val of array) {
    if (Math.abs(n - val) < temp) {
      // 처음이 Infinity라서 무조건 된다
      // 배열 min 값은 Spread
      temp = Math.abs(n - val);
      answer = val;
    }
  }
  return answer;
}

// 6. match, RegExp
function solution(s) {
  var answer = "";
  let set = {};
  for (let i = 0; i < s.length; i++) {
    set[s[i]] = 0;
  }
  for (let j = 0; j < s.length; j++) {
    set[s[j]] += 1;
  }
  // Set
  // Object.keys(), Object.values()
  return Object.keys(set)
    .filter((v) => set[v] === 1)
    .sort()
    .join("");
}
// match, RegExp
let a = "12312345";
a.match(/2/g);

let a = "123455";
[...a].filter((c) => a.split(c).length == 2);
// 개수가 1개인 것은 split했을 떄 2개가 나온다.

let b = "123455";
[...a].filter((c) => b.match(new RegExp(c, "g")).length == 1);
// 개수가 1개인 것은 split했을 떄 2개가 나온다.

function solution(my_str, n) {
  var answer = [];
  // for(let i =0; i<Math.ceil(my_str.length/n); i++){
  //     answer.push(my_str.substring(i*n,i*n+n))
  // }
  for (let i = 0; i < my_str.length; i += n) {
    answer.push(my_str.slice(i, i + n));
  }
  return answer;
}

// . 모든 문자, 1개부터 3개
let a = "abc1Addfggg4556b";
a.match(new RegExp(".{1,3}", "g"));

// 7. 중복제거
a.join("").split("1").length - 1;
```
