import Scripts.Gegner.Gegner as Gegner


#-----------------------------------------------------
# Funktion zum Anzeigen Gegnerischen Stats
#-----------------------------------------------------
def GegnerStatsAnzeigen_Waldgebiet():
    if Gegner.kobold.hp_current > Gegner.kobold.hp_min:
        print()
        print("Name",Gegner.kobold.name)
        print("Max HP",Gegner.kobold.hp_max)
        print("Aktuelle HP",Gegner.kobold.hp_current)
        print()
        
    if Gegner.kobold.hp_current == 0:
        print()
        print("Name",Gegner.kobold.name)
        print("Status: Besiegt")
        print()

    if Gegner.gnom.hp_current > Gegner.gnom.hp_min:
        print()
        print("Name",Gegner.gnom.name)
        print("Max HP",Gegner.gnom.hp_max)
        print("Aktuelle HP",Gegner.gnom.hp_current)
        print()

    if Gegner.gnom.hp_current == 0:
        print()
        print("Name",Gegner.gnom.name)
        print("Status: Besiegt")
        print()
    
    Stopper = input("... ")

