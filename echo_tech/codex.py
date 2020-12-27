from echo_tech.cryptography import encrypt,decrypt
import cv2
import numpy as np
import types
from datetime import date



today = date.today()
d1 = today.strftime("%m/%d/%Y")
def password():
    password = input ("please enter the password : ")
    if password == d1 :
        main()
        # return "correct password"
    else :
        print("incorrect password")
#####################################################

def messege_to_binary(message):
    """
    this function is mainly respossile for converting the message into binary and Vice versa
    """
    if type(message) == str:
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format( i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Unknown Input Type")

#######################################################
def encode(image, new_message):
    """
    this function will hide ur message inside the image using LSB algorithm
    """
    number_bytes = image.shape[0] * image.shape[1] * 3 // 8
    if len(new_message) > number_bytes:
        raise ValueError("You need a bigger Image or less data")
    new_message += "#####"
    data_index = 0
    binary_new_message = messege_to_binary(new_message)
    data_len = len(binary_new_message)
    for values in image:
        for pixel in values:
            r,g,b = messege_to_binary(pixel)
            # now we use the LSB method
            # remove last bit of every byte for all rgb's and then append new bit 
            # using int to convert the binary into a number again
            if data_index < data_len:
                pixel[0] = int(r[:-1] + binary_new_message[data_index], 2)
                data_index +=1
            if data_index < data_len:
                pixel[1] = int(g[:-1] + binary_new_message[data_index], 2)
                data_index +=1
            if data_index < data_len:
                pixel[2] = int(b[:-1] + binary_new_message[data_index], 2)
                data_index +=1
            if data_index >= data_len:
                break
    return image

############################################
def show_data(image):
    """
    this function is respossible for Revealing the hidden message *_* 
    """
    binary_data= ""
    for values in image:
        for pixel in values:
            # converting the r,g,b into binary format 
            r, g, b = messege_to_binary(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    all_bytes=[binary_data[i:i+8] for i in range(0,len(binary_data), 8)]
    # converting the bits into characters 
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte ,2))
        if decoded_data[-5:] == "#####":
            break
    return decoded_data[:-5]

#############################################


def encode_text():
    """
    1. Using this function, we insert the message, and the image
    2. We have used the Cipher code with special key in order to encrypt the message for more security 
    3. calling the function that will encode the encrypted message inside the image @.@
    """
    image_name = input("Insert an image(with the extention):  ") 
    image = cv2.imread(image_name)  #transforming image into matrix of r,g,b 
    print('the shape of the image is :', image.shape)
    data = input('Enter your secret message ^.^')
    if (len(data) == 0 ):
        raise ValueError ('there is no message ,, sorry  !!')
    encrypted_msg = encrypt(data)
    file_name = input('Enter the name of the new image(with the extention): ')
    encode_image = encode(image, encrypted_msg)
    cv2.imwrite(file_name, encode_image)


#################################################  


def decode_text():
    """
    1. using this function, we insert the image tat includes the hidden message
    2. We call the show_data() to return the hidden and encrypted message 
    3. We call the decrypt() to return the original message after decrypting it &.&
    """
    image_name = input("Insert an image(with the extention) you want to decode:  ") 
    image = cv2.imread(image_name)  #transforming image into matrix of r,g,b 
    text = show_data(image)
    decrypted_msg = decrypt(text) 
    return decrypted_msg


###################################################

def main():
    a = input("Welcome to our Steganography App ^.^ !! \n \n Please press the number of the task needed \n \n If you want to hide a message kindly press #1 \n \n If you want to reveal the hidden message kindly press #2 \n \n Option Number: ")
    userinput = int(a)
    if (userinput == 1):
        print("\n Encoding..")
        encode_text()
    elif (userinput == 2):
        print("\n Decoding..")
        print("Decoded message is : " + decode_text())
    else:
        raise Exception("Please try again")
# main()
password()




