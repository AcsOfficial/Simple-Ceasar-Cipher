def encode_message(string, shift):
    enciphered = ""
            
    for char in string:
        if char.isalpha():
            if char.isupper():
                enciphered += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                enciphered += chr((ord(char) - 97 + shift) % 26 + 97)
        elif char.isdigit():
            enciphered += chr((ord(char) - 48 + shift) % 10 + 48)
        else:
            enciphered += char
    
    return enciphered

def decode_message(string, shift):
    deciphered = ""
        
    for char in string:
        if char.isalpha():
            if char.isupper():
                deciphered += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                deciphered += chr((ord(char) - 97 - shift) % 26 + 97)
        elif char.isdigit():
            deciphered += chr((ord(char) - 48 - shift) % 10 + 48)
        else:
            deciphered += char
        
    return deciphered

option = input("Hello! Do you want to encode or decode a Caesar cipher? ").lower()

if "encode" in option:
    print("-- Encode the message --")
    word = input("Enter a message you want to encode: ")
    x = int(input("Enter the key value: "))
    encoded_message = encode_message(word, x)
    print("The encoded message using Caesar cipher is:", encoded_message)
    
elif "decode" in option:
    print("-- Decode the message --")
    word = input("Enter a message you want to decode: ")
    x = int(input("Enter the key value: "))
    decoded_message = decode_message(word, x)
    print("The decoded message using Caesar cipher is:", decoded_message)
    
else:
    print("Incorrect option. Please enter 'encode' or 'decode'.")
