import cv2
import numpy as np

from image_preprocessing import preprocess_image
from crack_detection import detect_cracks
from contour_analysis import analyze_contours
from severity_classifier import classify_severity


def process_image(image_path):
    # Load image
    image = cv2.imread(image_path)
    
    # Preprocess the image
    processed_image = preprocess_image(image)
    
    # Detect cracks
    cracks = detect_cracks(processed_image)
    
    # Analyze contours
    crack_metrics = analyze_contours(cracks)
    
    # Classify severity
    severity = classify_severity(crack_metrics['total_area'])
    
    # Return results
    return {
        'crack_count': crack_metrics['crack_count'],
        'total_area': crack_metrics['total_area'],
        'total_length': crack_metrics['total_length'],
        'severity': severity
    }