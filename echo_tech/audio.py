
# We will use wave package available in native Python installation to read and write .wav audio file
from echo_tech.cryptography import decrypt,encrypt
import wave

def encode_audio():
    # enter the audio path
    audio_path=input('Please Enter audio path ')
    # read wave audio file
    song = wave.open(audio_path, mode='rb')
    # Read frames and convert to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    # The "secret" text message
    text_msg=input('Please Enter you text massege ')
    encrypted_msg =encrypt(text_msg) 
    # Append dummy data to fill out rest of the bytes. Receiver shall detect and remove these characters.
    encrypted_msg = encrypted_msg + '###'
    # Convert text to bit array
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in encrypted_msg])))

    # Replace LSB of each byte of the audio data by one bit from the text bit array
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
        
    # Get the modified bytes
    frame_modified = bytes(frame_bytes)
    # Write bytes to a new wave audio file
    new_name = input('Enter the new name of the audio : ')
    with wave.open(new_name+ '.wav', 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)
    song.close()   
   
def decode_audio():
    # enter the audio path
    audio_path=input('Please Enter audio path ')
    song = wave.open(audio_path, mode='rb')
    # Convert audio to byte array
    frame_bytes = bytearray(list(song.readframes(song.getnframes())))
    # Extract the LSB of each byte
    """
     frame
       |
     bytes
   /||||||\
     bits (go through the last one)
    """
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    # Convert byte array back to string
    string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
    # Cut off at the filler characters
    decoded = string.split("###")[0]
    # Print the extracted text
    decrypted_msg=decrypt(decoded)
    # print("Sucessfully decoded: "+ decrypted_msg)
    song.close()
    return decrypted_msg

def main():
    a = input("Welcome to our Steganography App ^.^ !! ❤️❤️❤️\n \n Please press the number of the task needed \n \n If you want to hide a message kindly press #1 \n \n If you want to reveal the hidden message kindly press #2 \n \n Option Number: ")
    userinput = int(a)
    if (userinput == 1):
        print("\n Encoding..")
        encode_audio()
    elif (userinput == 2):
        print("\n Decoding..")
        print("Decoded message is : " + decode_audio())
    else:
        raise Exception("Please try again")   

main()

