# Import and print the logo from art.py when the program starts.
import art
print(art.logo)

#   starting field values
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = "encode"

# Caesar function. Encodes or Decodes
def caesar(original_text, shift):

    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter # Prints the space or symbol as is
        else:
            total_shift = alphabet.index(letter) + shift # Finds the total shift amount based on index
            total_shift %= len(alphabet)
            cipher_text += alphabet[total_shift] # Input shifted character
    print(f"Here is the {direction}d result: {cipher_text}")

#   Repeat until direction is invalid
while direction == "encode" or direction == "decode":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == "decode": # Switch directions based on Decode
            shift *= -1
            caesar(text, shift)
        else:
            caesar(text, shift)