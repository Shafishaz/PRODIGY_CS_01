def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a text using the Caesar Cipher algorithm.

    :param text: The input text to encrypt or decrypt.
    :param shift: The shift value for the Caesar Cipher.
    :param mode: The mode of operation ('encrypt' or 'decrypt').
    :return: The encrypted or decrypted text.
    """
    # Ensure shift is in the range 0-25
    shift = shift % 26

    # If mode is decrypt, reverse the shift
    if mode == 'decrypt':
        shift = -shift

    result = ""

    for char in text:
        if char.isalpha():
            # Shift uppercase and lowercase characters separately
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Leave non-alphabet characters unchanged
            result += char

    return result


def main():
    # Get user input
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (0-25): "))
    mode = input("Do you want to 'encrypt' or 'decrypt' the message? ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return

    # Perform encryption or decryption
    result = caesar_cipher(text, shift, mode)
    print(f"The result is: {result}")


if __name__ == "__main__":
    main()
