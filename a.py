import string

with open("enc", "r") as enc_file:
    encrypted = enc_file.read()

valid_characters = string.ascii_lowercase + string.digits
key = 't'  # key comes here

if key not in valid_characters:
    print("Invalid key. Please provide a single character from 'a' to 'z' or '0' to '9'.")
else:
    decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in encrypted])
    print(decrypted)
