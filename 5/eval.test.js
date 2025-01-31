const { findSmallestInteger } = require("./solution");

describe("findSmallestInteger", () => {
  test("Should return -1 for single-digit input (n=1)", () => {
    const input = 1;
    const expectedOutput = -1;
    expect(findSmallestInteger(input)).toBe(expectedOutput);
  });

  test("Should return the smallest valid number for two-digit input (n=2)", () => {
    const input = 2;
    const expectedOutput = 66;
    expect(findSmallestInteger(input)).toBe(expectedOutput);
  });

  test("Should return -1 for three-digit input (n=3)", () => {
    const input = 3;
    const expectedOutput = -1;
    expect(findSmallestInteger(input)).toBe(expectedOutput);
  });

  test("Should return the smallest valid number for four-digit input (n=4)", () => {
    const input = 4;
    const expectedOutput = 3366;
    expect(findSmallestInteger(input)).toBe(expectedOutput);
  });

  test("Should return the smallest valid number for seven-digit input (n=7)", () => {
    const input = 7;
    const expectedOutput = 3336366;
    expect(findSmallestInteger(input)).toBe(expectedOutput);
  });

  test("Should return the smallest valid number for larger input (n=20)", () => {
    const input = 20;
    const expectedOutput = "33333333333333330000";
    expect(findSmallestInteger(input).toString()).toBe(expectedOutput);
  });
});
