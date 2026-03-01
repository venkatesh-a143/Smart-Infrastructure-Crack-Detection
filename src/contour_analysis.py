import cv2
import numpy as np

def analyze_contours(image_path):
    """
    Analyze contours in an image and calculate crack metrics.
    Returns: crack_count, total_area, total_length
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    crack_count = len(contours)
    total_area = 0
    total_length = 0
    
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        total_area += area
        total_length += perimeter
    
    return crack_count, total_area, total_length

def draw_contours_on_image(image_path, output_path):
    """
    Draw detected contours on the image and save it.
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.imwrite(output_path, image)
    
    return image

if __name__ == '__main__':
    image_path = 'path_to_image.jpg'
    crack_count, area, length = analyze_contours(image_path)
    print(f'Crack Count: {crack_count}')
    print(f'Total Area: {area}')
    print(f'Total Length: {length}')