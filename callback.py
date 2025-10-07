def callback(text):
    text_grosse=len(text)
    print(f"Callback sagt: rechnet text length gleich {text_grosse}", text)

def gleb(text):
    print("Mein name ist gleb")

def mach_was(spaeter):
    print("Mache etwas...")
    spaeter("\n Fertig!")

mach_was(gleb)
