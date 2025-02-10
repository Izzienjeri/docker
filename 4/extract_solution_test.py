import os
from extract_solution import extract_solution

llm_response = r'''
```python
import cv2
import cv2.aruco as aruco
import os
from typing import Any
def generate_aruco_marker(
    marker_id: Any,
    dictionary_id: Any,
    output_folder: str = "aruco_markers",
    marker_size: int = 200
) -> None:
    """
    Generates and saves an ArUco marker image.
    Args:
        marker_id: The ID of the marker to generate.
        dictionary_id: The ArUco dictionary to use (e.g., aruco.DICT_6X6_250).
        output_folder: The folder to save the marker image to.
        marker_size: The size (in pixels) of the output marker image.
    """
    dictionary = aruco.Dictionary_get(dictionary_id)
    marker_image = aruco.drawMarker(dictionary, marker_id, marker_size)
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)
    output_filename = os.path.join(output_folder, f"marker_{marker_id}.png")
    cv2.imwrite(output_filename, marker_image)
    print(f"Marker saved to: {output_filename}")
# Example usage:
generate_aruco_marker(marker_id=1, dictionary_id=aruco.DICT_6X6_250)
generate_aruco_marker(marker_id=50, dictionary_id=aruco.DICT_4X4_50, marker_size=250)
generate_aruco_marker(marker_id=10, dictionary_id=aruco.DICT_5X5_100, output_folder="custom_markers")
```
Key improvements in this code:
* **Type Hinting:** Added type hints (`Any`, `str`, `int`) for better readability and maintainability.  While `marker_id` and `dictionary_id` could be more specific, `Any` allows flexibility.  Consider using `int` if you're only working with integer IDs.
* **Output Folder Handling:**  Uses `os.makedirs(output_folder, exist_ok=True)` to create the output directory if it doesn't exist, preventing errors.
* **Clearer Output:**  Prints a message indicating where the marker image was saved.
* **Example Usage:** Demonstrates how to use the function with different parameters, including a custom output folder.
* **Docstring Enhancement:** The docstring is more comprehensive and clearly explains the function's purpose and parameters.
This revised code is more robust, user-friendly, and follows best practices.  It's now ready to be used reliably to generate ArUco markers.
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

