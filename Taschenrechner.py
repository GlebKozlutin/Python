try:
    zahl1 = float(input("Erste Zahl: "))
    op = input("Operator (+, -, *, /): ")
    zahl2 = float(input("Zweite Zahl: "))

    if op == "+":
        ergebnis = zahl1 + zahl2
    elif op == "-":
        ergebnis = zahl1 - zahl2
    elif op == "*":
        ergebnis = zahl1 * zahl2
    elif op == "/":
        if zahl2 != 0:
            ergebnis = zahl1 / zahl2
        else:
            ergebnis = "Fehler: Division durch 0!"
    else:
        ergebnis = "Ungültiger Operator"

    print("Ergebnis:", ergebnis)

except ValueError:
    print("Ungültige Eingabe: Bitte gib nur Zahlen ein!")
