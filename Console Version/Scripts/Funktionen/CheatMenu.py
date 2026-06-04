import Scripts.Spieler.Spieler as Spieler


#-----------------------------------------------------
# Funktion zum Aufrufen des Cheat Menus
#-----------------------------------------------------
def CHEATmenuAnzeigen():
    print("Wilkommen im Cheat Menu")
    print()
    print("1 --- Gibt Spieler 5 Münzen")
    print("2 --- Gibt Spieler 10 Münzen")
    print("3 --- Gibt Spieler 99 Münzen")
    print("4 --- Gibt Spieler 100 HP")
    print("5 --- Erhöht vom Spieler die maximale HP um 100")
    CHEATinput = input("... ")
    if CHEATinput == "1":
        print(Spieler.stats.muenzen,"Alter Münzstand")
        Spieler.stats.muenzen += 5
        print("Dem Spieler wurden 5 Münzen hinzugefügt")
        print(Spieler.stats.muenzen,"Neuer Münzstand")
        print()
        Stopper = input("... ")
    if CHEATinput == "2":
        print(Spieler.stats.muenzen,"Alter Münzstand")
        Spieler.stats.muenzen += 10
        print("Dem Spieler wurden 10 Münzen hinzugefügt")
        print(Spieler.stats.muenzen,"Neuer Münzstand")
        print()
        Stopper = input("... ")
    if CHEATinput == "3":
        print(Spieler.stats.muenzen,"Alter Münzstand")
        Spieler.stats.muenzen += 99
        print("Dem Spieler wurden 99 Münzen hinzugefügt")
        print(Spieler.stats.muenzen,"Neuer Münzstand")
        print()
        Stopper = input("... ")
