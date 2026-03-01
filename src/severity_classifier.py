import numpy as np

def classify_crack(area, length):
    severity = "Unknown"

    # Simple rule-based classification
defined based on area and length
    if area < 10 and length < 5:
        severity = "Minor"
    elif area < 30 and length < 15:
        severity = "Moderate"
    elif area >= 30 or length >= 15:
        severity = "Severe"

    return severity

# Sample usage
if __name__ == '__main__':
    area = float(input('Enter the area of the crack: '))
    length = float(input('Enter the length of the crack: '))
    result = classify_crack(area, length)
    print(f'Crack severity is: {result}')