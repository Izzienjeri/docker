import cv2
import cv2.aruco as aruco
import os
from typing import Any

def generate_aruco_marker(
    marker_id: Any,
    dictionary_id: Any,
    output_folder: str = "aruco_markers",
    marker_size: int = 200,
) -> None:
    """
    Generates and saves an ArUco marker image.

    Args:
        marker_id: The ID of the marker to generate.
        dictionary_id: The ArUco dictionary to use (e.g., aruco.DICT_6X6_250).
        output_folder: The folder to save the marker image to.
        marker_size: The size (in pixels) of the output marker image.

    Raises:
        TypeError: if an invalid dictionary id is used
        ValueError: if the marker id is out of range for the given dictionary
        ValueError: if the marker size is too small
        ValueError: if the output folder is invalid
    """

    # Create the output folder if it doesn't exist
    if not output_folder:
        raise ValueError("Output folder cannot be empty.")
    os.makedirs(output_folder, exist_ok=True)

    # Get the ArUco dictionary
    try:
        aruco_dict = aruco.getPredefinedDictionary(dictionary_id)
    except cv2.error as e:
        raise TypeError("Invalid dictionary ID") from e
    
    # Check marker id range
    try:
        if not (0 <= marker_id < aruco_dict.bytesList.shape[0]):
            raise ValueError(
                f"Invalid marker ID. For this dictionary, marker ID must be between 0 and {aruco_dict.bytesList.shape[0] - 1}"
            )
    except AttributeError:
        raise ValueError(
            f"Invalid marker ID. For this dictionary, marker ID must be between 0 and {aruco_dict.markerSize - 1}"
        )

    # Check marker size
    if marker_size <= 0:
        raise ValueError("Marker size must be a positive integer.")

    # Generate the marker image
    try:
        marker_image = aruco.generateImageMarker(aruco_dict, marker_id, marker_size)
    except cv2.error as e:
        if "sidePixels >= (markerSize + 2*borderBits)" in str(e):
            raise ValueError("Marker size is too small for the given dictionary.") from e
        else:
            raise

    # Save the marker image
    output_path = os.path.join(output_folder, f"marker_{marker_id}.png")
    cv2.imwrite(output_path, marker_image)

    print(f"ArUco marker saved to: {output_path}")