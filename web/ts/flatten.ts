type Flattenable = string | number | boolean | null | FlattenableObject | FlattenableArray;
interface FlattenableObject {
  [key: string]: Flattenable;
}
interface FlattenableArray extends Array<Flattenable> {}

function flatten(value: Flattenable): Flattenable {
  if (typeof value !== 'object' || value === null) {
    return value;
  }

  if (Array.isArray(value)) {
    return value.reduce((acc: Flattenable[], curr: Flattenable) => acc.concat(flatten(curr)), []);
  }

  const flattened_obj: FlattenableObject = {};

  for (const [k, v] of Object.entries(value)) {
    const value_is_obj = typeof v === 'object' && v !== null && !Array.isArray(v);
    const flattened_value = flatten(v);

    if (value_is_obj) {
      Object.assign(flattened_obj, flattened_value);
    } else {
      flattened_obj[k] = flattened_value;
    }
  }

  return flattened_obj;
}

export { flatten };

const nestedObject = {
  a: 1,
  b: {
    c: 2,
    d: {
      e: 3,
      f: [4, 5, { g: 6 }]
    }
  }
};

const arr = [1, 2, [3, 4, [], 5]];

const flattenedObject = flatten(nestedObject);
const flattenedArray = flatten(arr);

console.log(flattenedObject);
console.log(flattenedArray);
