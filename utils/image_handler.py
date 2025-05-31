"""
ImageHandler module for image processing and color analysis.

This module provides the ImageHandler class which offers functionality to load images,
extract pixel data, identify dominant colors, and perform color clustering using KMeans.

Classes:
    ImageHandler: A class for handling image processing and color extraction operations.
"""

from PIL import Image
from sklearn.cluster import KMeans
import numpy as np
from collections import Counter

class ImageHandler:
    """
    A class that handles image processing and color analysis tasks.
    
    The ImageHandler class provides methods to load images, extract pixel data,
    and perform color analysis operations like finding the most common colors
    or dominant color groups using clustering techniques.
    
    Attributes:
        image (PIL.Image.Image): The loaded image in RGB format.
        pixels (list): List of RGB tuples representing all pixels in the image.
    """

    def __init__(self, image_file):
        """
        Initializes the ImageHandler with an image file.
        
        Opens the image from the specified path or file object and converts it to RGB format.
        Extracts all pixel data as RGB tuples for further processing.
        
        Args:
            image_file: Path to the image file or file-like object (e.g., Streamlit UploadedFile).
            
        Raises:
            FileNotFoundError: If the image file doesn't exist.
            PIL.UnidentifiedImageError: If the file is not a valid image.
        """
        self.image = Image.open(image_file).convert("RGB")
        self.pixels = list(self.image.getdata())

    def get_pixels(self):
        """
        Returns the pixel data of the image as a list of RGB tuples.
        
        Returns:
            list: A list of RGB tuples, where each tuple contains three integers
                  in the range [0, 255] representing red, green, and blue color channels.
        
        Example:
            >>> handler = ImageHandler('image.jpg')
            >>> pixels = handler.get_pixels()
            >>> print(pixels[0])
            (255, 240, 230)
        """
        return self.pixels

    def show(self):
        """
        Displays the image.
        
        Returns:
            PIL.Image.Image: The loaded image in RGB format.
        
        Example:
            >>> handler = ImageHandler('image.jpg')
            >>> image = handler.show()
            >>> # image.show()  # Uncomment in non-interactive environments
        """
        return self.image

    def get_important_pixels(self):
        """
        Returns the 10 most common colors in the image.
        
        This method identifies and returns the top 10 most frequent RGB values
        appearing in the image based on pixel counts.
        
        Returns:
            list: A list of the 10 most common RGB tuples sorted by frequency in descending order.
        
        Example:
            >>> handler = ImageHandler('image.jpg')
            >>> common_colors = handler.get_important_pixels()
            >>> print(f"Most common color: {common_colors[0]}")
        """
        color_counts = Counter(self.pixels)
        most_common_colors = color_counts.most_common(10)
        return [color[0] for color in most_common_colors]

    def get_group_important_pixels(self, num_colors: int = 20):
        """
        Returns dominant color groups in the image using KMeans clustering.
        
        This method applies KMeans clustering to group similar colors in the image,
        returning the cluster centers sorted by frequency of occurrence.
        
        Args:
            num_colors (int): The number of color clusters to form. Default is 20.
        
        Returns:
            list: A list of RGB tuples representing dominant colors, sorted from most to least frequent.
        
        Raises:
            ValueError: If num_colors is less than 1 or more than the number of pixels.
        
        Example:
            >>> handler = ImageHandler('image.jpg')
            >>> dominant_colors = handler.get_group_important_pixels(num_colors=5)
            >>> print(dominant_colors)
        """
        if num_colors < 1 or num_colors > len(self.pixels):
            raise ValueError("num_colors must be between 1 and the number of pixels in the image.")

        pixel_array = np.array(self.pixels)
        kmeans = KMeans(n_clusters=num_colors, random_state=42)
        labels = kmeans.fit_predict(pixel_array)
        centers = kmeans.cluster_centers_

        counts = Counter(labels)
        sorted_clusters = sorted(counts.items(), key=lambda x: -x[1])
        sorted_colors = [tuple(map(int, centers[cluster_idx])) for cluster_idx, _ in sorted_clusters]
        return sorted_colors
