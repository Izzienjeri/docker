import os
from extract_solution import extract_solution

llm_response = '''
"```python
import cv2
import cv2.aruco as aruco
import os
def generate_aruco_marker(
    marker_id: int,
    dictionary_id: int,
    output_folder: str = ""aruco_markers"",
    marker_size: int = 200
) -> None:
    """"""
    Generates and saves an ArUco marker image.
    Args:
        marker_id: The ID of the marker to generate.
        dictionary_id: The ArUco dictionary to use (e.g., aruco.DICT_6X6_250).
        output_folder: The folder to save the marker image to.
        marker_size: The size (in pixels) of the output marker image.
    """"""
    # Create the ArUco dictionary
    aruco_dict = aruco.Dictionary_get(dictionary_id)
    # Generate the marker image
    marker_image = aruco.drawMarker(aruco_dict, marker_id, marker_size)
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    # Create the output filename
    output_filename = f""marker_{marker_id}.png""
    output_path = os.path.join(output_folder, output_filename)
    # Save the marker image
    cv2.imwrite(output_path, marker_image)
# Example usage:
if __name__ == ""__main__"":
    # Generate a marker with ID 23 using 6x6 ArUco dictionary
    generate_aruco_marker(
        marker_id=23,
        dictionary_id=cv2.aruco.DICT_6X6_250,
        marker_size=300
    )
```
This code:
1. Imports the necessary libraries (OpenCV and os)
2. Creates the specified ArUco dictionary using `aruco.Dictionary_get()`
3. Generates the marker image using `aruco.drawMarker()`
4. Creates the output folder if it doesn't exist
5. Saves the marker image as a PNG file
You can use it by calling the function with appropriate parameters. For example:
```python
# Generate different markers with different dictionaries
generate_aruco_marker(0, cv2.aruco.DICT_4X4_50)  # 4x4 marker with ID 0
generate_aruco_marker(1, cv2.aruco.DICT_5X5_100)  # 5x5 marker with ID 1
generate_aruco_marker(2, cv2.aruco.DICT_6X6_250)  # 6x6 marker with ID 2
```
Common ArUco dictionary IDs include:
- `cv2.aruco.DICT_4X4_50`
- `cv2.aruco.DICT_4X4_100`
- `cv2.aruco.DICT_5X5_50`
- `cv2.aruco.DICT_5X5_100`
- `cv2.aruco.DICT_6X6_50`
- `cv2.aruco.DICT_6X6_250`
- `cv2.aruco.DICT_7X7_50`
- `cv2.aruco.DICT_7X7_100`
The generated markers will be saved in the specified output folder (default is ""aruco_markers"") with filenames like ""marker_0.png"", ""marker_1.png"", etc.






"

"```python
import cv2
import cv2.aruco as aruco
import os
def generate_aruco_marker(
    marker_id: int,
    dictionary_id: int,
    output_folder: str = ""aruco_markers"",
    marker_size: int = 200
) -> None:
    """"""
    Generates and saves an ArUco marker image.
    Args:
        marker_id: The ID of the marker to generate.
        dictionary_id: The ArUco dictionary to use (e.g., aruco.DICT_6X6_250).
        output_folder: The folder to save the marker image to.
        marker_size: The size (in pixels) of the output marker image.
    """"""
    # Create the ArUco dictionary
    aruco_dict = aruco.Dictionary_get(dictionary_id)
    # Generate the marker image
    marker_image = aruco.drawMarker(aruco_dict, marker_id, marker_size)
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    # Create the output filename
    output_filename = f""marker_{marker_id}.png""
    output_path = os.path.join(output_folder, output_filename)
    # Save the marker image
    cv2.imwrite(output_path, marker_image)
# Example usage:
if __name__ == ""__main__"":
    # Generate a marker with ID 23 using 6x6 ArUco dictionary
    generate_aruco_marker(
        marker_id=23,
        dictionary_id=cv2.aruco.DICT_6X6_250,
        marker_size=300
    )
```
This code:
1. Imports the necessary libraries (OpenCV and os)
2. Creates the specified ArUco dictionary using `aruco.Dictionary_get()`
3. Generates the marker image using `aruco.drawMarker()`
4. Creates the output folder if it doesn't exist
5. Saves the marker image as a PNG file
You can use it by calling the function with appropriate parameters. For example:
```python
# Generate different markers with different dictionaries
generate_aruco_marker(0, cv2.aruco.DICT_4X4_50)  # 4x4 marker with ID 0
generate_aruco_marker(1, cv2.aruco.DICT_5X5_100)  # 5x5 marker with ID 1
generate_aruco_marker(2, cv2.aruco.DICT_6X6_250)  # 6x6 marker with ID 2
```
Common ArUco dictionary IDs include:
- `cv2.aruco.DICT_4X4_50`
- `cv2.aruco.DICT_4X4_100`
- `cv2.aruco.DICT_5X5_50`
- `cv2.aruco.DICT_5X5_100`
- `cv2.aruco.DICT_6X6_50`
- `cv2.aruco.DICT_6X6_250`
- `cv2.aruco.DICT_7X7_50`
- `cv2.aruco.DICT_7X7_100`
The generated markers will be saved in the specified output folder (default is ""aruco_markers"") with filenames like ""marker_0.png"", ""marker_1.png"", etc.






"
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
