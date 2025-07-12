from Crypto.Cipher import AES
import base64

# Raw key as provided in the Java code (32 bytes for AES-256)
key_bytes = bytes([
    56, 50, 97, 100, 52, 50, 99, 50,
    102, 100, 101, 56, 55, 52, 99, 53,
    54, 101, 101, 50, 49, 52, 48, 55,
    101, 57, 48, 57, 48, 52, 97, 97
])

# Base64-encoded AES-encrypted string from the malware
b64_ciphertext = "R2qBFRx0KAZceVi+MWP6FGGs8MMoJRV5M3KY/GBiOn8="

# Decode the base64 string
ciphertext = base64.b64decode(b64_ciphertext)

# Create AES cipher in ECB mode
cipher = AES.new(key_bytes, AES.MODE_ECB)

# Decrypt and decode the plaintext
plaintext = cipher.decrypt(ciphertext)

# Print the output, stripping padding characters
print("[*] Decrypted output: ", plaintext.decode('utf-8', errors='replace').strip())
