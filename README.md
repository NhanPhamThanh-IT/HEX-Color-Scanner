# <div align="center">HEX Color Scanner</div>

A streamlined web application for extracting and displaying HEX color codes from uploaded images.

![HEX Color Scanner](https://img.shields.io/badge/App-HEX%20Color%20Scanner-blue) ![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen) ![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-red)

## Overview

HEX Color Scanner is a user-friendly web application that allows you to upload an image and instantly extract the dominant HEX color codes. Perfect for designers, developers, and anyone working with color palettes who needs to quickly identify and use colors from existing images.

## Features

- 🖼️ **Easy Image Upload**: Support for PNG, JPG, and JPEG formats
- 🎨 **Color Extraction**: Identifies dominant colors using K-Means clustering algorithm
- 📋 **Copy to Clipboard**: One-click copy for any extracted HEX code
- ⚙️ **Adjustable Settings**: Control the number of colors to extract (1-50)
- 🔍 **Visual Display**: See all extracted colors in an organized grid layout

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/HEX-Color-Scanner.git
cd HEX-Color-Scanner
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Access the application in your web browser (typically at http://localhost:8501)

3. Upload an image using the file uploader

4. Adjust the number of colors to extract using the sidebar slider

5. View the extracted colors and copy any HEX code with a single click

## Dependencies

- Streamlit: Web application framework
- Pillow: Image processing library
- scikit-learn: For K-Means clustering
- NumPy: Numerical computing
- pyperclip: Clipboard functionality

## Project Structure

```
HEX-Color-Scanner/
│
├── app.py               # Main Streamlit application
├── requirements.txt     # Required packages
├── LICENSE              # License information
├── README.md            # This file
└── utils/               # Utility modules
    ├── __init__.py
    ├── color_extractor.py   # Color extraction functionality
    └── image_handler.py     # Image processing functionality
```

## How It Works

1. The application uses the `ImageHandler` class to process uploaded images
2. K-Means clustering algorithm groups similar colors in the image
3. The `ColorExtractor` class converts RGB color values to HEX format
4. Results are displayed in an interactive grid with copy functionality

## License

This project is licensed under the terms included in the LICENSE file.

## Acknowledgements

- Built with [Streamlit](https://streamlit.io/)
- Uses [scikit-learn](https://scikit-learn.org/) for color clustering