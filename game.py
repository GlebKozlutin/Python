import random

print("Geben sie eine zahl Zwischen 1 bis 5 ein: ")
input_value=input()

if input_value.isdigit():
    input_value=int(input_value)
    zufallszahlgenerator=random.randint(1,5)
    if input_value==zufallszahlgenerator:
        print(" Herzlichen Glückwunsch du hast gewonnen")
    else:
        print(f"Schade sie haben verloren, die korrekte Zahl war {zufallszahlgenerator}")
else:
    print("Du hast keinen String eingegeben dass aussieht wie eine Zahl")


print("Danke dass du gespielt hast")