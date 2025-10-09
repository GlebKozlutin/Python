# implemantation Caesar Encyption

ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]



# this funtion do encryption
def encrypt()->str:
    klarText=input("please enter Text to be encrypted:")
    key=input("please enter encrypted Key:")
    return "it is encrypted from " + klarText + "and Key:" + key

def decode()->str:
    cypherText=input("\nplease enter Text to be DECRYPTED!!:")
    key=input("please enter DEXRYPTION KEY!!:")
    return "it is DECRYPTED from " + cypherText + " and Key:" + key




def main():
    result=""
    print("hello, i am caesar enc and dec supp")
    userChoice=input("if you want decrypt press d or encrypt press e:")

    if userChoice=="e":
        result=encrypt()
    elif userChoice=="d":
        result=decode()
    else:
        result="you must enter only e or d"

    print(result)


if __name__ == "__main__":
    main()