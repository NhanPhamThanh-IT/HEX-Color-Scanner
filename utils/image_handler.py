from PIL import Image

class ImageHandler:
    def __init__(self, image_path: str):
        self.image = Image.open(image_path).convert("RGB")

    def get_pixels(self):
        """
        Returns the pixel data of the image as a list of RGB tuples.
        """
        return list(self.image.getdata())
    
    def show(self):
        """
        Displays the image.
        """
        return self.image