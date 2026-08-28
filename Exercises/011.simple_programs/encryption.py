import random
import string

# string of random chars
chars = string.punctuation + string.digits + string.ascii_letters + " "
chars_list = list(chars)

key = chars_list.copy()
random.shuffle(key)
# encryption
plain_text = input("Add text to encrypt: ")

encrypted_message = ""
decrypted_message = ""


# Encrypt
for char in plain_text:
    index = chars_list.index(char)
    encrypted_message += key[index]

print(f"Your encypted message is : {encrypted_message}")


text_to_decrypt = input("Enter text to decrypt: ")

# Decrypt
for char in text_to_decrypt:
    index = key.index(char)
    decrypted_message += chars_list[index]


print(f"Your decrypted message is : {decrypted_message}")
