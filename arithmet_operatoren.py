strompreis = 0.4

verbrauch_tv = 3*1*3*365
verbrauch_herd = 4*2*2*52
verbrauch_router = 2*4*365
verbrauch_heizung = 8*20*170

gesamtverbrauch = verbrauch_herd+verbrauch_heizung+verbrauch_router+verbrauch_tv

gesamtkosten = strompreis * gesamtverbrauch

print(f"Gesamtkosten des Haushaltes im Jahr beträgt {gesamtkosten:.2f}")
print(10/2)
print("Das Ergebnis lautet ",gesamtkosten)
print(f"{10/2} ich kann auch direkt {gesamtkosten} {strompreis/gesamtverbrauch} Euro")
print("Das Ergebnis lautet" + str(gesamtkosten) + " Euro")
