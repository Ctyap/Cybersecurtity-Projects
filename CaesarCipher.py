"""

In cryptography, a Caesar cipher, also known as Caesar's cipher,
the shift cipher, Caesar's code or Caesar shift, is one of the
simplest and most widely known encryption techniques. It is a type
 of substitution cipher in which each letter in the plaintext is replaced
 by a letter some fixed number of positions down the alphabet. 

"""
#Constant that stores int 26 reminding that the key used in cipher should be within this range.
KEY_RANGE = 26

def promptUser():
    while True:
        userChoice = input("Would you like to encrypt or decrypt a message?").lower()
        
        if userChoice in ["encrypt", "e", "decrypt", "d"]:
            return userChoice[0]
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".\n')

    
def getMessage():
    return input("Enter your message: ")

def getKey():
    key = 0
    
    while True:
        key = int(input("Enter a key from 1-25: "))
        if (key in range(1,26)):
            return key


def CaesarCipher(userChoice, message, key):
    if userChoice == "d":
        key = -key
    translateMessage= ""
    
    for char in message:
        if char.isalpha():
            #num variable holds integer ordinal value of the letter
            num = ord(char)
            num += key
            
       
            if char.isupper():
                #Specials cases thatallow the ciphertext to start at begining of alphabet
                if num > ord("Z"):
                    num -= 26
                elif num < ord("A"):
                    num += 26
            elif char.islower():
                if num > ord("z"):
                    num -= 26
                elif num < ord("a"):
                    num += 26
            
            translateMessage += chr(num)
        else:
            #Meaning Numbers, punctuation marks, and everything else will stay in their original form
            translateMessage += char
            
    return translateMessage


if __name__ == "__main__":
    
    while True:
        userChoice = promptUser()
        userMessage = getMessage()
        userKey = getKey()
        
        print("\nYour translated Message is: ")
        print(CaesarCipher(userChoice, userMessage, userKey))
        userQuit = input("\nIf want to exit program type: quit or q").lower()
        
        if userQuit[0] == 'q':
            print("Program ended.")
            break
    
