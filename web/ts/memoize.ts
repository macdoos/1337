type Resolver = (...args: any[]) => string;
type Callback = (...args: any[]) => any;

function memoize(callback: Callback, resolver?: Resolver) {
  const cache = new Map<string, any>();

  function getCacheKey(args: any[]): string {
    return resolver != null ? resolver(...args) : JSON.stringify(args);
  }

  const memoized = function (...args: any[]) {
    const cacheKey = getCacheKey(args);

    if (cache.has(cacheKey)) {
      return cache.get(cacheKey);
    }

    const output = callback(...args);
    cache.set(cacheKey, output);
    return output;
  };

  memoized.clear = function () {
    cache.clear();
  };

  memoized.delete = function (...args: any[]) {
    const cacheKey = getCacheKey(args);
    cache.delete(cacheKey);
  };

  memoized.has = function (...args: any[]) {
    const cacheKey = getCacheKey(args);
    return cache.has(cacheKey);
  };

  return memoized;
}

// Do not edit the line below.
export { memoize };


const callback = (...args: any[]) => args.join(', ');
const memoized = memoize(callback);
console.log(memoized(123)); 
console.log(memoized(123));
console.log(memoized(123, 'abc')); 

const memoized2 = memoize(callback, args => args[0]);
console.log(memoized2(123)); 
console.log(memoized2(123));
console.log(memoized2(123, 'abc')); 
console.log(memoized2('abc', 123)); 
console.log(memoized2('abc')); 
