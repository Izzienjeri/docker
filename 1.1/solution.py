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

module.exports = transformScript;