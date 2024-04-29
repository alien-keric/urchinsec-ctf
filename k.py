def decrypt_message(encrypted, key):
    return ''.join([chr(ord(x) ^ ord(key)) for x in encrypted])

def try_decrypt(file_name):
    with open(file_name, "r") as enc:
        encrypted = enc.read().strip()

    for char in range(ord('a'), ord('z')+1):
        key = chr(char)
        decrypted = decrypt_message(encrypted, key)
        if "urchinsec{" in decrypted:  # Modify the pattern as needed
            print(f"Found correct key '{key}': {decrypted}")
            break

    for digit in range(10):
        key = str(digit)
        decrypted = decrypt_message(encrypted, key)
        if "urchinsec{" in decrypted:  # Modify the pattern as needed
            print(f"Found correct key '{key}': {decrypted}")
            break

# File to decrypt
file_name = "enc"
try_decrypt(file_name)
