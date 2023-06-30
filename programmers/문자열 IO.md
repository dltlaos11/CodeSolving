# 문자열 I/O

```js
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", function (line) {
  console.log(line);
  input = [line];
}).on("close", function () {
  str = input[0];
});
```

## readline 모듈

### readline 모듈 불러오기

```js
const readline = require("readline");
```

- readline 모듈은 JS 내장 모듈로, 한 번에 한 줄씩 Readable 스트림(process.stdin)에서 데이터를 읽기위한 인터페이스를 제공

### 인터페이스 생성

```js
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
```

- 처음 생성시 `createInterface`를 통해 `input`, `output`을 설정

### 입출력을 처리하는 코드 작성하기

```js
rl.on("line", (line) => {
  /*입력받는 값을 처리하는 코드*/
  rl.close();
});

rl.on("close", () => {
  /*입력이 끝나고 실행할 코드*/
  process.exit();
});
```

on()메서드를 연결해서 작성 가능

```js
rl.on("line", (line) => {
  /*입력받는 값을 처리하는 코드*/
  rl.close();
}).on("close", () => {
  /*입력이 끝나고 실행할 코드*/
  process.exit();
});
```

### 공백을 포함한 한 줄이 입력되는 경우

`10 20 30`

```js
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", (line) => {
  input = line.split(" ").map((element) => parseInt(element));
  rl.close();
});

rl.on("close", () => {
  /*입력이 끝나고 실행할 코드*/
  process.exit();
});
```

### 여러 줄이 입력되는 경우

```
10 //한 줄
20 //한 줄
30 //한 줄
```

```js
const readline = require("readline");

const rl = readline.createInterface({
  input: stdin,
  output: stdout,
});

let input = [];

rl.on("line", (line) => {
  input.push(line);
  // input.push(parseInt(line));
  rl.close();
});

rl.on("close", () => {
  /*입력이 끝나고 실행할 코드*/
  process.exit();
});
```

## fs 모듈

### readFile()

```js
fs.readFile(filename, [options], callback);
```

filename의 파일을 [options]의 방식으로 읽은 후 callback으로 전달된 함수를 호출 (비동기적)

### readFileSync()

```js
fs.readFileSync(filename, [options]);
```

filename의 파일을 [options]의 방식으로 읽은 후 문자열을 반환(동기적)

- Sync가 붙은 것은 동기적 읽기, 붙지 않은 것은 비동기적 읽기
- 동기적 읽기로 읽게 되면 파일을 읽으면서 다른 작업을 동시 ❌
- 비동기적으로 읽으면 파일을 읽으면서 다른 작업도 동시에 수행할 수 있고,
  파일을 다 읽으면 매개변수 callback으로 전달한 함수가 호출

```js
var fs = require("fs");

// 문자 하나만 입력받을 경우
var input = fs.readFileSync("/dev/stdin").toString();

// 한칸 띄어쓰기로 구분
// input[0], input[1] 배열에서 꺼내쓰면 된다.
var input = fs.readFileSync("/dev/stdin").toString().split(" ");

// 줄바꿈으로 구분
var input = fs.readFileSync("/dev/stdin").toString().split("\n");

// 만약 인풋값이 숫자라면
var input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map(function (a) {
    return +a;
  });
```

- +a -> 문자열을 숫자로
