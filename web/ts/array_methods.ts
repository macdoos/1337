interface Array<T> {
  myMap<U>(callback: (value: T, index: number, array: T[]) => U): U[];
  myFilter(callback: (value: T, index: number, array: T[]) => boolean): T[];
  myReduce<U>(callback: (accumulator: U, value: T, index: number, array: T[]) => U, initialValue?: U): U;
}

Array.prototype.myMap = function<T, U>(callback: (value: T, index: number, array: T[]) => U): U[] {
  const output: U[] = [];

  for (let i = 0; i < this.length; i++) {
    output.push(callback(this[i], i, this));
  }

  return output;
};

Array.prototype.myFilter = function<T>(callback: (value: T, index: number, array: T[]) => boolean): T[] {
  const output: T[] = [];

  for (let i = 0; i < this.length; i++) {
    if (callback(this[i], i, this) === true) {
      output.push(this[i]);
    }
  }

  return output;
};

Array.prototype.myReduce = function<T, U>(callback: (accumulator: U, value: T, index: number, array: T[]) => U, initialValue?: U): U {
  let acc: U;
  let startIndex: number = 0;

  // If initialValue is not provided, use the first element as the initial value
  if (initialValue === undefined) {
    acc = this[0] as unknown as U;
    startIndex = 1;
  } else {
    acc = initialValue;
  }

  for (let i = startIndex; i < this.length; i++) {
    acc = callback(acc, this[i], i, this);
  }

  return acc;
};

const arr = [1, 2, 3, 4, 5];

const mapped = arr.myMap((value, index) => value * 2);
const reduced = arr.myReduce((acc, value) => acc + value, 0);
const filtered = arr.myFilter(value => value % 2 === 0);

console.log(mapped); // [2, 4, 6, 8, 10]
console.log(reduced); // 15
console.log(filtered); // [2, 4]
