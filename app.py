# Third-party imports
import streamlit as st

# Local application imports
from utils import ImageHandler, ColorExtractor

# Configure and set up the page
st.set_page_config(page_title="HEX Color Scanner", layout="centered")
st.title("HEX Color Scanner")
st.write("Upload an image to extract and display HEX color codes.")

# Add sidebar for configuration
with st.sidebar:
    st.header("Settings")
    num_colors = st.slider("Number of colors to extract", min_value=1, max_value=50, value=20, step=1)

uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Process the image
    handler = ImageHandler(uploaded_file)
    
    # Display uploaded image
    st.image(handler.show(), caption="Uploaded image", use_container_width=True)
    
    # Extract colors
    pixels = handler.get_group_important_pixels(num_colors=num_colors)
    extractor = ColorExtractor(pixels)
    hex_colors = extractor.extract_unique_hex()
    st.success(f"Found {len(hex_colors)} unique HEX color codes.")
    st.markdown("""
        <style>
        .color-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
            justify-content: center;
        }
        .color-box {
            display: inline-block;
            margin: 5px;
            text-align: center;
            width: 90px;
        }
        .color-swatch {
            width: 80px;
            height: 80px;
            border-radius: 10px;
            margin-bottom: 5px;
            border: 2px solid #ccc;
            transition: transform 0.2s;
        }
        .color-code {
            font-size: 14px;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)

    # Display colors in a grid layout
    st.markdown('<div class="color-grid">', unsafe_allow_html=True)
    
    # Use columns for better display
    cols = st.columns(5)
    
    # Display each color with copy button functionality
    for i, color in enumerate(hex_colors):
        col_idx = i % 5
        with cols[col_idx]:
            st.markdown(f'<div class="color-box">', unsafe_allow_html=True)
            st.markdown(f'<div class="color-swatch" style="background-color: {color};"></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="color-code">{color}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            if st.button(f"Copy", key=f"copy_{i}"):
                st.session_state[f"copied_{i}"] = True
                st.toast(f"Copied: {color}")
                try:
                    import pyperclip
                    pyperclip.copy(color)
                except ImportError:
                    st.warning("Please install pyperclip for clipboard functionality: pip install pyperclip")
    
    st.markdown('</div>', unsafe_allow_html=True)
