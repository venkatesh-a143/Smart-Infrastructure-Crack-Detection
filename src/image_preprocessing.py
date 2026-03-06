def to_grayscale(image):
    """
    Convert an image to grayscale.
    
    Parameters:
    image (numpy.ndarray): Input image.

    Returns:
    numpy.ndarray: Grayscale image.
    """
    import cv2
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_threshold(image, threshold_value):
    """
    Apply a binary threshold to an image.
    
    Parameters:
    image (numpy.ndarray): Input grayscale image.
    threshold_value (int): Threshold value.

    Returns:
    numpy.ndarray: Binary image after thresholding.
    """
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image


def edge_detection(image):
    """
    Perform edge detection using Canny edge detector.
    
    Parameters:
    image (numpy.ndarray): Input grayscale image.

    Returns:
    numpy.ndarray: Image with edges detected.
    """
    return cv2.Canny(image, 100, 200)


def calculate_area(image):
    """
    Calculate the area of white regions in the binary image.
    
    Parameters:
    image (numpy.ndarray): Input binary image.

    Returns:
    float: Area of detected regions in square pixels converted to real-world units.
    """
    import numpy as np
    area = np.sum(image == 255)  # Count white pixels
    # Convert to real-world units based on pixel size, if known
    # Assume pixel_size is a known constant in square meters per pixel
    pixel_size = 0.01  # Example: 0.01 m² per pixel
    real_world_area = area * pixel_size
    return real_world_area
