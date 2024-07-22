class EventTarget {
  private listeners: { [key: string]: Set<() => void> };

  constructor() {
    this.listeners = {};
  }

  addEventListener(name: string, callback: () => void): void {
    if (!this.listeners.hasOwnProperty(name)) {
      this.listeners[name] = new Set([callback]);
    } else {
      this.listeners[name].add(callback);
    }
  }

  removeEventListener(name: string, callback: () => void): void {
    if (this.listeners.hasOwnProperty(name)) {
      this.listeners[name].delete(callback);
      if (this.listeners[name].size === 0) {
        delete this.listeners[name];
      }
    }
  }

  dispatchEvent(name: string): void {
    this.listeners[name]?.forEach(callback => {
      callback();
    });
  }
}

export { EventTarget };


const target = new EventTarget();
const logHello = () => console.log('Hello');
const logWorld = () => console.log('World');

target.addEventListener('hello', logHello);
target.addEventListener('world', logWorld);

target.dispatchEvent('hello'); // Prints 'Hello'
target.dispatchEvent('world'); // Prints 'World'

target.removeEventListener('hello', logHello);

target.dispatchEvent('hello'); // Prints nothing
target.dispatchEvent('world'); // Prints 'World'