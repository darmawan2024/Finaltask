import streamlit as st
from PIL import Image, ImageFilter

st.title("Simple Image Editor App")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Menu pilihan untuk mengedit gambar
    edit_option = st.sidebar.selectbox("Choose an edit option", ["Original", "Blur", "Rotate"])

    if edit_option == "Blur":
        blur_radius = st.slider("Select blur radius", 0, 10, 5)
        blurred_image = image.filter(ImageFilter.GaussianBlur(blur_radius))
        st.image(blurred_image, caption="Blurred Image", use_column_width=True)

    elif edit_option == "Rotate":
        rotation_angle = st.slider("Select rotation angle", -180, 180, 0)
        rotated_image = image.rotate(rotation_angle)
        st.image(rotated_image, caption="Rotated Image", use_column_width=True)

    # Jika opsi edit tidak dipilih, tampilkan gambar asli
    else:
        st.image(image, caption="Original Image", use_column_width=True)
