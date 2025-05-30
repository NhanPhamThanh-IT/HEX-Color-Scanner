class ColorExtractor:
    def __init__(self, pixels):
        """
        Initializes the ColorExtractor with a list of pixel data.
        
        :param pixels: List of RGB tuples representing the pixel data.
        """
        self.pixels = pixels
    
    def extract_unique_hex(self):
        """
        Extracts unique colors from the pixel data and converts them to hexadecimal format.
        
        :return: A list of unique colors in hexadecimal format.
        """
        hex_colors = set()
        for pixel in self.pixels:
            hex_color = '#{:02x}{:02x}{:02x}'.format(*pixel)
            hex_colors.add(hex_color.lower())
        return list(hex_colors)
