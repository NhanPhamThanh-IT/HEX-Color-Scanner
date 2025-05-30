# Standard library imports

# Third-party imports
import streamlit as st

# Local application imports
from utils import ImageHandler, ColorExtractor, ColorPlotter

# Configure and set up the page
st.set_page_config(page_title="HEX Color Extractor", layout="centered")
st.title("🎨 HEX Color Extractor (OOP)")
st.write("Upload an image to extract and display HEX color codes.")

uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    handler = ImageHandler(uploaded_file)
    st.image(handler.show(), caption="Uploaded image", use_container_width=True)

    pixels = handler.get_pixels()
    extractor = ColorExtractor(pixels)
    hex_colors = extractor.extract_unique_hex()
    st.success(f"Found {len(hex_colors)} unique HEX color codes.")
    
    plotter = ColorPlotter(hex_colors)
    st.pyplot(plotter.plot())

    with st.expander("📋 View HEX color list"):
        st.code("\n".join(hex_colors))
