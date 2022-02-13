from urllib import request
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import os
from utils import *

#Function to load the url
def load_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# load animation
lottie_coding = load_url("https://assets6.lottiefiles.com/packages/lf20_cgjrfdzx.json")
st.set_page_config(layout="wide")



col_1,col_2 = st.columns(2)
col1,col2=st.columns(2)

PATH=os.path.join(os.getcwd(),'assets\\enc_img.png')
with col_1:
    st.markdown("<h1> Steganographinator</h1", unsafe_allow_html=True)
    st.write(">##### _'Welcome to your One Stop Solution for Steganography!'_")
    st.write("* This is a tool to *hide your secret message* in an image. ")
    st.write("* Keep your _Secrets to yourself_, and no more compromise with your security!")
    st.write("* With _Caesar Cipher_ encyrpt images on the fly")
with col_2:
    # st.title("Steganography")
    st_lottie(lottie_coding,width=400,height=300)
   


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
        st.subheader(dec_text)
        st.image(img,use_column_width=True)