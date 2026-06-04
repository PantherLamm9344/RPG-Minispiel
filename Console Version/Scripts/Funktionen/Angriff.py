import Scripts.Spieler.Spieler as spieler
import Scripts.Gegner.Gegner as Gegner

#-------------------------------------
# Angriffe auch Gegner
#-------------------------------------
AktuellerGegner = None


def Angriff_Gnom():
    print()
    AktuellerGegner = Gegner.gnom
    if AktuellerGegner.hp_current > AktuellerGegner.hp_min:
        print()
        print("Wie oft willst du ",AktuellerGegner.name," angreifen?")
        print()
        try:
            Menge = input("... ")
            Menge = int(Menge)
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben!")
        for Angriffsmenge in range(Menge):
            Angriffsmenge +=1
            print()
            print("Name",AktuellerGegner.name)
            print("Alte HP",AktuellerGegner.hp_current)
            print()
            spieler.stats.Gesamtschaden = spieler.stats.Gesamtschaden + spieler.stats.PhysischerSchaden + spieler.stats.FeuerSchaden + spieler.stats.GiftSchaden
            AktuellerGegner.hp_current = (AktuellerGegner.hp_current - (spieler.stats.Gesamtschaden - AktuellerGegner.Rüstung))
            if AktuellerGegner.hp_current <= AktuellerGegner.hp_min:
                AktuellerGegner.hp_current = 0
            print()
            print("Name",AktuellerGegner.name)
            print("Aktuelle HP",AktuellerGegner.hp_current)
            print()
            print()
            print("Spieler")
            print("Alte HP",spieler.stats.hp_current)
            print()
            spieler.stats.hp_current = (spieler.stats.hp_current - (AktuellerGegner.Gesamtschaden - spieler.stats.Rüstung))
            print()
            print("Spieler")
            print("Aktuelle HP",spieler.stats.hp_current)
            print() 
            if AktuellerGegner.hp_current <= AktuellerGegner.hp_min:
                print("Du hast gefunden")
                print(AktuellerGegner.drop_gnommuetzen,"Gnommützen")
                print()
                if spieler.inventar.InventarKapazitaet < spieler.inventar.InventarMaxKapazitaet:
                    spieler.inventar.InventarGnomMuetze = spieler.inventar.InventarGnomMuetze + AktuellerGegner.drop_gnommuetzen
                    spieler.inventar.InventarKapazitaet += AktuellerGegner.drop_gnommuetzen
                    break
                elif spieler.inventar.InventarKapazitaet == spieler.inventar.InventarMaxKapazitaet:
                    print()
                    print("Du hast leider kein Platz mehr im Inventar und lässt den Gegenstand liegen")
                    print()
                    break
        TEST02 = input()
        AktuellerGegner = None
    else:
        print()
        AktuellerGegner = None

def Angriff_Goblin():
    print()
    if Gegner.gnom.hp_current > Gegner.gnom.hp_min:
        print()
        print("Wie oft willst du ",Gegner.gnom.name," angreifen?")
        print()
        try:
            Menge = input("... ")
            Menge = int(Menge)
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben!")
        for Angriffsmenge in range(Menge):
            Angriffsmenge +=1
            print()
            print("Name",Gegner.gnom.name)
            print("Alte HP",Gegner.gnom.hp_current)
            print()
            spieler.stats.Gesamtschaden = spieler.stats.Gesamtschaden + spieler.stats.PhysischerSchaden + spieler.stats.FeuerSchaden + spieler.stats.GiftSchaden
            Gegner.gnom.hp_current = (Gegner.gnom.hp_current - (spieler.stats.Gesamtschaden - Gegner.gnom.Rüstung))
            if Gegner.gnom.hp_current <= Gegner.gnom.hp_min:
                Gegner.gnom.hp_current = 0
            print()
            print("Name",Gegner.gnom.name)
            print("Aktuelle HP",Gegner.gnom.hp_current)
            print()
            print()
            print("Spieler")
            print("Alte HP",spieler.stats.hp_current)
            print()
            spieler.stats.hp_current = (spieler.stats.hp_current - (Gegner.gnom.Gesamtschaden - spieler.stats.Rüstung))
            print()
            print("Spieler")
            print("Aktuelle HP",spieler.stats.hp_current)
            print() 
            if Gegner.gnom.hp_current <= Gegner.gnom.hp_min:
                print("Du hast gefunden")
                print(Gegner.gnom.drop_gnommuetzen,"Gnommützen")
                print()
                if spieler.inventar.InventarKapazitaet < spieler.inventar.InventarMaxKapazitaet:
                    spieler.inventar.InventarGnomMuetze = spieler.inventar.InventarGnomMuetze + Gegner.gnom.drop_gnommuetzen
                    spieler.inventar.InventarKapazitaet += Gegner.gnom.drop_gnommuetzen
                    break
                elif spieler.inventar.InventarKapazitaet == spieler.inventar.InventarMaxKapazitaet:
                    print()
                    print("Du hast leider kein Platz mehr im Inventar und lässt den Gegenstand liegen")
                    print()
                    break
        TEST02 = input()
    else:
        print()

def Angriff_Kobold():
    print()
    if Gegner.kobold.hp_current > Gegner.kobold.hp_min:
        print()
        print("Wie oft willst du ",Gegner.kobold.name," angreifen?")
        print()
        Menge = input()
        Menge = int(Menge)
        for Angriffsmenge in range(Menge):
            Angriffsmenge +=1
            print()
            print("Name",Gegner.kobold.name)
            print("Alte HP",Gegner.kobold.hp_current)
            print()
            Gegner.kobold.hp_current = (Gegner.kobold.hp_current - (spieler.stats.Gesamtschaden - Gegner.kobold.Rüstung))
            if Gegner.kobold.hp_current <= Gegner.kobold.hp_min:
                Gegner.kobold.hp_current = 0
            print()
            print("Name",Gegner.kobold.name)
            print("Aktuelle HP",Gegner.kobold.hp_current)
            print()
            print()
            print("Spieler")
            print("Alte HP",spieler.stats.hp_current)
            print()
            spieler.stats.hp_current = (spieler.stats.hp_current - (Gegner.kobold.Gesamtschaden - spieler.stats.Rüstung))
            print()
            print("Spieler")
            print("Aktuelle HP",spieler.stats.hp_current)
            print()
            if Gegner.kobold.hp_current <= Gegner.kobold.hp_min:
                print("Du hast gefunden")
                print(Gegner.kobold.drop_koboldohr,"Kobold Ohr")
                print()
                if spieler.inventar.InventarKapazitaet < spieler.inventar.InventarMaxKapazitaet:
                    spieler.inventar.InventarKoboldohr = spieler.inventar.InventarKoboldohr + Gegner.kobold.drop_koboldohr
                    spieler.inventar.InventarKapazitaet += Gegner.kobold.drop_koboldohr
                    break
                elif spieler.inventar.InventarKapazitaet == spieler.inventar.InventarMaxKapazitaet:
                    print()
                    print("Du hast leider kein Platz mehr im Inventar und lässt den Gegenstand liegen")
                    print()
                    break
        TEST02 = input()
    else:
        print()

def Angriff_Oger():
    print()
    if Gegner.Oger.hp_current > Gegner.Oger.hp_min:
    
        print()
        print("Name",Gegner.Oger.name)
        print("Alte HP",Gegner.Oger.hp_current)
        print()
        Gegner.Oger.hp_current = (Gegner.Oger.hp_current - (spieler.stats.Gesamtschaden - Gegner.Oger.Rüstung))
        if Gegner.Oger.hp_current <= Gegner.Oger.hp_min:
            Gegner.Oger.hp_current = 0
        print()
        print("Name",Gegner.Oger.name)
        print("Aktuelle HP",Gegner.Oger.hp_current)
        print()
        print()
        print("Spieler")
        print("Alte HP",spieler.stats.hp_current)
        print()
        spieler.stats.hp_current = (spieler.stats.hp_current - (Gegner.Oger.Gesamtschaden - spieler.stats.Rüstung))
        print()
        print("Spieler")
        print("Aktuelle HP",spieler.stats.hp_current)
        print() 
        if Gegner.Oger.hp_current <= Gegner.Oger.hp_min:
            print("Du hast gefunden")
            print(Gegner.Oger.drop_OgerZahn,"Ogerzähne")
            print()
            if spieler.inventar.InventarKapazitaet <= spieler.inventar.InventarMaxKapazitaet:
                spieler.inventar.InventarOgerZahn = spieler.inventar.InventarOgerZahn + Gegner.Oger.drop_OgerZahn
                spieler.inventar.InventarKapazitaet += 1
            elif spieler.inventar.InventarKapazitaet >= spieler.inventar.InventarMaxKapazitaet:
                print()
                print("Du hast leider kein Platz mehr im Inventar und lässt den Gegenstand liegen")
                print()
        TEST02 = input()
    else:
        print()

def Angriff_Troll():
    print()
    if Gegner.Troll.hp_current > Gegner.Troll.hp_min:
    
        print()
        print("Name",Gegner.Troll.name)
        print("Alte HP",Gegner.Troll.hp_current)
        print()
        Gegner.Troll.hp_current = (Gegner.Troll.hp_current - (spieler.stats.Gesamtschaden - Gegner.Troll.Rüstung))
        if Gegner.Troll.hp_current <= Gegner.Troll.hp_min:
            Gegner.Troll.hp_current = 0
        print()
        print("Name",Gegner.Troll.name)
        print("Aktuelle HP",Gegner.Troll.hp_current)
        print()
        print()
        print("Spieler")
        print("Alte HP",spieler.stats.hp_current)
        print()
        spieler.stats.hp_current = (spieler.stats.hp_current - (Gegner.Troll.Gesamtschaden - spieler.stats.Rüstung))
        print()
        print("Spieler")
        print("Aktuelle HP",spieler.stats.hp_current)
        print() 
        if Gegner.Troll.hp_current <= Gegner.Troll.hp_min:
            print("Du hast gefunden")
            print(Gegner.Troll.drop_Trollhaut,"Trollhaut")
            print()
            if spieler.inventar.InventarKapazitaet <= spieler.inventar.InventarMaxKapazitaet:
                spieler.inventar.InventarTrollhaut = spieler.inventar.InventarTrollhaut + Gegner.Troll.drop_Trollhaut
                spieler.inventar.InventarKapazitaet += 1
            elif spieler.inventar.InventarKapazitaet >= spieler.inventar.InventarMaxKapazitaet:
                print()
                print("Du hast leider kein Platz mehr im Inventar und lässt den Gegenstand liegen")
                print()
        TEST02 = input()
    else:
        print()
       
def Angriff_Koboldhauptmann():
    print()
    if Gegner.Koboldhauptmann.hp_current > Gegner.Koboldhauptmann.hp_min:

        print()
        print("Name",Gegner.Koboldhauptmann.name)
        print("Alte HP",Gegner.Koboldhauptmann.hp_current)
        print()
        Gegner.Koboldhauptmann.hp_current = (Gegner.Koboldhauptmann.hp_current - (spieler.stats.Gesamtschaden - Gegner.Koboldhauptmann.Rüstung))
        if Gegner.Koboldhauptmann.hp_current <= Gegner.Koboldhauptmann.hp_min:
            Gegner.Koboldhauptmann.hp_current = 0
        print()
        print("Name",Gegner.Koboldhauptmann.name)
        print("Aktuelle HP",Gegner.Koboldhauptmann.hp_current)
        print()
        print()
        print("Spieler")
        print("Alte HP",spieler.stats.hp_current)
        print()
        spieler.stats.hp_current = (spieler.stats.hp_current - (Gegner.Koboldhauptmann.Gesamtschaden - spieler.stats.Rüstung))
        print()
        print("Spieler")
        print("Aktuelle HP",spieler.stats.hp_current)
        print()
        if Gegner.Koboldhauptmann.hp_current <= Gegner.Koboldhauptmann.hp_min:
            print("Du hast gefunden")
            print(Gegner.Koboldhauptmann.drop_koboldohr,"Kobold Ohr")
            print()
            if spieler.inventar.InventarKapazitaet <= spieler.inventar.InventarMaxKapazitaet:
                spieler.inventar.InventarKoboldohr = spieler.inventar.InventarKoboldohr + Gegner.Koboldhauptmann.drop_koboldohr
                spieler.inventar.InventarKapazitaet += 1
            elif spieler.inventar.InventarKapazitaet >= spieler.inventar.InventarMaxKapazitaet:
                print()
                print("Du hast leider kein Platz mehr im Inventar und lässt den Gegenstand liegen")
                print()
        TEST02 = input()
    else:
        print()