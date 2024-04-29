def decrypt_message(encrypted, key):
    return ''.join([chr(ord(x) ^ ord(key)) for x in encrypted])

def check_decryption(decrypted):
    # You can modify this function to check for specific patterns or keywords
    # For example, if the decrypted message contains a known keyword or phrase
    # you can return True indicating that this might be the correct decryption.
    # Otherwise, return False.
    if "urchinsec{" in decrypted:
        return True
    return False

def try_decrypt(file_name):
    with open(file_name, "r") as enc:
        encrypted = enc.read().strip()

    for char in range(ord('a'), ord('z')+1):
        key = chr(char)
        decrypted = decrypt_message(encrypted, key)
        if check_decryption(decrypted):
            print(f"Found correct key '{key}': {decrypted}")
            break

    for digit in range(10):
        key = str(digit)
        decrypted = decrypt_message(encrypted, key)
        if check_decryption(decrypted):
            print(f"Found correct key '{key}': {decrypted}")
            break

# File to decrypt
file_name = "enc"
try_decrypt(file_name)
