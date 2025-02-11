import pytesseract
import cv2
import numpy as np
import os
import json


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 




def preprocess_image(image):
    """Preprocess the image to improve OCR accuracy."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Grayscale conversion
    gray = cv2.GaussianBlur(gray, (5, 5), 0)  # Gaussian blur to reduce noise
    gray = cv2.equalizeHist(gray)  # Histogram equalization to improve contrast
    edges = cv2.Canny(gray, 50, 150)  # Edge detection
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)  # Dilation
    edges = cv2.erode(edges, kernel, iterations=1)  # Erosion
    return edges

def extract_bib_number(image_path, debug=False):
    """Extract the bib number from an image."""
    image = cv2.imread(image_path)
    if image is None:
        if debug:
            print(f"Error: Unable to read image '{image_path}'.")
        return None

    # Preprocess the image
    preprocessed_image = preprocess_image(image)

    # Define the region of interest (ROI) for OCR
    h, w = preprocessed_image.shape[:2]
    x, y, w, h = int(w * 0.2), int(h * 0.4), int(w * 0.6), int(h * 0.2)  # Adjusted dynamic ROI
    roi = preprocessed_image[y:y+h, x:x+w]

    # Use OCR to extract text
    custom_config = r'--oem 3 --psm 6'  # Experiment with different configurations
    text = pytesseract.image_to_string(roi, config=custom_config).strip()
    text = ''.join(c for c in text if c.isdigit())  # Keep only numbers

    if text:
        if debug:
            print(f"{os.path.basename(image_path)} → Bib Number: {text}")
        return text

    if debug:
        print(f"{os.path.basename(image_path)} → No bib number detected.")
    return None

def process_images(image_folder, output_json="bib_numbers.json", debug=True):
    """Process multiple images and save results to a JSON file."""
    results = {}

    if not os.path.exists(image_folder):
        print(f"Error: Folder '{image_folder}' not found.")
        return

    # Loop through all images in the folder
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Process only image files
            image_path = os.path.join(image_folder, filename)
            bib_number = extract_bib_number(image_path, debug=debug)
            results[filename] = bib_number if bib_number else "Not Detected"

    # Save results to JSON
    with open(output_json, "w") as json_file:
        json.dump(results, json_file, indent=4)

    print(f"\nResults saved to {output_json}")

# Example usage
image_folder = "images"  # Replace with your folder path containing images
process_images(image_folder, debug=True)


