"""
Color Extractor Module

This module provides functionality to extract and process color data from images.
It contains the ColorExtractor class which handles pixel data and converts 
RGB colors to hexadecimal format.
"""

class ColorExtractor:
    """
    A class for extracting and processing colors from pixel data.
    
    This class takes pixel data (typically from an image) and provides methods
    to extract unique colors in hexadecimal format, which can be useful for
    color analysis, palette creation, and data visualization.
    
    Attributes:
        pixels (list): A list of RGB tuples representing the pixel data from an image.
    """
    
    def __init__(self, pixels):
        """
        Initializes the ColorExtractor with a list of pixel data.
        
        Args:
            pixels (list): A list of RGB tuples (e.g., [(255, 0, 0), (0, 255, 0)]) 
                representing the pixel data from an image. Each tuple should contain
                three integer values between 0 and 255, representing the red, green,
                and blue components of a pixel.
                
        Example:
            >>> pixel_data = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
            >>> extractor = ColorExtractor(pixel_data)
        """
        self.pixels = pixels

    def extract_unique_hex(self):
        """
        Extracts unique colors from the pixel data and converts them to hexadecimal format.
        
        This method processes all pixels in the initialized data, converts each RGB tuple
        to a hexadecimal color code (e.g., '#ff0000' for red), and returns only unique 
        color values. The hexadecimal values are standardized to lowercase.
        
        Returns:
            list: A list of unique colors in hexadecimal format (e.g., ['#ff0000', '#00ff00']).
                  Each color is represented as a string starting with '#' followed by 
                  six hexadecimal digits, with the first two representing red, the middle
                  two representing green, and the last two representing blue.
                  
        Example:
            >>> extractor = ColorExtractor([(255, 0, 0), (0, 255, 0), (255, 0, 0)])
            >>> extractor.extract_unique_hex()
            ['#ff0000', '#00ff00']
        """
        hex_colors = set()
        for pixel in self.pixels:
            hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel)
            hex_colors.add(hex_color.lower())
        return list(hex_colors)
