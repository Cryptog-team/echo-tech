import cv2
import numpy as np
import types


def messege_to_binary(message):
    if type(message) == str:
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format( i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Unknown Input Type")

def encode(image, new_message):
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




def show_data(image):
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


def encode_text():

    image_name = input("Insert an image(with the extention):  ") 
    image = cv2.imread(image_name)  #transforming image into matrix of r,g,b 

    print('the shape of the image is :', image.shape)
    
    data = input('Enter your secret message ^.^')
    if (len(data) == 0 ):
        raise ValueError ('there is no message ,, sorry  !!')

    file_name = input('Enter the name of the new image(with the extention): ')
    encode_image = encode(image, data)
    cv2.imwrite(file_name, encode_image)


def decode_text():

    image_name = input("Insert an image(with the extention) you want to decode:  ") 
    image = cv2.imread(image_name)  #transforming image into matrix of r,g,b 
 
    text = show_data(image)
    return text


def Main():
    a = input("Steganography, Please press the number of the task needed \n 1.Encode \n 2.Decode \n Option Number: ")
    userinput = int(a)
    if (userinput == 1):
        print("\n Encoding..")
        encode_text()
    elif (userinput == 2):
        print("\n Decoding..")
        print("Decoded message is" + decode_text())
    else:
        raise Exception("Please try again")

Main()