#import pyperclip

def caesartranslate(message, key, mode):


    # the string to be encrypted/decrypted
    #message = 'This is my secret message.'

    # the encryption/decryption key
    

    # tells the program to encrypt or decrypt
    #mode = 'encrypt' # set to 'encrypt' or 'decrypt'

    # every possible symbol that can be encrypted
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # stores the encrypted/decrypted form of the message
    translated = []

    # capitalize the string in message
    #message = message.upper()

    # run the encryption/decryption code on each symbol in the message string
    for symbol in message:

        # get the encrypted (or decrypted) number for this symbol
            #num = LETTERS.find(symbol.upper()) # get the number of the symbol
            
            if mode == 'encrypt':
                #print symbol
                num = symbol + key

            elif mode == 'decrypt':
                num = symbol - key
                #print symbol

            # handle the wrap-around if num is larger than the length of
            # LETTERS or less than 0
            if num >= 256:
                
                num = num - 256
            elif num < 0:
                
                num = num + 256

            # add encrypted/decrypted number's symbol at the end of translated
            translated.append(chr(num))
            #translated = translated + LETTERS[num]

            # just add the symbol without encrypting/decrypting
            


        
            
    # print the encrypted/decrypted string to the screen
    return ''.join(translated)

    # copy the encrypted/decrypted string to the clipboard
    #pyperclip.copy(translated)
