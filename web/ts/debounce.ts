type DebouncedFunction = (...args: any[]) => void;

function debounce(callback: (...args: any[]) => void, delay: number, immediate = false): DebouncedFunction {
  let timerId: NodeJS.Timeout | null;

  return function(this: any, ...args: any[]) {
    const context = this;
    if (timerId) {
      clearTimeout(timerId);
    }

    const shouldCallImmediately = !timerId && immediate;
    if (shouldCallImmediately) {
      callback.apply(context, args);
    }

    timerId = setTimeout(() => {
      if (!immediate) {
        callback.apply(context, args);
      }
      timerId = null;
    }, delay);
  };
}

// Do not edit the line below.
export { debounce };

const debounced: DebouncedFunction = debounce(console.log, 3000, true);
console.log(debounced);