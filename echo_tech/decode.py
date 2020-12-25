from echo_tech.codex import *


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
    print('the original image is as shown below: ')
    resized_image = cv2.resize(image, (500,500)) 
    cv2_imshow(resized_image)

    
    data = input('Enter your secret message ^.^')
    if (len(data) == 0 ):
        raise ValueError ('there is no message ,, sorry  !!')

    file_name = input('Enter the name of the new image(with the extention): ')
    encode_image = encode(image, data)
    cv2.imwrite(file_name, encode_image)





       

        

    
    