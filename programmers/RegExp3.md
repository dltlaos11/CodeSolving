# RegExp3

```js
// #1
/* 문자열에 + 붙이면 숫자 변환 */
// replace, replaceAll 함수의 2번째 인자에는 함수와 값이 들어갈 수 있음
// 함수
return +numbers.replace(
  /one|two|three|four|five|six|seven|eight|nine|zero/g,
  (v) => {
    return num[v];
  }
);
// 값
+numbers
  .replaceAll("one", "1")

  [
    // #2
    // JSON.toString():[1,2] !== toString([1,2]):1,2
    // some
    // [1,2,3,10,20].some(v => v>10);
    //some: 하나라도 만족하면
    // every
    (1, 2, 3, 10, 20)
  ].every((v) => v > 10);
//every: 모두 만족해야 함
return dic.some((v) => [...spell].sort().toString() == [...v].sort().toString())
  ? 1
  : 2;

// #3
// 생각의 전환이 필요한 문제들이 나올 것
// 로테이션해서 1차원 배열에서 회전하는 수를 찾는 것과
// 2차원 좌표 평면에서 좌표를 이동하는 것 모두 생각의 전환으로 풀기 가능
// ex how to make?
// 010     000
// 000 ->  010
// 000     000
// 보통의 생각
// 처음 1의 좌표를 구해서 순회를 돌면서 그다음 row값의 1로 값을 바꿔줌
// 처음 1의 좌표를 0으로 바꿈
// 생각의 전환
// 1차원 배열로 만들어서 010000000 -> 000010000
// 3칸 이후의 인덱스 값을 바꿔주기만 하면 된다. 더간편

// #4
// 문자, 숫자 정규식 /[1-9]/g
// match(/-?\d+(\.\d+)?/g) 정수, 실수 정규표현식
// '1 -1 1.2'.match(/-?\d+(\.\d+)?/g) -:문자, ?: 없 있, \d+: 숫자
// let i of arr[]
var answer = 0;
let result = [];
s = s.split(" ");
for (let i of s) {
  if (i === "Z") {
    result.pop();
  } else {
    result.push(+i);
  }
}
answer = result.reduce((acc, val) => (acc += val), 0);
return answer;

// #5
// 순서 뽑기
// 중복된 것도 index를 표현해야하는데 set으로 할 필요가 없었디.
// 깊은 복사 slice() -> indexOf()
let 총합 = score.map((v) => v[0] + v[1]);
let 정렬된배열 = 총합.slice().sort((a, b) => b - a);
return 총합.map((v) => 정렬된배열.indexOf(v) + 1);
```
