def encrypt(text, shift):
    """Encrypt the text using Caesar Cipher with the given shift value."""
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift character and handle wrap-around using modulo
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += encrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    """Decrypt the text using Caesar Cipher with the given shift value."""
    return encrypt(text, -shift)  # Decryption is simply encryption with a negative shift

def main():
    print("Caesar Cipher Encryption/Decryption")
    
    while True:
        # Prompt user for input
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        
        if choice == 'e':
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted message: {encrypted_text}")
        
        elif choice == 'd':
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")
        
        elif choice == 'q':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
