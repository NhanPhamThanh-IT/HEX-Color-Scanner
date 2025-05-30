"""
Color Extractor Package

This package provides tools for extracting and visualizing colors from images.
"""

from .color_extractor import ColorExtractor
from .image_handler import ImageHandler
from .plotter import ColorPlotter

__all__ = ['ColorExtractor', 'ImageHandler', 'ColorPlotter']