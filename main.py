from art import logo


def caesar(text, shift, type):
    if type == "decode":
        shift *= -1
    caesar_text = ""
    for letter in text:
        if letter in numbers_symbols:
            i = numbers_symbols.index(letter)
            caesar_text += numbers_symbols[i]
            continue
        i = alphabet.index(letter)
        letter = alphabet[(i + shift) % len(alphabet)]
        caesar_text += letter
    return caesar_text


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
numbers_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*',
                   '(', ')', '-', '_', '+', '=', '[', '{', '}', ']', '|', ';', ':', '"', '<', ',', '.', '>',
                   '?', '/', ' ']

print(logo)
print("\nHello welcome in Ceaser cipher maker.")

prev_text = ""
while True:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt (if you want to decode previous"
                      " encrypt message just type p_r_e_v: ")

    if direction == "p_r_e_v":
        prev_text = caesar(prev_text, shift, "decode")
        print(prev_text)
        start_stop = input("\nDo you want to run this program again (type yes/no): ")
        if start_stop == "no":
            print("Thank you for use my program. See you next time.")
            break


    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if direction == "encode":
        prev_text = caesar(text, shift, direction)
        print(f"Your encrypted message is: {prev_text}")
    elif direction == "decode":
        prev_text = caesar(text, shift, direction)
        print(f"Message {text} after decryption is: {prev_text}")
    else:
        print("Wrong input, program end.")
        break

    start_stop = input("Do you want to run this program again (type yes/no): ")
    if start_stop == "no":
        print("Thank you for use my program. See you next time.")
        break
