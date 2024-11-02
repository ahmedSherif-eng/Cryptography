import encryption
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
if __name__ == "__main__":
    print( encryption.encrypt("a", "F46E986435465354"))

pass



# key = bytes.fromhex("F46E986435465354")
#
# # Create a Lab2_DES cipher object
# cipher = Lab2_DES.new(key, Lab2_DES.MODE_ECB)
#
# # Data to encrypt (ASCII 'a' -> hex 0x61, padded to 8 bytes as required by Lab2_DES)
# data = b'a'  # Character 'a' in bytes
# padded_data = pad(data, Lab2_DES.block_size)  # Pad to 8 bytes for Lab2_DES
#
# # Encrypt the data
# ciphertext = cipher.encrypt(padded_data)
#
# # Print the encrypted output in hexadecimal
# print("Ciphertext (hex):", ciphertext.hex())