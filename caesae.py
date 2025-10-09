#Start - Caesarkryptographie in Python
 
 
#Variables and Lists
Alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
###Function ask user for Key and return it as int
def getKey()->int:                              
    key = int(input("Enter the key: "))                                         #Input key as string and convert to int
    return key                                                                  #return key as int
 
 
 
###Function to encrypt
def encrypt()->str:
    result = ""
    klartext = input("Enter the text you want to encrypt:")                     #Input text as string klartext= user enter text
    key = getKey()                                                              #Get key from function getKey
 
    for char in klartext:                                                       #We find position of each character in the alphabet array | when char is "J" then alphabet_index is 9
        alphabet_index = Alphabet.index(char)                                   #We add the key to the position of the character
        newcharindex = alphabet_index + key                                     #alphabet_index + key = newcharindex || index for j = 9 +key(userinput) = newcharindex
 
        encryptedchar_index = newcharindex % len(Alphabet)                      #We use modulo to make sure we stay in the bounds of the alphabet array
        result += Alphabet[encryptedchar_index]                                 #We return the result += stands for result = result + Alphabet[encryptedchar_index]    
 
    return result
 
 
###Function to decrypt
def decode()->str:
    result = ""
    encrypttext = input("Enter the text you want to decrypt:")
    key = getKey()
 
    for char in encrypttext:                                                    #We find position of each character in the alphabet array | when char is "J" then alphabet_index is 9
        alphabet_index = Alphabet.index(char)                                   #We add the key to the position of the character
        newcharindex = alphabet_index - key                                     #alphabet_index - key = newcharindex || index for j = 9 -key(userinput) = newcharindex
 
        encryptedchar_index = newcharindex % len(Alphabet)                      #We use modulo to make sure we stay in the bounds of the alphabet array
        result += Alphabet[encryptedchar_index]                                 #We return the result += stands for result = result + Alphabet[encryptedchar_index]    
 
    return result
 
 
 
 
#Main Programm Funktion
def main():
    result = ""
    print("Hello, my name is Caesar, a enc and dec app!")
    userchoice = input("If u want to decrypt press d or if u want to encrypt press e:")
 
 
    if userchoice == "e":
        result = encrypt()
    elif userchoice == "d":
        result = decode()
    else:
        print("Wrong input.")
        main()
    print(result)
 
 
 
#Programm start
if __name__ == "__main__":
    main()
 
 
#End - Caesarkryptographie in Python