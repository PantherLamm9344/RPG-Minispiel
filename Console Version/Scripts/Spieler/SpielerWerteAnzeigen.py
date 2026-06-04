import Scripts.funktionen as funktionen
import Scripts.Spieler.Spieler as Spieler


#-----------------------------------------------------
# Funktion zum Aufrufen des aktuellen Spieler Status
#-----------------------------------------------------
def SpielerStatus_anzeigen():
    print()
    print("Spieler Werte")
    print()
    print("Klasse",Spieler.stats.klassenname)
    print()
    print("Aktuelle HP",Spieler.stats.hp_current)
    print()
    print("PhysischerSchaden",Spieler.stats.PhysischerSchaden)
    print("Rüstung",Spieler.stats.Rüstung)
    print("PhysischeResistenz",Spieler.stats.PhysischeResistenz)
    print()
    print("Münzen ",Spieler.stats.muenzen)
    print()
    funktionen.Stopper.Stopper()