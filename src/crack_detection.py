import cv2
import numpy as np


def contour_detection(image_path):
    """Detect contours in an image."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def crack_analysis(image_path):
    """Analyze the cracks in the given image."""
    contours = contour_detection(image_path)
    return len(contours)


if __name__ == '__main__':
    # Example usage:
    image_path = 'path_to_image.jpg'
    print(f'Detected contours: {contour_detection(image_path)}')
    print(f'Number of cracks: {crack_analysis(image_path)}')
