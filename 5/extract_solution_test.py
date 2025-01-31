import os
from extract_solution import extract_solution

llm_response = """
```javascript
/**
 * @param {number} n - The length of the decimal representation.
 * @returns {number} - The smallest integer that meets the criteria, or -1 if no such integer exists.
 */
function findSmallestInteger(n) {
  if (n < 3) {
    return -1;
  }

  let numString = "3".repeat(n);
  let num = parseInt(numString);

  while (numString.length === n) {
    if (num % 33 === 0 && num % 66 === 0) {
      return num;
    }

    numString = findNextNumber(numString);
    if (numString === null) {
      return -1;
    }
    num = parseInt(numString);
  }

  return -1;
}


function findNextNumber(numString) {
    let digits = numString.split("");
    for (let i = digits.length - 1; i >= 0; i--) {
        if (digits[i] === "3") {
            digits[i] = "6";
            return digits.join("");
        } else {
            digits[i] = "3";
        }
    }
    return null;
}
``` 

"""

try:
    response = extract_solution(llm_response=llm_response)

    if not isinstance(response, list):
        raise ValueError("Expected response to be a list of (file_name, code) tuples.")

    for item in response:

        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Invalid tuple.")

        file_name, code = item

        # Check if the file itself exists
        if not os.path.isfile(file_name):
            raise FileNotFoundError(
                f"The file '{file_name}' does not exist. Please check the path."
            )

        # Clear the file and write to the file
        with open(file_name, "w") as file:
            file.write(code)

        print(f"File '{file_name}' written successfully.")

except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")

