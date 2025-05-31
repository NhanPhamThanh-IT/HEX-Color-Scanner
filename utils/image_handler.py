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
    
    def __init__(self, image_path: str):
        """
        Initializes the ImageHandler with an image file.
        
        Opens the image from the specified path and converts it to RGB format.
        Extracts all pixel data as RGB tuples for further processing.
        
        Args:
            image_path (str): Path to the image file to be loaded.
            
        Raises:
            FileNotFoundError: If the image file doesn't exist.
            PIL.UnidentifiedImageError: If the file is not a valid image.
        """
        self.image = Image.open(image_path).convert("RGB")
        self.pixels = list(self.image.getdata())
        
    def get_pixels(self):
        """
        Returns the pixel data of the image as a list of RGB tuples.
        
        This method provides access to the raw pixel data of the image,
        which is stored as a list of RGB tuples, where each tuple contains
        three integer values representing red, green, and blue color channels.
        
        Returns:
            list: A list of RGB tuples, where each tuple contains three integers
                 in the range [0, 255] representing the red, green, and blue
                 color values for each pixel in the image.
                 
        Example:
            >>> handler = ImageHandler('image.jpg')
            >>> pixels = handler.get_pixels()
            >>> print(pixels[0])  # Print the RGB values of the first pixel
            (255, 240, 230)
        """
        return self.pixels

    def show(self):
        """
        Displays the image.
        
        Returns the PIL Image object for display purposes. In interactive
        environments like Jupyter notebooks, the returned image will be
        automatically displayed. In other environments, you may need to
        use PIL's built-in show() method on the returned object.
        
        Returns:
            PIL.Image.Image: The loaded image in RGB format.
            
        Example:
            >>> handler = ImageHandler('image.jpg')
            >>> image = handler.show()
            >>> # For non-interactive environments:
            >>> # image.show()
        """
        return self.image

    def get_important_pixels(self):
        """
        Returns the most common colors in the image.
        
        This method counts the occurrences of each unique RGB color in the image
        and returns the 10 most frequently occurring colors. This is useful for
        identifying the predominant colors in an image without performing clustering.
        
        Returns:
            list: A list of the 10 most common RGB tuples in the image, ordered
                 by frequency (most common first). Each tuple contains three integers
                 in the range [0, 255] representing the red, green, and blue values.
                 
        Example:
            >>> handler = ImageHandler('image.jpg')
            >>> common_colors = handler.get_important_pixels()
            >>> print(f"The most common color is RGB{common_colors[0]}")
        """
        color_counts = Counter(self.pixels)
        most_common_colors = color_counts.most_common(10)
        return [color[0] for color in most_common_colors]

    def get_group_important_pixels(self, num_colors: int = 20):
        """
        Returns dominant color groups using KMeans clustering with a default number of clusters.
        :return: List of RGB tuples representing dominant colors, sorted by frequency.
        """
        pixel_array = np.array(self.pixels)

        kmeans = KMeans(n_clusters=num_colors, random_state=42)
        labels = kmeans.fit_predict(pixel_array)
        centers = kmeans.cluster_centers_

        counts = Counter(labels)

        sorted_clusters = sorted(counts.items(), key=lambda x: -x[1])
        sorted_colors = [tuple(map(int, centers[cluster_idx])) for cluster_idx, _ in sorted_clusters]
        return sorted_colors
