const axios = require('axios');

console.log('Hello, world!');

function quick() {
  console.log('quick ' + Date.now());
}

function fabunacci(n) {
  if (n <= 1) {
    return 1;
  } else {
    return fabunacci(n - 1) + fabunacci(n - 2);
  }
}

async function io() {
  try {
    await axios.get('https://macdoos.dev');
    console.log('io done ' + Date.now());
  } catch (error) {
    console.error('Error in io: ', error);
  }
}

const qeue = [];

for (let i = 0; i < 10; i++) {
  qeue.push(() => quick());
  qeue.push(async () => await io());
  qeue.push(() => fabunacci(40));
}

(async () => {
  const start = Date.now();
  // Run all tasks in parallel
  // await Promise.all(qeue.map((fn) => fn()));

  // Run all tasks sequentially
  for (let i = 0; i < qeue.length; i++) {
    await qeue[i]();
  }

  // Additional fabunacci call after the queue
  fabunacci(40);
  console.log('All done ', Date.now() - start);
})();

