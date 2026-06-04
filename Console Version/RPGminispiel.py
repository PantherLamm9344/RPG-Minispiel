import Scripts.funktionen as funktionen
import Scripts.Werte.Stats as Stats
import Scripts.Spieler.Spieler as spieler
import Scripts.Texte.Texte as Texte
import Scripts.Gegner.Gegner as Gegner
import Scripts.Händler.Haendler as Haendler
import Scripts.Gebiete.Gebiete as Gebiete


#----------------------------------------------------------------------------------
#-------------------- Hauptmenü ---------------------------------------------------
#----------------------------------------------------------------------------------
while True:
        print()
        print()
        print()
        print("<----------------------------------------------->")
        print("<----------------------------------------------->")
        print("<--------->                          <---------->")
        print("<--------->       RPG Minispiel      <---------->")
        print("<--------->        -----------       <---------->")
        print("<--------->           Start          <---------->")
        print("<--------->          Beenden         <---------->")
        print("<--------->                          <---------->")
        print("<----------------------------------------------->")
        print("<----------------------------------------------->")
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
#----------------------------------------------------------------------------------
#------------------ START / Klassenauswahl ----------------------------------------
#----------------------------------------------------------------------------------
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
                funktionen.Stopper.Stopper()
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
                funktionen.Stopper.Stopper()
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
                funktionen.Stopper.Stopper()
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
#----------------------------------------------------------------------------------
#------------------- GAME LOOP ANFANG----------------------------------------------
#----------------------------------------------------------------------------------
while Gebiete.Waldgebiet == True:
    if MainMenu == "Beenden":
        break
    funktionen.ClearScreen.clear_screen()
    match Gebiete.Gebietauswahl:
        case "1": #WALDGEBIET
            funktionen.Menu.Menu_Waldgebiet()
            EntscheidungAuswahl = input("... ")
            print()
            print()
            print()
            #----------------------------------------------------
            #------------- CHEAT MENU ---------------------------
            #----------------------------------------------------
            match EntscheidungAuswahl:
                case "CHEAT":
                    funktionen.ClearScreen.clear_screen()
                    print()
                    funktionen.CheatMenu.CHEATmenuAnzeigen()
            #----------------------------------------------------
            #------------- ANGRIFF gnom -------------------------
            #----------------------------------------------------
                case "1":
                    funktionen.Angriff.Angriff_Gnom()
            #----------------------------------------------------
            #------------- ANGRIFF kobold -----------------------
            #----------------------------------------------------
                case "2":
                    funktionen.Angriff.Angriff_Kobold()
            #----------------------------------------------------
            #------------- REISEN ------------------------------
            #----------------------------------------------------
                case "4":
                    funktionen.Reisen.Reisen()
            #----------------------------------------------------
            #------------- HÄNDLER ------------------------------
            #----------------------------------------------------
                case "5":
                    Haendler.HaendlerEmmil.Emmil_Haendler()
            #----------------------------------------------------
            #------------- INVENTAR -----------------------------
            #----------------------------------------------------
                case "6":
                    spieler.Inventar.SpielerInventar_anzeigen()
            #----------------------------------------------------
            #------------- NEUSTART LOOP ------------------------
            #----------------------------------------------------
                case "9":
                    if Gegner.gnom.hp_current <= Gegner.gnom.hp_min and Gegner.kobold.hp_current <= Gegner.kobold.hp_min:
                        funktionen.GegnerReset.GegnerResetWaldgebiet()
            #----------------------------------------------------
            #------------------- SPIEL BEENDEN ------------------
            #----------------------------------------------------
                case "Beenden":
                    funktionen.ClearScreen.clear_screen()
                    MainMenu = "Beenden"
                case "beenden":
                    funktionen.ClearScreen.clear_screen()
                    MainMenu = "Beenden"
                case "exit":
                    funktionen.ClearScreen.clear_screen()
                    MainMenu = "Beenden"
            #-------------------------------------------------
            #------------------- STATS -----------------------
            #-------------------------------------------------
                case "7":
                    funktionen.GegnerStatsAnzeigen.GegnerStatsAnzeigen_Waldgebiet()

                case "8":
                    spieler.SpielerWerteAnzeigen.SpielerStatus_anzeigen()

                case _:
                    print("Eingabe war falsch")
        case "2": #STADTGEBIET
            if Gebiete.Gebietauswahl == "2" and spieler.inventar.Karte_Stadtgebiet == True: 
                funktionen.Menu.Menu_Stadtgebiet()
                EntscheidungAuswahl = input("... ")
                print()
                print()
                print() 
                #----------------------------------------------------
                #------------- CHEAT MENU ---------------------------
                #----------------------------------------------------
                match EntscheidungAuswahl:
                    case "CHEAT":
                        funktionen.ClearScreen.clear_screen()
                        print()
                        funktionen.CheatMenu.CHEATmenuAnzeigen()  
                #----------------------------------------------------
                #------------- REISEN ------------------------------
                #----------------------------------------------------
                    case "4":
                        funktionen.Reisen.Reisen() 
                #----------------------------------------------------
                #------------- HÄNDLER KASTOR -----------------------
                #----------------------------------------------------
                    case "1":
                        Haendler.HaendlerKastor.Kastor_Haendler()
                #----------------------------------------------------
                #------------- HÄNDLER HORUS -----------------------
                #----------------------------------------------------
                    case "2":
                        Haendler.HaendlerHorus.Horus_Haendler()
                #----------------------------------------------------
                #------------- INVENTAR ------------------------------
                #----------------------------------------------------
                    case "6":
                        spieler.Inventar.SpielerInventar_anzeigen()
                #----------------------------------------------------
                #------------- NEUSTART LOOP ------------------------
                #----------------------------------------------------
                    case "9":
                        if Gegner.gnom.hp_current <= Gegner.gnom.hp_min and Gegner.kobold.hp_current <= Gegner.kobold.hp_min:
                            funktionen.GegnerReset.GegnerResetWaldgebiet()
                            print("   *      *     *         *          *      *")
                            print(" *     *              *           *        * ")
                            print("    *     *       *        *     *     *    *")
                            print(" *   *             *      *        *  *     *")
                            print()
                            print()
                            print("Du rastest und ruhst dich aus. In der Nacht wachst du wegen geräusche von Kreaturen wieder auf.")
                            print("Anscheinend sind wieder Monster aufgetaucht, und du beendest deine Rast.")
                            print()
                            print()
                            funktionen.Stopper.Stopper() 
                #----------------------------------------------------
                #------------------- SPIEL BEENDEN ------------------
                #----------------------------------------------------
                    case "Beenden":
                        funktionen.ClearScreen.clear_screen()
                        MainMenu = "Beenden"

                    case "beenden":
                        funktionen.ClearScreen.clear_screen()
                        MainMenu = "Beenden"

                    case "exit":
                        funktionen.ClearScreen.clear_screen()
                        MainMenu = "Beenden"
                #-------------------------------------------------
                #------------------- STATS -----------------------
                #-------------------------------------------------  
                    case "8":
                        spieler.SpielerWerteAnzeigen.SpielerStatus_anzeigen()    
                    case _:
                        print("Eingabe war falsch")            
            if Gebiete.Gebietauswahl == "2" and spieler.inventar.Karte_Stadtgebiet == False:
                print()
                print("Du versuchst zur Stadt zu reisen")
                print("Leider fehlt dir eine Karte um den Weg zur Stadt zu finden")
                print()
                Gebiete.Gebietauswahl = "1"
                Stopper = input("... ")
        case "3": #BERGGEBIET
            if Gebiete.Gebietauswahl == "3" and spieler.inventar.Karte_Berggebiet == True: 
                funktionen.ClearScreen.clear_screen()
                funktionen.Menu.Menu_Berggebiet()
                EntscheidungAuswahl = input("... ")
                print()
                print()
                print()
                #----------------------------------------------------
                #------------- CHEAT MENU ---------------------------
                #----------------------------------------------------
                match EntscheidungAuswahl:
                    case "CHEAT":
                        funktionen.ClearScreen.clear_screen()
                        print()
                        funktionen.CheatMenu.CHEATmenuAnzeigen()
                #----------------------------------------------------
                #------------- ANGRIFF Oger -------------------------
                #----------------------------------------------------
                    case "1":
                        funktionen.Angriff.Angriff_Oger()
                #----------------------------------------------------
                #------------- ANGRIFF Troll -----------------------
                #----------------------------------------------------
                    case "2":
                        funktionen.Angriff.Angriff_Troll()
                #----------------------------------------------------
                #------------- ANGRIFF Koboldhauptmann --------------
                #----------------------------------------------------
                    case "3":
                        funktionen.Angriff.Angriff_Koboldhauptmann()
                #----------------------------------------------------
                #------------- REISEN ------------------------------
                #----------------------------------------------------
                    case "4":
                        funktionen.Reisen.Reisen()
                #----------------------------------------------------
                #------------- INVENTAR ------------------------------
                #----------------------------------------------------
                    case "6":
                        spieler.Inventar.SpielerInventar_anzeigen()
                #----------------------------------------------------
                #------------- NEUSTART LOOP ------------------------
                #----------------------------------------------------
                    case "9":
                        if Gegner.Oger.hp_current <= Gegner.Oger.hp_min and Gegner.Troll.hp_current <= Gegner.Troll.hp_min and Gegner.Koboldhauptmann.hp_current <= Gegner.Koboldhauptmann.hp_min:
                            funktionen.GegnerReset.GegnerResetBerggebiet()
                            print("    *     *       *        *     *     *    *")
                            print("   *      *     *         *          *      *")
                            print("    *     *       *        *     *     *    *")
                            print(" *     *              *           *        * ")
                            print()
                            print("Du rastest und ruhst dich aus. In der Nacht wachst du wegen geräusche von Kreaturen wieder auf.")
                            print("Anscheinend sind wieder Monster aufgetaucht, und du beendest deine Rast.")
                            print()
                            print()
                            Stopper = input("... ")
                #----------------------------------------------------
                #------------------- SPIEL BEENDEN ------------------
                #----------------------------------------------------
                    case "Beenden":
                        funktionen.ClearScreen.clear_screen()
                        MainMenu = "Beenden"
                    case "beenden":
                        funktionen.ClearScreen.clear_screen()
                        MainMenu = "Beenden"
                    case "exit":
                        funktionen.ClearScreen.clear_screen()
                        MainMenu = "Beenden"
                #-------------------------------------------------
                #------------------- STATS -----------------------
                #-------------------------------------------------
                    case "7":
                        funktionen.GegnerStatsAnzeigen.GegnerStatsAnzeigen_Waldgebiet()
                    case "8":
                        spieler.SpielerWerteAnzeigen.SpielerStatus_anzeigen()
                    case _:
                        print("Eingabe war falsch")            
            if Gebiete.Gebietauswahl == "3" and spieler.inventar.Karte_Berggebiet == False:
                print()
                print("Du versuchst zu den Bergen zu reisen")
                print("Leider fehlt dir eine Karte um die Berge hinauf zu steigen")
                print()
                Gebiete.Gebietauswahl = "1"
                funktionen.Stopper.Stopper()
#----------------------------------------------------------------------------------
#------------------ SPIEL BEENDEN -------------------------------------------------
#----------------------------------------------------------------------------------
while MainMenu == "Beenden":
    print("Spiel wird geschlossen...")
    break