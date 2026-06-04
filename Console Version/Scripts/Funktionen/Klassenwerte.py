import Scripts.Spieler.Spieler as Spieler


#-----------------------------------------------------
# Funktion zum Auswählen der Klasse
#-----------------------------------------------------
def selectMage(): 
    Spieler.stats.hp_max = 120
    Spieler.stats.hp_current = 120
    Spieler.stats.hp_min = 0
    Spieler.stats.Gesamtschaden = 0
    Spieler.stats.PhysischerSchaden = 12
    Spieler.stats.GiftSchaden = 0
    Spieler.stats.FeuerSchaden = 0
    Spieler.stats.Rüstung = 0
    Spieler.stats.PhysischeResistenz = 0
    Spieler.stats.GiftResistenz = 0
    Spieler.stats.FeuerResistenz = 0
    Spieler.stats.klassenname = "Magier"
    Spieler.inventar.InventarMaxKapazitaet = 12
    Spieler.inventar.Karte_Waldgebiet = True

def selectPaladin(): 
    Spieler.stats.hp_max = 150
    Spieler.stats.hp_current = 150
    Spieler.stats.hp_min = 0
    Spieler.stats.Gesamtschaden = 0
    Spieler.stats.PhysischerSchaden = 10
    Spieler.stats.GiftSchaden = 0
    Spieler.stats.FeuerSchaden = 0
    Spieler.stats.Rüstung = 6
    Spieler.stats.PhysischeResistenz = 0
    Spieler.stats.GiftResistenz = 0
    Spieler.stats.FeuerResistenz = 0
    Spieler.stats.klassenname = "Paladin"
    Spieler.inventar.InventarMaxKapazitaet = 8
    Spieler.inventar.Karte_Waldgebiet = True

def selectKaempfer(): 
    Spieler.stats.hp_max = 75
    Spieler.stats.hp_current = 75
    Spieler.stats.hp_min = 0
    Spieler.stats.Gesamtschaden = 0
    Spieler.stats.PhysischerSchaden = 8
    Spieler.stats.GiftSchaden = 0
    Spieler.stats.FeuerSchaden = 0
    Spieler.stats.Rüstung = 9
    Spieler.stats.PhysischeResistenz = 0
    Spieler.stats.GiftResistenz = 0
    Spieler.stats.FeuerResistenz = 0
    Spieler.stats.klassenname = "Kämpfer"
    Spieler.inventar.InventarMaxKapazitaet = 10
    Spieler.inventar.Karte_Waldgebiet = True