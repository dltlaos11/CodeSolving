## k진수에서 소수 개수 구하기

2022 KAKAO BLIND RECRUITMENT

## 입출력 예제

n k result

437674 3 3

110011 10 2

## 내 풀이

```javascript
function isPrimeNum(number) {
  if (number <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.floor(Math.sqrt(number)); i++) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
}

function solution(n, k) {
  let answer = 0;
  let num = n.toString(k); // n을 k진수로 변환
  let numArr = num.split("0").map(Number); // 0을 기준으로 split

  for (let i = 0; i < numArr.length; i++) {
    if (isPrimeNum(numArr[i])) {
      answer++; // 해당 숫자가 소수면 answer++
    }
  }

  return answer;
}
```
