function promisify<T>(callback: (...args: any[], cb: (error: any, value: T) => void) => void): (...args: any[]) => Promise<T> {
  return function (...args: any[]): Promise<T> {
    return new Promise((resolve, reject) => {
      function handleErrorAndValue(error: any, value: T) {
        if (error == null) {
          resolve(value);
        } else {
          reject(error);
        }
      }

      callback.call(this, ...args, handleErrorAndValue);
    });
  }
}

export { promisify };

function adder(a: number, b: number, cb: (error: any, value: number) => void): void {
  cb(null, a + b);
}

const promisifiedAdder = promisify(adder);

// Use the promisified adder
promisifiedAdder(1, 2).then(result => {
  console.log(result); // Prints '3'
}).catch(error => {
  console.error(error);
});
