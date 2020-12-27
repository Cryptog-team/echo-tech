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
    encrypted = ''
    data = data.lower()
    for char in data:
        if char == " " :
              encrypted += " "
              continue
        if char == "," or char == "." or char == "#" or char == ";" or char == "&":
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
    decrypted = ''
    encryptedMsg = encryptedMsg.lower()
    for char in encryptedMsg:
        if char == " " :
              decrypted += " "
              continue
        if char == "," or char == "." or char == "#" or char == ";" or char == "&":
           continue
        index = alphabet.index(char)
        shifted_text = (index - key) % 26
        decrypted += alphabet[shifted_text]
    return  decrypted