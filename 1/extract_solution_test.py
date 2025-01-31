import os
from extract_solution import extract_solution

llm_response = '''
The `resetForm` function was being called within the `onClose` callback of the `toast.success` function. This means the form would only be reset after the toast notification automatically closed after 1 second.  To reset the form immediately after a successful submission, call `resetForm` directly within the `if` block, before displaying the success toast.

Here's the corrected `handleFormSubmit` function:

```javascript
const f = (values, { resetForm }) => {
  console.log(values);
  values.ipd_enrollment_id = id; // Assume id is defined
  axios
    .post("/api/doctor/ipd_enrollement_bill_items/create", values, headers) // Assume headers is defined
    .then((response) => {
      console.log(response.data);
      const message = response.data.message;
      if (response.data.status) {
        resetForm(); // Reset the form immediately
        toast.success(message, {
          autoClose: 1000,
        });
      } else {
        toast.error(message, {
          autoClose: 2000,
        });
      }
    })
    .catch((error) => {
      console.log(error);
    });
};
```

With this change, the form will be reset immediately after a successful API call, providing a smoother user experience.  The `onClose` callback in `toast.success` is no longer needed and has been removed.
'''



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

        # Proceed to write only if the file already exists
        with open(file_name, "w") as file:
            file.write(code)

        print(f"File '{file_name}' written successfully.")

except FileNotFoundError as fnf_error:
    print(f"File error: {fnf_error}")

except Exception as e:
    print(f"An error occurred while running extract solution test: {e}")