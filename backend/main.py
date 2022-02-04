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

x,width,height=getImagePixels(PATH)
y=getImageFromPixels(x,width,height)
y.save("new.jpg")