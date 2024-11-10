import base64

# Combined Base64 string from the .rdata section
encoded_string = (
    "cQoFRQErX1YAVw1zVQdFUSxfAQNRBXUNAxBSe15QCVRVJ1pQEwd/WFBUAlElCFBFUnlaB1ULByRdBEFdfVtWVA=="
)

# Decode from Base64 to get the original binary data
decoded_data = base64.b64decode(encoded_string)
print(decoded_data)


# Assuming "FlareOn2024bad" is the key
key = "FlareOn2024"
key_bytes = key.encode()

# XOR Decrypt with key
decrypted_data = bytearray()
for i in range(len(decoded_data)):
    decrypted_data.append(decoded_data[i] ^ key_bytes[i % len(key_bytes)])

# Print the result as a UTF-8 string (if it's readable text) or as raw bytes
try:
    print(decrypted_data.decode('utf-8'))
except UnicodeDecodeError:
    print("Decrypted data (raw bytes):", decrypted_data)

# ------------------------------------------------------------------------------------------------

# import base64

# # Hexadecimal checksum provided
# hex_checksum = "7fd7dd1d0e959f74c133c13abb740b9faa61ab06bd0ecd177645e93b1e3825dd"

# # Decode the checksum from hexadecimal to bytes
# decoded_checksum = bytes.fromhex(hex_checksum)

# # Replace `xor_table` with actual bytes extracted from the binary's XOR table
# xor_table = [
#     0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE, 0xF0,
#     0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x70, 0x80,
#     0x90, 0xAB, 0xCD, 0xEF, 0xFE, 0xDC, 0xBA, 0x98,
#     0x76, 0x54, 0x32, 0x10, 0xFF, 0xEE, 0xDD, 0xCC
# ]

# # Apply the XOR transformation using the table
# xor_transformed = bytearray()
# for i in range(len(decoded_checksum)):
#     xor_transformed.append(decoded_checksum[i] ^ xor_table[i % len(xor_table)])

# # Base64 encode the result
# base64_encoded_result = base64.b64encode(xor_transformed).decode()

# # Output the Base64 encoded result
# print("Base64 Encoded Result:", base64_encoded_result)
