# Steganographinator


## What is Steganography?
* Steganography is the art of hiding a message inside another message. In our case, we will hide a text message inside an image. 
* An image will most probably go unnotified, most of the people will not suspect a message hidden inside of an image.

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
  * To allow a user to upload an image (.png,.jpeg or .jpg) and enter a plain-text along with it select a specific key value.
  * Here , the message encryption is done using **Caesar Cipher** as a layer of security.
  * It allows user to download the image in the png format(lossless compression) which can be used while decoding.
 
 ### 2. Decoding
  * In the Decode part, upload the image suspected to contain hidden text.
  * Now enter the key value used while encoding to get the original plaintext.
  * **Remember to upload only those images that have been generated using Steganographinator, since the logic is unique to this project**.
  * Finally, The Decrypted Message will be displayed at the Decoding end. 
 
 #### Note: Image Uploading size has been set to Max 200 MB.
 
## Contributors
 * Burhanuddin Rangwala - 1911109
 * Rishabh Kothari - 1911110
 * Shrikant Sahu - 1911113
