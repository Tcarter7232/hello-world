def decrypt(encrypted_text, distance):
    """
    Decrypts a Caesar cipher with the given distance.

    :param encrypted_text: The encrypted text to decrypt.
    :param distance: The distance to shift the characters.
    :return: The decrypted plaintext.
    """
    plaintext = ""
    for char in encrypted_text:
        if char.isalpha():  # Check if the character is a letter
            ascii_offset = 65 if char.isupper() else 97  # ASCII offset for uppercase or lowercase letters
            char_code = ord(char) - ascii_offset  # Convert to 0-25 index
            char_code = (char_code - distance) % 26  # Shift and wrap around
            plaintext += chr(char_code + ascii_offset)  # Convert back to character
        else:
            plaintext += char  # Non-letter characters remain unchanged
    return plaintext

# Get user input
encrypted_text = input("Enter the encrypted text: ")
distance = int(input("Enter the distance value: "))

# Decrypt and print the result
print("Plaintext:", decrypt(encrypted_text, distance))
