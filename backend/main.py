from pydoc import plain
from PIL import Image
import numpy as np
import os

PATH=os.path.join(os.getcwd(),'backend\\assets\\test1.jpg')

#get the pixel array of the image
def getImagePixels(path):
    '''
    @param path: path of the image
    returns: flattened pixel array of the image, width and height of the image
    '''
    im=Image.open(path)
    width,height=im.size
    pixel_array=list(im.getdata())
    return [x for pixel in pixel_array for x in pixel],width,height

#convert the pixel array to an image
def getImageFromPixels(pixels,width,height):
    '''
    @param pixels: flattened pixel array of the image
    @param width: width of the image
    @param height: height of the image
    returns: converted image from the pixel array
    '''
    arr=np.array(pixels,dtype=np.uint8)
    image_arr=arr.reshape((height,width,3))
    img=Image.fromarray(image_arr)
    return img

#normalize the pixel array by converting all pixels to even numbers
def normalizeImage(pixels):
    '''
    @param pixels: flattened pixel array of the image
    returns: normalized pixel array of the image
    '''
    new_arr=list()
    for pixel in pixels:
        if pixel%2:
            new_arr.append(pixel-1)
        else:
            new_arr.append(pixel)
    return new_arr

#encrypt via ceaser cipher
def encrypt(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i]==" ":
            ciphertext+=" "
            continue
        ciphertext += chr(((ord(plaintext[i])-ord('a')) + key) % 26 + ord('a'))
    return ciphertext

#decrypt via cease cipher
def decrypt(ciphertext, key):
    nkey = 26 - key
    plaintext = ''
    for i in range(len(ciphertext)):
        if ciphertext[i]==" ":
            plaintext+=" "
            continue
        plaintext += chr(((ord(ciphertext[i])-ord('a')) + nkey) % 26 + ord('a'))
    return plaintext

#get binary representation of the message
def getBinary(text):
    return ''.join(bin(ord(c)).replace('b','').zfill(8) for c in text)

#get text representation of the binary
def getText(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

# encode the message to an image
def encode(image_path,message,key):
    pixels,width,height=getImagePixels(image_path)
    normalizedPixels=normalizeImage(pixels)
    ciphertext=encrypt(message,key)
    binary=getBinary(ciphertext)
    for i,bit in enumerate(binary):
        normalizedPixels[i]+=int(bit)
    print("normalized  ",normalizedPixels[:100])
    # print("encoded  ",binary)
    img=getImageFromPixels(normalizedPixels,width,height)
    # pixel_array=list(img.getdata())
    # print("pixelarray  ",pixel_array[:33])
    # print("flat  ",[x for pixel in pixel_array for x in pixel][:100])
    return img

#decode the message from an image
def decode(image_path,key):
    pixels,width,height=getImagePixels(image_path)
    print("decoded  ",pixels[:100])
    binary=''
    for i in range(len(pixels)):
        if pixels[i]%2:
            binary+=str(1)
        else:
            binary+=str(0)
    message=getText(binary)
    # print(message[:100])
    # print("decoded  ",binary[:88])
    plaintext=decrypt(message,key)
    return plaintext


    

# x,width,height=getImagePixels(PATH)
# z=normalizeImage(x)
# y=getImageFromPixels(z,width,height)
# y.save("new.jpg")
# for c in "hello world":
#     print(c,bin(ord(c)))
# a=getBinary("hello world.")
# b=getText("011010010110011001101101011011010111000000100000011110000111000001110011011011010110010101100011")
# # print(a)
# print(b)

x=encode(PATH,"hello world",1)
x.save("new.jpg")

y=decode("new.jpg",1)
# print(y[:100])
