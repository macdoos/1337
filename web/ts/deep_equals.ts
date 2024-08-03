function deepEquals(valueOne: any, valueTwo: any): boolean {
  if (typeof valueOne !== typeof valueTwo) return false;

  if (typeof valueOne !== 'object' || valueOne === null || valueTwo === null) {
    if (Number.isNaN(valueOne) && Number.isNaN(valueTwo)) return true;
    return valueOne === valueTwo;
  }

  if (valueOne === valueTwo) return true;

  if (Array.isArray(valueOne) && Array.isArray(valueTwo)) {
    if (valueOne.length !== valueTwo.length) return false;
    for (let i = 0; i < valueOne.length; i++) {
      if (!deepEquals(valueOne[i], valueTwo[i])) return false;
    }
    return true;
  }

  if (Array.isArray(valueOne) || Array.isArray(valueTwo)) return false;

  const valueOneKeys = Object.keys(valueOne);
  const valueTwoKeys = Object.keys(valueTwo);

  if (valueOneKeys.length !== valueTwoKeys.length) return false;

  for (const key of valueOneKeys) {
    if (!Object.prototype.hasOwnProperty.call(valueTwo, key)) return false;
    if (!deepEquals(valueOne[key], valueTwo[key])) return false;
  }

  return true;
}

// Do not edit the line below.
export { deepEquals };

// Test cases with console.log to see the output
console.log(deepEquals(1, 1)); // Expected: true
console.log(deepEquals(1, '1')); // Expected: false
console.log(deepEquals(null, null)); // Expected: true
console.log(deepEquals(null, undefined)); // Expected: false
console.log(deepEquals([], [])); // Expected: true
console.log(deepEquals({}, {})); // Expected: true
console.log(deepEquals([], {})); // Expected: false
