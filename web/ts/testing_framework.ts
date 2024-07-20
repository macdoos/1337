type TestFunction = () => void;

interface TestError {
  failedTestName: string;
  expectErrorMessage: string;
}

function describe(testSuiteName: string, func: TestFunction): void {
  console.log(`beginning test suite ${testSuiteName}`);

  try {
    func();
    console.log(`successfully completed test suite ${testSuiteName}`);
  } catch (error: any) {
    const { failedTestName, expectErrorMessage }: TestError = error;
    console.error(`failed running test suite ${testSuiteName} on test case ${failedTestName} with error message ${expectErrorMessage}`);
  }
}

function it(testCaseName: string, func: TestFunction): void {
  console.log(`beginning test case ${testCaseName}`);

  try {
    func();
    console.log(`successfully completed test case ${testCaseName}`);
  } catch (e: any) {
    throw {
      failedTestName: testCaseName,
      expectErrorMessage: e
    };
  }
}

function expect(actual: any) {
  return {
    toExist: () => throwIfFalse(actual != null, `expected value to exist but got ${JSON.stringify(actual)}`),
    toBe: (expected: any) => throwIfFalse(actual === expected, `expected ${JSON.stringify(actual)} to be ${JSON.stringify(expected)}`),
    toBeType: (type: string) => throwIfFalse(typeof actual === type, `expected ${JSON.stringify(actual)} to be of type ${type} but got ${typeof actual}`)
  };
}

function throwIfFalse(value: boolean, errorMessage: string): void {
  if (!value) {
    throw errorMessage;
  }
}

// Do not edit the lines below.
export { describe, it, expect };


describe('Passing test suite', () => {
  it('Passing test case 1', () => {
    expect('foo').toExist();
    expect(1 + 1).toBe(2);
  });

  it('Passing test case 2', () => {
    expect({}).toBeType('object');
  });
});


describe('Failing test suite', () => {
  it('Passing test case', () => {
    expect(0).toBe(0);
  });

  it('Failing test case 1', () => {
    expect(true).toBe(true);
    expect(true).toBe(false);
  });

  it('Unreachable test case', () => {
    expect('foo').toBe('bar');
  });
});