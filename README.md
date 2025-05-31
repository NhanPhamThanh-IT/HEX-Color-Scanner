<!-- 
HEX Color Scanner - A streamlined tool for extracting color palettes from images
Created: May 31, 2025
Version: 1.0.0
-->
# <div align="center">HEX Color Scanner</div>

![HEX Color Scanner](https://img.shields.io/badge/App-HEX%20Color%20Scanner-blue) ![Python](https://img.shields.io/badge/Python-3.9%2B-brightgreen) ![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1-red) ![License](https://img.shields.io/badge/License-MIT-yellow) ![Version](https://img.shields.io/badge/Version-1.0.0-orange)

## 📋 Overview

HEX Color Scanner is a sophisticated yet user-friendly web application that allows you to upload any image and instantly extract the dominant HEX color codes. Using advanced color clustering algorithms, it intelligently identifies the most representative colors in your images, making it indispensable for:

- 🎨 Graphic designers seeking color inspiration
- 💻 Web developers creating consistent color schemes
- 📱 UI/UX designers working on application interfaces
- 🖼️ Digital artists analyzing color palettes
- 🧪 Color theory researchers and educators

Whether you're building a website, crafting a brand identity, or simply curious about the color composition of your favorite images, HEX Color Scanner provides immediate, accurate results with a clean, modern interface.

## ✨ Features

- 🖼️ **Universal Image Support**: Seamlessly works with PNG, JPG, and JPEG formats of any resolution
- 🎨 **Advanced Color Extraction**: Employs K-Means clustering algorithm to identify true dominant colors, not just the most frequent pixels
- 📋 **Instant Copy Functionality**: One-click copy for any HEX code with visual confirmation
- ⚙️ **Customizable Analysis**: Fine-tune results with adjustable color extraction (1-50 colors)
- 🔍 **Interactive Color Display**: Visually appealing grid layout with color swatches and codes
- 🔄 **Real-time Processing**: Get results immediately after upload with no waiting
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- 🛡️ **Error Handling**: Robust validation for image formats and processing

## 🚀 Installation

### Prerequisites
- Python 3.9 or higher
- Git (optional, for cloning)
- Internet connection (for dependency installation)

### Method 1: From Source
1. Clone the repository:
```bash
git clone https://github.com/yourusername/HEX-Color-Scanner.git
cd HEX-Color-Scanner
```

2. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Method 2: Using pip (if published)
```bash
pip install hex-color-scanner
```

### System Requirements
- **Minimum**: 2GB RAM, 1GHz CPU
- **Recommended**: 4GB RAM, 2GHz multi-core CPU for faster processing of high-resolution images

## 💻 Usage

### Starting the Application
1. Navigate to the project directory and start the application:
```bash
# If using virtual environment
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# Launch the app
streamlit run app.py
```

2. Your default web browser will automatically open with the application running at http://localhost:8501

### Using the Interface
1. **Upload an Image**:
   - Click the "Upload image" button
   - Select any PNG, JPG, or JPEG file from your device
   - The image will display on screen after successful upload

2. **Configure Settings**:
   - Use the sidebar slider to adjust the number of colors to extract (1-50)
   - More colors will capture subtle variations, fewer will focus on dominant tones

3. **Analyze Results**:
   - View the extracted colors displayed in a responsive grid layout
   - Each color is shown as a visual swatch with its corresponding HEX code

4. **Copy Colors**:
   - Click the "Copy" button under any color to copy its HEX code to clipboard
   - A toast notification will confirm successful copying
   - Use copied codes in design software, CSS, or any other application

### Tips for Best Results
- For brand analysis, upload logo images on white backgrounds
- For website color schemes, use screenshots of the homepage
- For nature-inspired palettes, try landscape photography
- Experiment with different extraction numbers to find the optimal palette size

## 🔧 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.45.1 | Interactive web application framework |
| matplotlib | 3.10.3 | Data visualization and color representation |
| pillow | 11.2.1 | Image processing and manipulation |
| scikit-learn | latest | K-Means clustering for color analysis |
| numpy | latest | Efficient numerical operations |
| pyperclip | latest | Cross-platform clipboard functionality |

### Core Technologies
- **Streamlit**: Provides the reactive web interface with minimal code
- **K-Means Clustering**: Unsupervised machine learning algorithm that groups pixels by color similarity
- **RGB to HEX Conversion**: Custom implementation for accurate color representation

## 📁 Project Structure

```
HEX-Color-Scanner/
│
├── app.py                 # Main Streamlit application entry point
├── requirements.txt       # Required dependencies with versions
├── LICENSE                # MIT License information
├── README.md              # Project documentation
└── utils/                 # Modular utility components
    ├── __init__.py        # Package initializer
    ├── color_extractor.py # RGB to HEX conversion and color processing
    └── image_handler.py   # Image loading, processing and analysis
```

### Component Details

#### app.py
The main application file that orchestrates the Streamlit interface, handles user inputs, and displays results. It implements:
- File upload system
- User interface components
- Visualization of extracted colors
- Copy-to-clipboard functionality
- Error handling and user feedback

#### utils/color_extractor.py
Specializes in color data manipulation:
- Converts RGB tuples to HEX format
- Ensures color uniqueness in results
- Formats color codes for display
- Manages color data structures

#### utils/image_handler.py
Handles all image-related operations:
- Loads and validates image files
- Extracts pixel data from images
- Implements K-Means clustering for color grouping
- Identifies dominant color patterns
- Optimizes performance for large images

## 🔬 How It Works

### Technical Process Flow
1. **Image Upload & Processing**:
   - User uploads an image through the Streamlit interface
   - `ImageHandler` class loads and converts the image to RGB format
   - Pixel data is extracted and prepared for analysis

2. **Color Analysis & Clustering**:
   - K-Means clustering algorithm (from scikit-learn) analyzes pixel data
   - Similar colors are grouped together into specified number of clusters
   - Cluster centers represent the dominant colors in the image
   - Colors are sorted by frequency/dominance in the image

3. **Color Conversion & Presentation**:
   - `ColorExtractor` class converts RGB values to standardized HEX format
   - Duplicate colors are removed to ensure a unique palette
   - Colors are displayed in a responsive grid layout with visual swatches
   - Each color is paired with its HEX code and a copy button

4. **User Interaction**:
   - User can adjust settings via sidebar controls
   - Copy functionality utilizes pyperclip for cross-platform clipboard access
   - Toast notifications provide feedback on successful actions

### Algorithm Details
The K-Means clustering implementation uses these parameters:
- **n_clusters**: User-defined (1-50), determines palette size
- **random_state**: Set to 42 for reproducible results
- **Initialization**: Uses k-means++ for optimal starting cluster centers
- **Convergence**: Iterates until cluster assignments stabilize

## 📊 Performance Considerations

- **Image Size**: Larger images (>4000px) may require more processing time
- **Color Count**: Requesting large numbers of colors (>30) increases computation time
- **Memory Usage**: High-resolution images with many colors may use significant memory
- **Optimization**: Internal sampling techniques maintain performance even with large images

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for full details.

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 👏 Acknowledgements

- Built with [Streamlit](https://streamlit.io/) - The fastest way to build data apps
- Uses [scikit-learn](https://scikit-learn.org/) for machine learning algorithms
- [Pillow](https://python-pillow.org/) for image processing
- [NumPy](https://numpy.org/) for numerical operations
- Icon designed by [Freepik](https://www.freepik.com/) from Flaticon

## 📧 Contact

For questions, feedback, or support, please open an issue on this repository or contact the developer at [your-email@example.com].

## 📈 Future Development

The HEX Color Scanner project has several planned enhancements for future releases:

1. **Color Scheme Suggestions**:
   - Automatic generation of complementary colors
   - Suggestions for analogous, triadic, and tetradic color schemes
   - CSS code snippets for web design implementation

2. **Advanced Export Options**:
   - Export palettes in Adobe ASE format
   - Generate color palette images for sharing
   - Direct integration with design software

3. **Enhanced Analysis**:
   - Color classification (warm/cool, pastel/vibrant)
   - Accessibility analysis for color blindness considerations
   - Color harmony scoring

4. **User Experience Improvements**:
   - Drag-and-drop interface for image upload
   - Custom color sorting options
   - User accounts to save favorite palettes

5. **Batch Processing**:
   - Analyze multiple images simultaneously
   - Compare color schemes across different images
   - Bulk export options

## 🔗 Related Projects

- [Color Theory Guide](https://github.com/example/color-theory-guide) - Educational resource about color usage in design
- [Web Design Color Tools](https://github.com/example/webdesign-color-tools) - Suite of tools for web developers
- [Image Analysis Suite](https://github.com/example/image-analysis-suite) - Comprehensive image processing toolkit