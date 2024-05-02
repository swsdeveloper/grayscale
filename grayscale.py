# Convert a photo into grayscale (via Python library "pillow" (PIL)
# - installed v10.3.0)

import streamlit as st
from PIL import Image   # Image is a type

st.set_page_config(layout="wide")

st.title("Convert Image to Grayscale")

options = st.radio("Select:", ["Take a photo", "Upload an Image"], key='options',
                   index=None, label_visibility='visible')  # Start with neither option selected

st.write('\n')  # skip a line

original_image = None

match options:
    case "Take a photo":
        with st.expander("Start Camera"):
            camera_image = st.camera_input("Camera")         # get streamlit UploadedFile type
            if camera_image:
                original_image = camera_image

    case "Upload an Image":
        uploaded_image = st.file_uploader("Select an Image",  # get streamlit Image type
                                         type=['bmp', 'jpeg', 'jpg', 'png', 'webp'])    # *.heic not supported
        if uploaded_image:
            original_image = uploaded_image

# Prevent the next lines from running until we have an image:
if original_image:
    img = Image.open(original_image)
    gray_img = img.convert("L")     # convert the pillow image to grayscale
    st.image(img)                   # render the color image in the webpage
    st.image(gray_img)              # render the grayscale image on the webpage
