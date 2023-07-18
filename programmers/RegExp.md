# RegExp

```js
// 1. Array(n).fill().map((_, i) => i +1).filter(v=>v*2)
answer = Array(n)
  .fill()
  .map((_, i) => i + 1)
  .filter((v) => v % 2 == 0)
  .reduce((acc, val) => (acc += val), 0);

// 2. Array.from
// Array.from() 메서드는 유사 배열 객체(array-like object)나 반복 가능한
// 객체(iterable object)를 얕게 복사해 새로운Array 객체를 만듭니다.
Array.from([my_string], (x) => console.log(x + x));
return Array.from(my_string).reverse().join("");
console.log(Array.from("foo"));
// Expected output: Array ["f", "o", "o"]

console.log(Array.from([1, 2, 3], (x) => x + x));
// Expected output: Array [2, 4, 6]

// 3. repeat, replaceAll
".".repeat(10).split(".");
my_string.replaceAll(letter, "");

// 4. replace, new RegExp('B', 'g')
"BCVddbe12312456".replace(/[A-Z]/g, "");
// 'ddbe12312456'#
let a = new RegExp("B", "g");
"BCVddbe".replace(a, "");
// 'CVddbe'

// 5. Set
new Set([...s1, ...s2]).size;

// 6. Spread
console.log([...rsp].map((v) => a[v]).join(""));

// 7. getLCM
let getLCM = (num1, num2) => {
  let lcm = 1;

  while (!(lcm % num1 == 0 && lcm % num2 == 0)) {
    // if((lcm % num1 == 0) && (lcm % num2 == 0)){
    //   break;
    // }
    lcm++;
  }
  return lcm;
};
```
