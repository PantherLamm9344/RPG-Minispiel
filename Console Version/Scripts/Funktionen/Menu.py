import Scripts.funktionen as funktionen
import Scripts.Texte.Texte as Texte
import Scripts.Gebiete.Gebiete as Gebiete
import Scripts.Spieler.Spieler as spieler
import Scripts.Gegner.Gegner as Gegner

MainMenu = ""

def Menu_Hauptmenu():
    while True:
        print("---------------------------------------------------")
        print("---------------------------------------------------")
        print("---------          RPGminispiel          ----------")
        print("---------          ------------          ----------")
        print("---------             Start              ----------")
        print("---------            Beenden             ----------")
        print("---------------------------------------------------")
        print("---------------------------------------------------")
        print()
        print()
        print()
        MainMenu = input("... ")
        match MainMenu:
            #-------------------------------------
            #----------- START -------------------
            #-------------------------------------
            case "Start":
                funktionen.ClearScreen.clear_screen()
                print("Daten werden geladen...")
                MainMenu = "Start"
                break
            case "Starten":
                funktionen.ClearScreen.clear_screen()
                print("Daten werden geladen...")
                MainMenu = "Start"
                break
            case "start":
                funktionen.ClearScreen.clear_screen()
                print("Daten werden geladen...")
                MainMenu = "Start"
                break
            case "starten":
                funktionen.ClearScreen.clear_screen()
                print("Daten werden geladen...")
                MainMenu = "Start"
                break
            #---------------------------------------
            #----------- BEENDEN -------------------
            #---------------------------------------
            case "Beenden":
                funktionen.ClearScreen.clear_screen()
                print("Spiel wird beendet")
                break

            case "beenden":
                funktionen.ClearScreen.clear_screen()
                print("Spiel wird beendet")
                break

            case "exit":
                funktionen.ClearScreen.clear_screen()
                print("Spiel wird beendet")
                break
            #--------------------------------------------
            #----------- ALLES ANDERE -------------------
            #--------------------------------------------
            case _:
                print()
                print("Eingabe wurde nicht erkannt")
                print()
                print("Bitte erneut versuchen")
                print()


def Menu_Klassenauswahl():
    while MainMenu == "Start":
        print()
        print("Spieler wird erstellt ...")  
        print()
        print("Welche Klasse willst du spielen?")
        print()
        print("     1   --- für Magier")
        print("     2   --- für Paladin")
        print("     3   --- für Kämpfer")
        print()
        spieler.stats
        KlasseGewaehlt = False
        KlassenAuswahl = input()
        match KlassenAuswahl:
            #-----------------------------------
            #------------ MAGIER ---------------
            #-----------------------------------
            case "1":
                print("Daten werden geladen...")
                funktionen.Klassenwerte.selectMage()
                KlasseGewaehlt = True
                funktionen.ClearScreen.clear_screen()
                print()
                print("Klasse des Spielers wurde festgelegt auf", spieler.stats.klassenname)
                print()
                print()
                print()
                Texte.IntroText01()
                print()
                Gebiete.Gebietauswahl = "1"
                Stopper = input()
                break
            #------------------------------------
            #------------ PALADIN ---------------
            #------------------------------------
            case "2":
                print("Daten werden geladen...")
                funktionen.Klassenwerte.selectPaladin()
                KlasseGewaehlt = True
                funktionen.ClearScreen.clear_screen()
                print()
                print("Klasse des Spielers wurde festgelegt auf", spieler.stats.klassenname)
                print()
                print()
                print()
                Texte.IntroText01()
                print()
                Gebiete.Gebietauswahl = "1"
                Stopper = input()
                break
            #-----------------------------------
            #------------ KÄPFER ---------------
            #-----------------------------------
            case "3":
                print("Daten werden geladen...")
                funktionen.Klassenwerte.selectKaempfer()
                KlasseGewaehlt = True
                funktionen.ClearScreen.clear_screen()
                print()
                print("Klasse des Spielers wurde festgelegt auf", spieler.stats.klassenname)
                print()
                print()
                print()
                Texte.IntroText01()
                print()
                Gebiete.Gebietauswahl = "1"
                Stopper = input()
                break
            #--------------------------------------------
            #----------- ALLES ANDERE -------------------
            #--------------------------------------------
            case _:
                print()
                print("Eingabe wurde nicht erkannt")
                print()
                print("Bitte erneut versuchen")
                print()


def Menu_Waldgebiet():
    funktionen.ClearScreen.clear_screen()
    print()
    print(" Du befindest dich im Waldgebiet")
    print()
    print("    ( )     ( )     ( )      ")
    print("   (   )   (   )   (   )     ")
    print("    | |     | |     | |      ")
    print("    | |     | |     | |      ")
    print("   -----   -----   -----     ")
    print()
    print("===============================")
    print()
    print("Wie gehst du weiter vor?")
    print()
    if Gegner.gnom.hp_current > Gegner.gnom.hp_min:
        print(" 1   ---    Starte einen Angriff auf Gnom")
    if Gegner.kobold.hp_current > Gegner.kobold.hp_min:
        print(" 2   ---    Starte einen Angriff auf Kobold")
    print(" 3")
    print(" 4   ---    Reisen") #--- GEBIETSAUSWHAL / REISEMENU
    print(" 5   ---    Zum Händler")
    print(" 6   ---    Inventar")
    if Gegner.kobold.hp_current > Gegner.kobold.hp_min or Gegner.gnom.hp_current > Gegner.gnom.hp_min:
        print(" 7   ---    Zeigt Gegnerische aktuellen Werte an")
    print(" 8   ---    Ausrüstung Anlegen/Ablegen")
    if Gegner.gnom.hp_current <= Gegner.gnom.hp_min and Gegner.kobold.hp_current <= Gegner.kobold.hp_min:   
        print(" 9   ---    Du hast das Gebiet erfolgreich gesäubert willst du an einem Lagerfeuer rasten?")
    print()
    print()
    print()


def Menu_Stadtgebiet():
    funktionen.ClearScreen.clear_screen()
    print()
    print(" Du befindest dich im Stadtgebiet")
    print()
    print("   ||             ")
    print(" -------------    ")
    print(" |  | |  | | |    ")
    print(" |   ___     |    ")
    print(" |   | |     |    ")
    print(" -------------    ")
    print()
    print("===============================")
    print()
    print("Wie gehst du weiter vor?")
    print()
    print(" 1   ---    Zum Händler Kastor")
    print(" 2   ---    Zum Händler Horus")
    print(" 3")
    print(" 4   ---    Reisen") #--- GEBIETSAUSWHAL / REISEMENU
    print(" 5")
    print(" 6   ---    Inventar")   
    print(" 7")   
    print(" 8   ---    Ausrüstung Anlegen/Ablegen")  
    print(" 9") 
    print()
    print()
    print()


def Menu_Berggebiet():
    print()
    print("         Du befindest dich im Berggebiet")
    print()
    print("Wie gehst du weiter vor?")
    print()
    if Gegner.Oger.hp_current > Gegner.Oger.hp_min:
        print(" 1   ---    Starte einen Angriff auf Oger")
    if Gegner.Troll.hp_current > Gegner.Troll.hp_min:
        print(" 2   ---    Starte einen Angriff auf Troll")
    if Gegner.kobold.hp_current > Gegner.kobold.hp_min:
        print(" 3   ---    Starte einen Angriff auf Kobold")
    print(" 4   ---    Reisen") #--- GEBIETSAUSWHAL / REISEMENU
    print(" 5")
    print(" 6   ---    Inventar")
    if Gegner.Oger.hp_current > Gegner.Oger.hp_min or Gegner.Troll.hp_current > Gegner.Troll.hp_min or Gegner.kobold.hp_current > Gegner.kobold.hp_min:
        print(" 7   ---    Zeigt Gegnerische aktuellen Werte an")
    print(" 8   ---    Ausrüstung Anlegen/Ablegen")
    if Gegner.Oger.hp_current <= Gegner.Oger.hp_min and Gegner.Troll.hp_current <= Gegner.Troll.hp_min and Gegner.kobold.hp_current <= Gegner.kobold.hp_min:   
        print(" 9   ---    Du hast das Gebiet erfolgreich gesäubert willst du an einem Lagerfeuer rasten?")
    print()
    print()
    print()