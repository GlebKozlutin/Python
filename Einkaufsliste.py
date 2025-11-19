from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class Produkt:
    id: int
    name: str
    preis: float


@dataclass
class WarenkorbPosition:
    produkt: Produkt
    menge: int = 1


@dataclass
class Benutzer:
    eingeloggt: bool = False
    adresse: Optional[Dict[str, str]] = None
    zahlungsmethode: Optional[Dict[str, str]] = None


PRODUKTE_DB = [
    Produkt(id=1, name="T-Shirt", preis=19.99),
    Produkt(id=2, name="Hose", preis=39.99),
    Produkt(id=3, name="Schuhe", preis=59.99),
]


def zeige_startseite() -> None:
    print("Willkommen im Online-Shop!")
    print("Du kannst nach Produkten suchen oder 'exit' eingeben, um den Shop zu verlassen.\n")


def benutzer_suchanfrage() -> str:
    return input("Suchbegriff eingeben (oder leer lassen, um alle anzuzeigen): ")


def suche_produkte(eingabe: str) -> List[Produkt]:
    if not eingabe:
        return PRODUKTE_DB
    eingabe_lower = eingabe.lower()
    return [p for p in PRODUKTE_DB if eingabe_lower in p.name.lower()]


def zeige_produkte(produkte: List[Produkt]) -> None:
    if not produkte:
        print("Keine Produkte gefunden.\n")
        return
    print("\nVerfügbare Produkte:")
    for p in produkte:
        print(f"{p.id}: {p.name} - {p.preis:.2f} €")
    print()


def benutzer_waehlt_produkt() -> bool:
    auswahl = input("Produkt-ID wählen oder Enter zum Überspringen: ")
    return auswahl.strip() != ""


def gewaehlt_produkt(eingabe_id: Optional[str] = None) -> Optional[Produkt]:
    if eingabe_id is None:
        eingabe_id = input("Bitte Produkt-ID eingeben: ")
    try:
        pid = int(eingabe_id)
    except ValueError:
        print("Ungültige ID.")
        return None
    for p in PRODUKTE_DB:
        if p.id == pid:
            return p
    print("Produkt nicht gefunden.")
    return None


def zeige_produktdetails(produkt: Produkt) -> None:
    print(f"\nDetails zu Produkt {produkt.id}:")
    print(f"Name: {produkt.name}")
    print(f"Preis: {produkt.preis:.2f} €\n")


def benutzer_klickt_in_den_warenkorb() -> bool:
    auswahl = input("'w' eingeben, um in den Warenkorb zu legen, sonst Enter: ")
    return auswahl.lower() == "w"


def zeige_warenkorb_status(warenkorb: List[WarenkorbPosition]) -> None:
    print("\nAktueller Warenkorb:")
    if not warenkorb:
        print("Warenkorb ist leer.")
    else:
        gesamt = 0.0
        for pos in warenkorb:
            summe_pos = pos.produkt.preis * pos.menge
            gesamt += summe_pos
            print(f"- {pos.produkt.name} x {pos.menge} = {summe_pos:.2f} €")
        print(f"Gesamt: {gesamt:.2f} €")
    print()


def benutzer_klickt_warenkorb() -> bool:
    auswahl = input("Warenkorb anzeigen? (j/n): ")
    return auswahl.lower() == "j"


def zeige_warenkorb(warenkorb: List[WarenkorbPosition]) -> None:
    zeige_warenkorb_status(warenkorb)


def benutzer_aendert_warenkorb() -> bool:
    auswahl = input("Warenkorb ändern? (Menge/Entfernen) (j/n): ")
    return auswahl.lower() == "j"


def aktualisiere_warenkorb(warenkorb: List[WarenkorbPosition]) -> None:
    if not warenkorb:
        print("Warenkorb ist leer, nichts zu ändern.\n")
        return

    zeige_warenkorb_status(warenkorb)
    aktion = input("Aktion: 'm' = Menge ändern, 'e' = entfernen, Enter = abbrechen: ")

    if aktion.lower() not in ("m", "e"):
        return

    pid = input("Produkt-ID im Warenkorb: ")
    try:
        pid = int(pid)
    except ValueError:
        print("Ungültige ID.")
        return

    for pos in warenkorb:
        if pos.produkt.id == pid:
            if aktion.lower() == "m":
                neue_menge = input("Neue Menge: ")
                try:
                    neue_menge = int(neue_menge)
                    if neue_menge <= 0:
                        warenkorb.remove(pos)
                    else:
                        pos.menge = neue_menge
                    print("Warenkorb aktualisiert.\n")
                except ValueError:
                    print("Ungültige Menge.\n")
            elif aktion.lower() == "e":
                warenkorb.remove(pos)
                print("Artikel entfernt.\n")
            return

    print("Produkt nicht im Warenkorb gefunden.\n")


def benutzer_klickt_zur_kasse() -> bool:
    auswahl = input("Zur Kasse gehen? (j/n): ")
    return auswahl.lower() == "j"


def benutzer_nicht_eingeloggt(benutzer: Benutzer) -> bool:
    return not benutzer.eingeloggt


def frage_nach_login_oder_registrierung() -> str:
    return input("Bereits Kunde? (l = Login, r = Registrierung): ")


def benutzer_login_oder_registrieren(benutzer: Benutzer, entscheidung: str) -> None:
    if entscheidung.lower() == "l":
        print("Login erfolgreich (Dummy).")
    else:
        print("Registrierung erfolgreich (Dummy).")
    benutzer.eingeloggt = True


def benutzer_gibt_lieferadresse_ein() -> Dict[str, str]:
    print("\nLieferadresse eingeben:")
    name = input("Name: ")
    strasse = input("Straße: ")
    stadt = input("Stadt: ")
    plz = input("PLZ: ")
    return {"name": name, "strasse": strasse, "stadt": stadt, "plz": plz}


def pruefe_adresse(adresse: Dict[str, str]) -> bool:
    return all(adresse.values())


def benutzer_waehlt_versand_option() -> str:
    print("\nVersandoptionen:")
    print("1: Standard (3–5 Tage)")
    print("2: Express (1–2 Tage)")
    auswahl = input("Versandoption wählen (1/2): ")
    return auswahl if auswahl in ("1", "2") else "1"


def berechne_versandkosten(option: str) -> float:
    if option == "2":
        return 9.99
    return 4.99


def benutzer_waehlt_zahlungsmethode() -> Dict[str, str]:
    print("\nZahlungsmethoden:")
    print("1: Kreditkarte")
    print("2: PayPal")
    auswahl = input("Zahlungsmethode wählen (1/2): ")
    if auswahl == "1":
        nummer = input("Kreditkartennummer (Dummy): ")
        return {"typ": "kreditkarte", "nummer": nummer}
    else:
        konto = input("PayPal-E-Mail (Dummy): ")
        return {"typ": "paypal", "konto": konto}


def pruefe_zahlungsdaten(zahlungsmethode: Dict[str, str]) -> bool:
    return all(zahlungsmethode.values())


def zeige_bestelluebersicht(
    warenkorb: List[WarenkorbPosition],
    adresse: Dict[str, str],
    zahlungsmethode: Dict[str, str],
    versandkosten: float,
) -> None:
    print("\n--- Bestellübersicht ---")
    zeige_warenkorb_status(warenkorb)
    print("Lieferadresse:")
    for k, v in adresse.items():
        print(f"{k.capitalize()}: {v}")
    print("\nZahlungsmethode:", zahlungsmethode.get("typ"))
    print(f"Versandkosten: {versandkosten:.2f} €")
    gesamt = sum(pos.produkt.preis * pos.menge for pos in warenkorb) + versandkosten
    print(f"Zu zahlender Gesamtbetrag: {gesamt:.2f} €")
    print("------------------------\n")


def benutzer_klickt_jetzt_kaufen() -> bool:
    auswahl = input("'Jetzt kaufen' bestätigen? (j/n): ")
    return auswahl.lower() == "j"


def fuehre_zahlung_durch() -> bool:
    print("Zahlung wird verarbeitet...")
    return True


def erstelle_bestellung() -> None:
    print("Bestellung wurde im System erstellt.")


def sende_bestellbestaetigung() -> None:
    print("Bestellbestätigung per E-Mail gesendet.")


def zeige_danke_seite() -> None:
    print("\nVielen Dank für deinen Einkauf!")
    print("Deine Bestellung wird in Kürze bearbeitet.\n")


def zeige_fehlermeldung(nachricht: str) -> None:
    print(f"FEHLER: {nachricht}\n")


def main() -> None:
    benutzer_ist_im_shop = True
    warenkorb: List[WarenkorbPosition] = []
    benutzer = Benutzer()

    zeige_startseite()

    while benutzer_ist_im_shop:
        eingabe = benutzer_suchanfrage()
        if eingabe.lower() == "exit":
            print("Shop wird verlassen...")
            break

        produkte = suche_produkte(eingabe)
        zeige_produkte(produkte)

        if benutzer_waehlt_produkt():
            produkt = gewaehlt_produkt()
            if produkt:
                zeige_produktdetails(produkt)

                if benutzer_klickt_in_den_warenkorb():
                    for pos in warenkorb:
                        if pos.produkt.id == produkt.id:
                            pos.menge += 1
                            break
                    else:
                        warenkorb.append(WarenkorbPosition(produkt=produkt, menge=1))
                    zeige_warenkorb_status(warenkorb)

        if benutzer_klickt_warenkorb():
            zeige_warenkorb(warenkorb)

            if benutzer_aendert_warenkorb():
                aktualisiere_warenkorb(warenkorb)

            if benutzer_klickt_zur_kasse() and warenkorb:
                if benutzer_nicht_eingeloggt(benutzer):
                    entscheidung = frage_nach_login_oder_registrierung()
                    benutzer_login_oder_registrieren(benutzer, entscheidung)

                adresse = benutzer_gibt_lieferadresse_ein()
                if not pruefe_adresse(adresse):
                    zeige_fehlermeldung("Adresse unvollständig.")
                    continue
                benutzer.adresse = adresse

                versand_option = benutzer_waehlt_versand_option()
                versandkosten = berechne_versandkosten(versand_option)

                zahlungsmethode = benutzer_waehlt_zahlungsmethode()
                if not pruefe_zahlungsdaten(zahlungsmethode):
                    zeige_fehlermeldung("Zahlungsdaten unvollständig.")
                    continue
                benutzer.zahlungsmethode = zahlungsmethode

                zeige_bestelluebersicht(
                    warenkorb,
                    benutzer.adresse,
                    benutzer.zahlungsmethode,
                    versandkosten,
                )

                if benutzer_klickt_jetzt_kaufen():
                    bezahlung_erfolgreich = fuehre_zahlung_durch()

                    if bezahlung_erfolgreich:
                        erstelle_bestellung()
                        sende_bestellbestaetigung()
                        zeige_danke_seite()
                        benutzer_ist_im_shop = False
                    else:
                        zeige_fehlermeldung("Zahlung fehlgeschlagen")

    print("Programm beendet.")


if __name__ == "__main__":
    main()
