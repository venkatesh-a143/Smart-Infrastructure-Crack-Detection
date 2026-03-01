import cv2
import numpy as np
import os

def create_road_image_with_cracks(width=800, height=600):
    """Create a synthetic road image with cracks"""
    image = np.ones((height, width, 3), dtype=np.uint8) * 100
    noise = np.random.randint(0, 30, (height, width, 3))
    image = cv2.add(image, noise.astype(np.uint8))
    
    # Add cracks as black lines
    cv2.line(image, (300, 100), (310, 500), (20, 20, 20), 3)
    cv2.line(image, (200, 200), (600, 400), (30, 30, 30), 2)
    cv2.line(image, (100, 300), (700, 320), (25, 25, 25), 2)
    
    for i in range(0, 400, 20):
        cv2.line(image, (500 + i, 50), (510 + i, 150), (20, 20, 20), 2)
    
    return image

def create_bridge_image_with_cracks(width=800, height=600):
    """Create a synthetic bridge surface image with cracks"""
    image = np.ones((height, width, 3), dtype=np.uint8) * 150
    
    for i in range(height):
        for j in range(width):
            image[i, j] += np.random.randint(-20, 20)
    
    # Horizontal cracks
    for i in range(100, 500, 80):
        cv2.line(image, (50, i), (750, i), (40, 40, 40), 2)
    
    # Vertical cracks
    for j in range(100, 700, 100):
        cv2.line(image, (j, 50), (j, 550), (40, 40, 40), 2)
    
    # Diagonal cracks
    cv2.line(image, (100, 100), (700, 500), (35, 35, 35), 2)
    cv2.line(image, (700, 100), (100, 500), (35, 35, 35), 2)
    
    return image

def generate_sample_images(output_dir='sample_images'):
    """Generate and save sample images"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    road_image = create_road_image_with_cracks()
    cv2.imwrite(os.path.join(output_dir, 'sample_road_cracks.jpg'), road_image)
    
    bridge_image = create_bridge_image_with_cracks()
    cv2.imwrite(os.path.join(output_dir, 'sample_bridge_cracks.jpg'), bridge_image)
    
    print("Sample images generated successfully!")

if __name__ == '__main__':
    generate_sample_images()