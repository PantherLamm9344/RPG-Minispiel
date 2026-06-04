import Scripts.funktionen as funktionen
import Scripts.Spieler.Spieler as spieler
#------------------------------
# Eventueller Ablageplatz für 
# Inventar Gegenstände
#-------------------------------
#Handschuhe = {'Lederhandschuhe': False,'Stoffhandschuhe': False}
#Hose = {'Lederhose': False, 'Stoffhose': False}
#Ausrüstung = {Handschuhe,Hose}

# Ausrüstung[Handschuhe["Lederhandschuhe"]] = True

class SpielerInventar:
    def __init__(self):
        #--------- VERBRAUCHSGEGENSTÄNDE -------
        self.InventarHeiltrank = 0
        self.InventarManatrank = 0
        self.InventarSchadensbufftrank = 0
        self.InventarVerteidigungstrank = 0

        #--------- GEBIETSKARTEN ---------------
        self.Karte_Waldgebiet = False
        self.Karte_Berggebiet = False
        self.Karte_Sumpfgebiet = False
        self.Karte_Wiesengebiet = False
        self.Karte_Stadtgebiet = False   

        #--------- AUSRÜSTUNG ------------------
        #--------- Haupthand
        self.AusrüstungHaupthand = False
        self.AusrüstungHaupthandGegenstand = None

        #--------- Nebenhand
        self.AusrüstungNebenhand = False
        self.AusrüstungNebenhandGegenstand = None

        #--------- PASSIVE UPGRADES ------------
        self.kleiner_Rucksack = False
        self.kleiner_Rucksack_Tragekapazität = 4

        self.Normaler_Rucksack = False
        self.Normaler_Rucksack_Tragekapazität = 4

        self.Großer_Rucksack = False
        self.Großer_Rucksack_Tragekapazität = 4

        self.Riesiger_Rucksack = False
        self.Riesiger_Rucksack_Tragekapazität = 8

        #--------- LOOT ------------------------
        self.InventarMaxKapazitaet = 0
        self.InventarKapazitaet = 0
        self.InventarGnomMuetze = 0
        self.InventarKoboldohr = 0
        self.InventarOgerZahn = 0
        self.InventarTrollhaut = 0


        self.InventarName = "SpielerInventar"






#----------------------------
# INVENTAR ANZEIGEN FUNKTION
#----------------------------

def SpielerInventar_anzeigen():
       funktionen.ClearScreen.clear_screen()
       print()
       print("  ",spieler.inventar.InventarName)
       print("  ",spieler.inventar.InventarMaxKapazitaet," / ",spieler.inventar.InventarKapazitaet,"Tragekapazität Max/Aktuell")
       print()
       print("      _____    ")
       print("     |   X |   ")
       print("     |  _| |   ")
       print("     |_____|   ")
       print()
       print("  Verfügbare Landkarten im Besitz")
       print()
       if spieler.inventar.Karte_Waldgebiet == True:
           print("  Landkarte Waldgebiet")
       if spieler.inventar.Karte_Stadtgebiet == True:
           print("  Landkarte Stadtgebiet")
       if spieler.inventar.Karte_Berggebiet == True:
           print("  Landkarte Berggebiet")
       if spieler.inventar.Karte_Wiesengebiet == True:
           print("  Landkarte Wiesengebiet")
       if spieler.inventar.Karte_Sumpfgebiet == True:
           print("  Landkarte Sumpfgebiet")
       print()
       print("      __       ")
       print("     /  |      ")
       print("     |  |      ")
       print("     |  |      ")
       print("     |  |      ")
       print("     |  |      ")
       print("     |__|      ")
       print("    |____|     ")
       print("     |__|      ")
       print("     (__)      ")
       print()
       print("  Derzeit Ausgerüstet")
       print()
       print("  Haupthand")
       if spieler.inventar.AusrüstungHaupthand == True:
           print(spieler.inventar.AusrüstungHaupthandGegenstand)
       if spieler.inventar.AusrüstungHaupthand == False:
           print("  Leer")
       print("  Nebenhand")
       if spieler.inventar.AusrüstungNebenhand == True:
           print(spieler.inventar.AusrüstungNebenhandGegenstand)
       if spieler.inventar.AusrüstungNebenhand == False:
           print("  Leer")
       print()
       print("      _____    ")
       print("    (|    (|   ")
       print("     |     |   ")
       print("     |_____|   ")
       print()
       print("  Derzeitige Rucksäcke")
       print()
       if spieler.inventar.kleiner_Rucksack == True:
           print("  Kleiner Rucksack --- +4 Tragekapazität")
       if spieler.inventar.Normaler_Rucksack == True:
           print("  Normaler Rucksack --- +4 Tragekapazität")
       if spieler.inventar.Großer_Rucksack == True:
           print("  Großer Rucksack --- +4 Tragekapazität")
       if spieler.inventar.Riesiger_Rucksack == True:
           print("  Riesiger Rucksack --- +8 Tragekapazität")
       print()
       print("       ___     ")
       print("       | |     ")
       print("      (___)    ")
       print()
       print("  Vorhandene Tränke")
       print()
       print("  ",spieler.inventar.InventarHeiltrank,"Heiltränke")
       print("  ",spieler.inventar.InventarManatrank,"Manatrank")
       print("  ",spieler.inventar.InventarSchadensbufftrank,"Schadensbufftrank")
       print("  ",spieler.inventar.InventarVerteidigungstrank,"Verteidigungstrank")
       print()
       print("  ",spieler.inventar.InventarGnomMuetze,"GnomMütze")
       print("  ",spieler.inventar.InventarKoboldohr,"Kobold Ohren")
       print()
       print()
       print()
       spieler.SpielerWerteAnzeigen.SpielerStatus_anzeigen() 