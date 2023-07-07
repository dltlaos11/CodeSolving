# No More Undefined

```js
// const safelyGet = (obj, str) => {
//   let a = str.split('.');
//   // console.log(obj ? obj?.[a[0]] ? obj?.[a[0]] ? obj?.[a[0]]?.[a[1]] : obj?.[a[0]] :obj?.[a[0]] : obj?.[a[0]]);
//   console.log(obj[`${str}`])
// }
const safelyGet = (obj, path) => {
  let properties = path.split(".");

  let current = obj;
  for (const property of properties) {
    if (current == undefined) {
      return undefined;
    } else {
      current = current[property];
    }
  }

  return current;
};
/* repository가 undefined인 경우 */
const object1 = {
  repository: undefined,
};

// safelyGet(object1, 'repository.readme.extension')
// -> 반환 값: undefined
console.log(safelyGet(object1, "repository.readme.extension"));
// safelyGet(object1, 'repository.readme')
// -> 반환 값: undefined
console.log(safelyGet(object1, "repository.readme"));
// safelyGet(object1, 'repository')
// -> 반환 값: undefined
console.log(safelyGet(object1, "repository"));
console.log("--------------------------------------");
/* repository의 readme가 undefined인 경우 */
const object2 = {
  repository: {
    readme: undefined,
  },
};
console.log(safelyGet(object2, "repository.readme.extension"));
// -> 반환 값: undefined
console.log(safelyGet(object2, "repository.readme"));
// -> 반환 값: undefined
console.log(safelyGet(object2, "repository"));
// -> 반환 값: { readme: undefined }
console.log("--------------------------------------");

/** repository.readme 모두가 존재하는 경우 */
const object3 = {
  repository: {
    readme: {
      extension: "md",
      content: "금융을 쉽고 간편하게",
    },
  },
};
console.log(safelyGet(object3, "repository.readme.extension"));
// -> 반환 값: 'md'
console.log(safelyGet(object3, "repository.readme"));
// -> 반환 값: { extension: 'md' }
```
