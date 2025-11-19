def kekse(lines):
    pyramide = []

    for i in range(lines, 0, - 1):
        leerzeichen = "  " * (lines - i)
        kekse = "🍪" * (2 * i - 1)
        zeile = leerzeichen + kekse

        pyramide.append(zeile)
        print(zeile)

    return pyramide


def main():
    n = int(input("Wie viele Kekse soll die Pyramide haben? "))
    pyramide_array = kekse(n)  # Funktion aufrufen und Array speichern
    print("\nPyramide als Array:")
    print(pyramide_array)  # Zeigt die Liste in der Konsole


main()
