import streamlit as st
from color_extractor.image_handler import ImageHandler
from color_extractor.color_extractor import ColorExtractor
from color_extractor.plotter import ColorPlotter

st.set_page_config(page_title="HEX Color Extractor", layout="centered")
st.title("🎨 HEX Color Extractor (OOP)")
st.write("Tải ảnh lên để trích xuất và hiển thị mã màu HEX.")

uploaded_file = st.file_uploader("Tải ảnh lên", type=["png", "jpg", "jpeg"])

if uploaded_file:
    handler = ImageHandler(uploaded_file)
    st.image(handler.show(), caption="Ảnh đã tải lên", use_container_width=True)

    pixels = handler.get_pixels()
    extractor = ColorExtractor(pixels)
    hex_colors = extractor.extract_unique_hex()
    st.success(f"Tìm thấy {len(hex_colors)} mã màu HEX duy nhất.")

    plotter = ColorPlotter(hex_colors)
    st.pyplot(plotter.plot())

    with st.expander("📋 Xem danh sách mã HEX"):
        st.code("\n".join(hex_colors))
