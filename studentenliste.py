def kekse(n):
    """Gibt einen String mit n Keksen (🍪) zurück."""
    return '🍪' * n

while True:
    n = input("Wie viele Kekse möchtest du haben? (0 zum Beenden) ")

    try:
        n = int(n)
        if n == 0:
            print("Okay, keine Kekse mehr! Cookie Monster Traurig 😭 ")
            break
        elif n < 0:
            print("Das Cookie Monste Wäre enttäuscht! ")
        else:
            print(kekse(n))
    except ValueError:
        print("Bitte gib eine gültige Zahl ein")
