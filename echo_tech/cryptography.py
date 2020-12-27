# from cryptography.fernet import Fernet


# # Generating the key and writing it to a file
# def genwrite_key():
#     key = Fernet.generate_key()
#     with open("pass.key", "wb") as key_file:
#         key_file.write(key)
# print(genwrite_key())

# def call_key():
#                   return open("pass.key", "rb").read()


# key = call_key()
# slogan = "Hello!! Welcome to AIM!!".encode()
# a = Fernet(key)
# coded_slogan = a.encrypt(slogan)
# print(coded_slogan)

# key = call_key()
# b = Fernet(key)
# decoded_slogan = b.decrypt(coded_slogan)
# print(decoded_slogan)



####################################################



