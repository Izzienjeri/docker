/**
 * @param {number} n - The length of the decimal representation.
 * @returns {string} - The smallest integer that meets the criteria as a string, or '-1' if no such integer exists.
 */
function findSmallestInteger(n) {
  if (n < 2) return -1;

  // Calculate remainder for large numbers represented as strings
  function modulo(numStr, divisor) {
    let remainder = 0;
    for (let i = 0; i < numStr.length; i++) {
      remainder = (remainder * 10 + parseInt(numStr[i])) % divisor;
    }
    return remainder;
  }

  // Compare two string numbers of same length
  function compareStrings(str1, str2) {
    for (let i = 0; i < str1.length; i++) {
      if (str1[i] !== str2[i]) {
        return str1[i] < str2[i] ? -1 : 1;
      }
    }
    return 0;
  }

  let dp = new Array(66).fill(null);
  dp[0] = "";

  for (let i = 0; i < n; i++) {
    const newDp = new Array(66).fill(null);

    for (let rem = 0; rem < 66; rem++) {
      if (dp[rem] !== null) {
        // Try adding 3
        const str3 = dp[rem] + "3";
        const newRem3 = modulo(str3, 66);
        if (
          newDp[newRem3] === null ||
          compareStrings(str3, newDp[newRem3]) < 0
        ) {
          newDp[newRem3] = str3;
        }

        // Try adding 6
        const str6 = dp[rem] + "6";
        const newRem6 = modulo(str6, 66);
        if (
          newDp[newRem6] === null ||
          compareStrings(str6, newDp[newRem6]) < 0
        ) {
          newDp[newRem6] = str6;
        }
      }
    }
    dp = newDp;
  }

  // Verify the result
  if (dp[0] !== null && dp[0].length === n) {
    // Double check divisibility
    if (modulo(dp[0], 66) === 0) {
      return Number(dp[0]);
    }
  }
  return -1;
}

module.exports = { findSmallestInteger };
