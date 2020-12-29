import cv2 
import numpy as np 
import random 
from PIL import Image
  
# Encryption function 
def encrypt(): 

    # first resizing the two images in order to be the same size
    img1 = Image.open("cake.jpg")
    img1 = img1.resize((500,600),Image.ANTIALIAS)
    img1.save(fp='cake.jpg')
    img2 = Image.open("we.png")
    img2 = img2.resize((500,600),Image.ANTIALIAS)
    img2.save(fp="we.png")

    # img1 and img2 are the 
    # two input images 

    img1 = cv2.imread('cake.jpg') 
    img2 = cv2.imread('we.png') 
      
    for i in range(img2.shape[0]): 
        for j in range(img2.shape[1]): 
            for l in range(3): 
                # v1 and v2 are 8-bit pixel values 
                # of img1 and img2 respectively 
                v1 = format(img1[i][j][l], '08b') 
                v2 = format(img2[i][j][l], '08b') 
                # Taking 4 MSBs of each image 
                v3 = v1[:4] + v2[:4]  
                img1[i][j][l]= int(v3, 2) 
    cv2.imwrite('pic3in2.png', img1) 
  
      

# Driver's code 
encrypt() 




