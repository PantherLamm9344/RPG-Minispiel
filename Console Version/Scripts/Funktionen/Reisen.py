import Scripts.funktionen as funktionen
import Scripts.Spieler.Spieler as spieler
import Scripts.Gebiete.Gebiete as Gebiete

def Reisen():
    print()
    funktionen.ClearScreen.clear_screen()
    print()
    print("     Wohin möchtest du reisen?")
    print()
    print("1    --- Waldgebiet")
    if spieler.inventar.Karte_Stadtgebiet == True:
        print("2    --- Stadtgebiet")
    if spieler.inventar.Karte_Berggebiet == True:
        print("3    --- Berggebiet")
    if spieler.inventar.Karte_Sumpfgebiet == True:
        print("4    --- Sumpfgebiet")
    Gebiete.Gebietauswahl = input("... ")
    match Gebiete.Gebietauswahl:
        case "1":
            print()
            Gebiete.Gebietauswahl = "1"
        case "2":
            print()
            Gebiete.Gebietauswahl = "2"
        case "3":
            print()
            Gebiete.Gebietauswahl = "3"
        case "4":
            print()
            Gebiete.Gebietauswahl = "4"
        case _:
            print()
            Gebiete.Gebietauswahl = "1"