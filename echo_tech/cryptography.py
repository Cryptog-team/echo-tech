
from Crypto.Cipher import AES
import binascii, os

def encrypt_AES(msg):
    msg = msg.encode('utf-8')
    key =input("Enter yout Key : ")
    if len(key) >0 and len(key) < 17 :
        key +=  "0"*(16-len(key))
    elif len(key) >16 and len(key) < 25 :
        key +=  "0"*(24-len(key))
    elif len(key) >24 and len(key) < 33 :
        key +=  "0"*(32-len(key))
    key= key.encode('utf-8')
    aesCipher = AES.new(key, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)


def decrypt_AES(encryptedMsg):
    key =input("Enter yout Key : ")
    if len(key) >0 and len(key) < 17 :
        key +=  "0"*(16-len(key))
    elif len(key) >16 and len(key) < 25 :
        key +=  "0"*(24-len(key))
    elif len(key) >24 and len(key) < 33 :
        key +=  "0"*(32-len(key))
    key= key.encode('utf-8')
    (ciphertext, nonce, authTag) = encryptedMsg
    aesCipher = AES.new(key, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    plaintext = plaintext.decode('utf-8')
    return plaintext


def encrypt(data):
    """
    Input:
         text to be encrypted
         key of the caesar cypher
    Output: Encrypted text
    """
    key = input("Enter the key that you and the reciever have already agreed on : ")
    key=int(key)
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols_num =['!','@','#','$','%','^','&','*','(',')','_','-','+', '=', ',', '.','/', '?', '{', '}', '[', ']',  '~' , '|', '1', '2', '3', '4', '5', '6', '7', '8', '9','10']
    encrypted = ''
    data = data.lower()
    for char in data:
        if char == " " :
              encrypted += " "
              continue
        if char in symbols_num:
            encrypted += char 
            continue
        index = alphabet.index(char)
        shifted_text = (index + key) % 26
        encrypted += alphabet[shifted_text]
    return encrypted
def decrypt(encryptedMsg):
    """
    Input:
         text to be deccrypted
         key of the caesar cypher
    Output: deccrypted text
    """
    key = input("Enter the key that you and the sender have already agreed on : ")
    key = int(key)
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols_num =['!','@','#','$','%','^','&','*','(',')','_','-','+', '=', ',', '.','/', '?', '{', '}', '[', ']',  '~' , '|', '1', '2', '3', '4', '5', '6', '7', '8', '9','10']
    decrypted = ''
    encryptedMsg = encryptedMsg.lower()
    for char in encryptedMsg:
        if char == " " :
              decrypted += " "
              continue
        if char in symbols_num :
            decrypted += char 
            continue
        index = alphabet.index(char)
        shifted_text = (index - key) % 26
        decrypted += alphabet[shifted_text]
    return  decrypted