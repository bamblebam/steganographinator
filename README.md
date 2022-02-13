# Steganographinator

## Objective : 
* To provide a WebPage which will allow you to upload an Image and Enter a Plain-Text Message associated with it while assigning a specific key value to it.
* It will also allow you to extract the original text from the image while decoding the image provided you enter the correct key value associated with it.

## File Types supported: 
Images with extension:- .jpeg, .jpg and .png

## To run the project on localhost
```
1. git clone https://github.com/rishabh547/steganographinator.git
2. cd .\steganographinator\
3. cd backend
4. Then do streamlit run main.py
5. You can now see the project runnning at localhost:http://127.0.0.1:8000/
```

## Features:

 ### 1. Encoding
  * To allow a user to upload an image (.png,.jpeg or .jpg) and enter a plain-text along with it with a specific key value.
  * It allows user to download the image in the png format(lossless compression) which can be used while decoding.
 
 ### 2. Decoding
  * A User can extract the Original text from the same image by Entering the correct key value assocaited with it.
 
 
 #### Note: Image Uploading size has been set to Max 200 MB.
 
 ### Contributors
 * Burhanuddin Rangwala - 1911109
 * Rishabh Kothari - 1911110
 * Shrikant Sahu - 1911113