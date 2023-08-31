// 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)
// L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
// 왼쪽 스택에서 pop을 해서 오른쪽 스택에 push한다. (왼쪽 스택이 비었을 경우 명령을 수행하지 않으면 된다.)
// D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
// 오른쪽 스택에서 pop을 해서 왼쪽 스택에 push한다. (오른쪽 스택이 비었을 경우 명령을 수행하지 않으면 된다.)
// B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
//      삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임 
// 왼쪽 스택에서 무조건 pop한다.
// (스택이 비어있다면 undefined를 pop하므로 별 다른 오류는 발생하지 않는다.오른쪽 스택은 건드리지 않으므로 상관이 없다.)
// P $	$라는 문자를 커서 왼쪽에 추가함
// 왼쪽 스택에 $ 문자를 push한다.

// 입력
// N 입력되어 있는 문자열
// 영어 소문자로만 이루어져 있으며, 길이는 100,000
// 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)
// 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로
const fs = require("fs");
const input = fs.readFileSync("./BOJ/input.txt").toString().trim().split("\n");

let lStack = input[0].split("");
let rStack = [];
let len = +(input[1]);

for (let i = 2; i < 2 + len; i++) {
  let [cmd, value] = input[i].split(" ");
  if (cmd === "L" && lStack.length) rStack.push(lStack.pop());
  if (cmd === "D" && rStack.length) lStack.push(rStack.pop());
  if (cmd === "B") lStack.pop();
  if (cmd === "P") lStack.push(value);
}

let answer = lStack.join("");
answer += rStack.reverse().join("");
console.log(answer);

// 두개의 리스트 커서는 고정, 왼쪽 배열의 오른쪽 끝과 오른쪽 배열의 왼쪽 끝
// abc 
// _ cba
// y cbax
// shift & unshift: O(N)
// push & pop : O(1)