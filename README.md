# Barcode Generation and Detection System Using Python

## Project Overview

The **Barcode Generation and Detection System Using Python** is an MCA major project that demonstrates how to generate and detect barcodes using Python programming.

The project has two main modules: barcode generation and barcode detection. The generation module creates Code 128 barcodes from user-provided input, while the detection module reads barcode information from image files and displays the extracted data.

## Project Objectives

- To generate Code 128 barcodes using Python.
- To detect barcodes from image files.
- To extract encoded information from detected barcodes.
- To identify the barcode format.
- To understand the practical application of Python libraries in barcode processing.

## Features

### 1. Barcode Generation
- Accepts numerical or alphanumeric input from the user.
- Generates Code 128 barcodes.
- Saves the generated barcode as a PNG image.

### 2. Barcode Detection
- Accepts a barcode image path from the user.
- Detects barcode information using Pyzbar.
- Extracts the encoded data.
- Identifies the barcode type.
- Highlights the detected barcode using OpenCV.

## Technologies and Libraries Used

- **Python:** Main programming language.
- **Python-Barcode:** Barcode generation.
- **Pillow:** Image writing support.
- **OpenCV:** Image processing and display.
- **Pyzbar:** Barcode detection and decoding.
- **ZBar:** Barcode decoding library.

## Project Structure

```text
Barcode-Generation-and-Detection/
│
├── generate_barcode.py
├── barcode_scanner.py
├── generated_barcode.png
└── README.md
```

## Installation and Setup

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Install Required Python Packages

Open the terminal and execute:

```bash
pip install python-barcode pillow opencv-python pyzbar
```

### Step 3: Install ZBar

For macOS users with Homebrew:

```bash
brew install zbar
```

**Note:** The current scanner code uses a ZBar library path configured for Apple Silicon Macs with Homebrew installed in `/opt/homebrew`.

## How to Run the Project

### Barcode Generation

Run the following command:

```bash
python3 generate_barcode.py
```

Enter a numerical or alphanumeric value when prompted.

The program generates a Code 128 barcode and saves it as:

```text
generated_barcode.png
```

### Barcode Detection

Run the following command:

```bash
python3 barcode_scanner.py
```

Enter the path of the barcode image when prompted.

The program attempts to detect and decode the barcode, display its data and identify its barcode type.

## Sample Output

The project generates a barcode image in PNG format. The detection module displays the extracted barcode information and highlights the detected barcode region.

## Project Limitations

- Barcode detection currently works with image files rather than a live camera.
- The generation module currently generates Code 128 barcodes.
- The scanner requires the ZBar library.
- The scanner's current library path is configured for a specific macOS Homebrew installation.

## Future Scope

- Real-time barcode scanning using a webcam.
- Development of a graphical user interface.
- Integration with a database.
- Support for additional barcode formats.
- Improved cross-platform library configuration.

## Project Team

**Department:** Master of Computer Applications (MCA)  
**University:** Adamas University  
**Academic Year:** 2026–2027

### Team Members

1. Debjyoti Mondal
2. Sneha Mondal
3. Rittija Chowdhury

**Project Guide:** Dr. Biswajit Halder  
**Project Coordinator:** Dr. Soumitra Roy  
**Head of Department:** Dr. Abhishek Roy

---

**Project:** Barcode Generation and Detection System Using Python  
**Institution:** Adamas University
