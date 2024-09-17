# Function to encrypt text using Caesar cipher
#from operator import truediv


def caesar_encrypt(plaintext, shift):
    result = ""

    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result


# Function to decrypt text using Caesar cipher
def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)


# Main program
def main():
    while True:
        mode = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid mode selected. Please choose 'e' or 'd'.")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if mode == 'e':
        print("Encrypted message:", caesar_encrypt(message, shift))
    elif mode == 'd':
        print("Decrypted message:", caesar_decrypt(message, shift))


if __name__ == "__main__":
    main()