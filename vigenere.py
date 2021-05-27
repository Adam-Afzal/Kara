


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = [] # stores the encrypted/decrypted message string

    keyIndex = 0
    

    for symbol in message: # loop through each character in message
        #num = LETTERS.find(symbol.upper())
        if mode == 'encrypt':
            num = symbol + ord(key[keyIndex])
        elif mode == 'decrypt':
            num = symbol - ord(key[keyIndex])

        if num >= 256:
            
            num = num - 256
        elif num < 0:
            
            num = num + 256

        keyIndex += 1 # move to the next letter in the key
        if keyIndex == len(key):
            keyIndex = 0

        translated.append(chr(num))


        
        

    return ''.join(translated)


# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()