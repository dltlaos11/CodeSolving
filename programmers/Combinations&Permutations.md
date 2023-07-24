# Combinations & Permutations

```js
// 조합
/*
const getCombinations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]);
    // n개중에서 1개 선택할 때(nC1), 바로 모든 배열의 원소 return

    arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1);
      // 해당하는 fixed를 제외한 나머지 뒤
      const combinations = getCombinations(rest, selectNumber - 1);
      // 나머지에 대해서 조합을 구한다.
      const attached = combinations.map((el) => [fixed, ...el]);
      //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
      results.push(...attached);
      // 배열 spread syntax 로 모두다 push
    });

    return results; // 결과 담긴 results return
}
 */

const getCombination = (arrays, selectedNum) => {
  let res = [];
  // if(arrays === 1) return res.map((el) => el); res❌ => arrays
  if (selectedNum === 1) return arrays.map((el) => [el]);

  // let arr  = arrays.forEach((fixed, index, origin) => {
  arrays.forEach((fixed, index, origin) => {
    let rest = origin.slice(index + 1);
    let combinations = getCombination(rest, selectedNum - 1);
    // res.push([fixed, ...combinations]);
    const attached = combinations.map((el) => [fixed, ...el]);
    res.push(...attached);
  });
  return res;
};
/*
const getPermutations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]);
    // n개중에서 1개 선택할 때(nP1), 바로 모든 배열의 원소 return. 1개선택이므로 순서가 의미없음.

    arr.forEach((fixed, index, origin) => {
      const rest = [...origin.slice(0, index), ...origin.slice(index+1)]
      // 해당하는 fixed를 제외한 나머지 배열
      const permutations = getPermutations(rest, selectNumber - 1);
      // 나머지에 대해서 순열을 구한다.
      const attached = permutations.map((el) => [fixed, ...el]);
      //  돌아온 순열에 떼 놓은(fixed) 값 붙이기
      results.push(...attached);
      // 배열 spread syntax 로 모두다 push
    });

    return results; // 결과 담긴 results return
}
*/
const getPermutations = (arrays, selectNum) => {
  let res = [];
  if (selectNum === 1) return arrays.map((el) => [el]);

  arrays.forEach((fixed, index, origin) => {
    let rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    let combinations = getPermutations(rest, selectNum - 1);
    // res.push([fixed, ...combinations]);
    const attached = combinations.map((el) => [fixed, ...el]);
    res.push(...attached);
  });
  return res;
};
```
