import cv2
import cv2.aruco as aruco
import os

def generate_aruco_marker(
    marker_id: int,
    dictionary_id: int,
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
    # Create the directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Get the ArUco dictionary
    dictionary = aruco.Dictionary_get(dictionary_id)
    
    # Generate the marker image
    marker_image = aruco.drawMarker(dictionary, marker_id, marker_size)
    
    # Create the output filename
    output_filename = os.path.join(output_folder, f"marker_{marker_id}.png")
    
    # Save the marker image
    cv2.imwrite(output_filename, marker_image)
    
    print(f"Marker {marker_id} saved to {output_filename}")

# Example usage:
# generate_aruco_marker(42, aruco.DICT_6X6_250)