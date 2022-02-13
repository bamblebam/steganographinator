# Steganographinator


## What is Steganography?
* Steganography is the art of hiding a message inside another message. In our case, we will hide a text message inside an image. 
* An image will most probably go unnotified, most of the people will not suspect a message hidden inside of an image.

## Objective : 
* To provide a WebPage which will allow you to upload an Image and Enter a Plain-Text Message associated with it while assigning a specific key value to it.
* It will also allow you to extract the original text from the image while decoding the image provided you enter the correct key value associated with it.

## File Types supported: 
**Images with extension:- .jpeg, .jpg and .png**

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

## To Run the project on localhost
```
1. git clone https://github.com/rishabh547/steganographinator.git
2. cd .\steganographinator\
3. cd backend
4. Then do streamlit run main.py
5. You can now see the project runnning at localhost:http://127.0.0.1:8000/
```
## Short Demo Video

https://user-images.githubusercontent.com/59617133/153758689-58590a61-d7a2-4143-8400-92c192ce695a.mp4



## UI Screen

### Part-1
![image](https://user-images.githubusercontent.com/59617133/153759192-1540700a-d501-4248-aed9-49cf1340f07b.png)
</br>

### Part-2
![image](https://user-images.githubusercontent.com/59617133/153759238-b9cfd79e-9681-4524-adfa-1c5cb1fb89b1.png)

</br>

### Part-3

![image](https://user-images.githubusercontent.com/59617133/153759252-4bbde8b5-27b3-4fbd-9c14-3fcab3a8786e.png)




## Contributors
 * Burhanuddin Rangwala - 1911109
 * Rishabh Kothari - 1911110
 * Shrikant Sahu - 1911113



![made-with-streamlit (1)](https://user-images.githubusercontent.com/59617133/153754448-c006c061-4c0c-49ff-93c2-95605768b066.svg)
