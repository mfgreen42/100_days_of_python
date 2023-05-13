alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 
            'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
end_game = False
#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(text, shift):
    while end_game:
        if direction == "encode":
            new_text = ""
            for letter in text:
                position = alphabet.index(letter)
                new_position = position + shift
                new_text += alphabet[new_position]
        print(f"The encoded text is {new_text}")
        go_again = input("Do you want to go again? y or n")
        if go_again == "n":
                go_again == True
        elif direction == "decode":
            new_text = ""
            for letter in text:
                position = alphabet.index(letter)
                new_position = position - shift
                new_text += alphabet[new_position]
        print(f"The decoded text is {new_text}")
        go_again = input("Do you want to go again? y or n")
        if go_again == "n":
            go_again == True

caesar(text, shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.