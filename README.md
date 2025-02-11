#OCR-bib-number
# 📌 Enhanced Bib Number Detection Using OCR and OpenCV

## 🔍 Overview

This project enhances the detection and extraction of bib numbers from race images using OpenCV for advanced image preprocessing and Tesseract OCR for text recognition. The extracted bib numbers are saved in a JSON file for further analysis.

## 🚀 Features

- 🎨 Advanced image preprocessing using grayscale conversion, Gaussian blur, histogram equalization, and morphological operations.
- 🔍 Dynamic region of interest (ROI) selection for better accuracy.
- 🔠 Enhanced OCR processing using optimized Tesseract configurations.
- 📂 Saves extracted bib numbers in a structured JSON format.

## 🛠 Installation

### 📌 Prerequisites

Ensure you have the following installed:

- 🐍 Python 3.x
- 🌿 Git
- 🖼 OpenCV (`cv2`)
- 🔠 Tesseract OCR

### ⚙️ Setup

1. 🖥 Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. 📦 Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. 🔠 Set up Tesseract OCR:
   - 🪟 Windows: Download and install from [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
   - 🐧 Linux/macOS: Install via package manager (`sudo apt install tesseract-ocr`)
4. 🛠 Update `pytesseract` path if needed in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

## ▶️ Usage

1. 📂 Place images in the `images/` folder.
2. ▶️ Run the script:
   ```sh
   python script.py
   ```
3. 💾 Extracted bib numbers will be saved in `bib_numbers.json`.

## 📊 Output

The script generates a JSON file with results:

```json
{
  "image1.jpg": "1234",
  "image2.jpg": "5678",
  "image3.jpg": "Not Detected"
}
```

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
