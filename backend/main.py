import streamlit as st
from PIL import Image
import os
from utils import *

st.set_page_config(layout="wide")
st.title("Steganography")
col1,col2=st.columns(2)

PATH=os.path.join(os.getcwd(),'assets\\enc_img.png')

with col1:
    st.header("Encode Image")
    uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg','jpg'],key="file1")
    key=st.number_input("Enter Key",0,25,5,key="encKey")
    msg=st.text_area("Enter Message","Hello World.")
    if uploaded_file is not None and msg and key:
        img=Image.open(uploaded_file).convert('RGB')
        enc_img=encode(img,msg,key)
        enc_img.save("assets/enc_img.png")
        st.write("Encoded Image")
        st.image(enc_img,use_column_width=True)
        with open(PATH,"rb") as file:    
            st.download_button("Download",file,mime="image/png")

        
with col2:
    st.header("Decode Image")
    uploaded_file = st.file_uploader("Upload Files",type=['png'],key="file2")
    key=st.number_input("Enter Key",0,25,5,key="decKey")
    if uploaded_file is not None and key:
        img=Image.open(uploaded_file).convert('RGB')
        dec_text=decode(img,key)
        st.write("Decoded Text: ")
        st.write(dec_text)