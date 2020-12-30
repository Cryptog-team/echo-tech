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
  
# Decryption function 
def decrypt(): 
      
    # Encrypted image 
    img = cv2.imread('pic3in2.png')  
    width = img.shape[0] 
    height = img.shape[1] 
      
    # img1 and img2 are two blank images 
    img1 = np.zeros((width, height, 3), np.uint8) 
    img2 = np.zeros((width, height, 3), np.uint8) 
      
    for i in range(width): 
        for j in range(height): 
            for l in range(3): 
                v1 = format(img[i][j][l], '08b') 
                v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
                v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
                  
                # Appending data to img1 and img2 
                img1[i][j][l]= int(v2, 2) 
                img2[i][j][l]= int(v3, 2) 
      
    # These are two images produced from 
    # the encrypted image 
    cv2.imwrite('pic2_re.png', img1) 
    cv2.imwrite('pic3_re.png', img2)



# Driver's code 
encrypt() 
decrypt()      




