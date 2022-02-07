import streamlit as st
from PIL import Image
from io import BytesIO
import base64
from utils import *

st.set_page_config(layout="wide")
st.title("Steganography")
col1,col2=st.columns(2)

with col1:
    st.header("Encode Image")
    uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'],key="file1")
    msg=st.text_input("Enter Message","Hello World.")
    key=st.number_input("Enter Key",0,25,5)
    if uploaded_file is not None and msg and key:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)
        img=Image.open(uploaded_file)
        enc_img=encode(img,msg,key)
        enc_img.save("enc_img.png")
        st.write("Encoded Image")
        st.image(enc_img,use_column_width=True)
        with open("enc_image.png"):    
            st.download_button("Download","enc_img.png",mime="image/png")

        
with col2:
    st.header("Decode Image")
    uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg'],key="file2")
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)
        img=Image.open(uploaded_file)
        dec_text=decode(img,1)
        st.write("Decoded Text",dec_text)
        # st.image(enc_img,use_column_width=True)
        # st.download_button("Download",enc_img)