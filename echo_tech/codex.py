from echo_tech.cryptography import encrypt,decrypt
import cv2
import numpy as np
import types

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