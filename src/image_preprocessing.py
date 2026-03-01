import cv2
import numpy as np


def grayscale(image):
    """
    Convert the image to grayscale.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY


def thresholding(image, threshold=128):
    """
    Apply binary thresholding to the image.
    """
    _, thresh = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return thresh


def edge_detection(image):
    """
    Perform edge detection using the Canny algorithm.
    """
    return cv2.Canny(image, 100, 200)