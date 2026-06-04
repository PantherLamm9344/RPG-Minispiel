#------------------------------
# Baugerüste für Objekte 
#------------------------------
class Spieler:
    def __init__(self):
        self.hp_max = 100
        self.hp_current = 0
        self.hp_min = 0
        self.muenzen = 0
        #   Schadensarten
        self.Gesamtschaden = 0
        self.PhysischerSchaden = 0
        self.GiftSchaden = 0
        self.FeuerSchaden = 0
        #   Wiederstände
        self.Rüstung = 0
        self.PhysischeResistenz = 0
        self.GiftResistenz = 0
        self.FeuerResistenz = 0
        self.klassenname = None



class Gegner:
    def __init__(self):
        self.hp_max = 0
        self.hp_current = 0
        self.hp_start = 0
        self.hp_min = 0
        #   Schadensarten
        self.Gesamtschaden = 0
        self.PhysischerSchaden = 0
        self.GiftSchaden = 0
        self.FeuerSchaden = 0
        #   Wiederstände
        self.Rüstung = 0
        self.PhysischeResistenz = 0
        self.GiftResistenz = 0
        self.FeuerResistenz = 0
        #------- LOOT---------
        self.drop_gnommuetzen = 0
        self.drop_koboldohr = 0
        self.drop_OgerZahn = 0
        self.drop_Trollhaut = 0
        self.drop_Muenzen = 0



        self.name = None



class Traenke:
    def __init__(self):
        self.hp = 0
        self.mana = 0
        self.anwendungen = 0
        #   Schadensarten
        self.Gesamtschaden = 0
        #   Wiederstände
        self.PhysischeResistenz = 0
        self.name = None



class Haendler:
    def __init__(self):
        self.name = None
        self.titel = None
        #----- KAUF -------------------
        self.KaufPreisHeiltrank = 0
        self.KaufPreisManatrank = 0
        self.KaufPreisLandKarte_Stadtgebiet = 50
        self.KaufPreisLandKarte_Berggebiet = 250
        self.KaufPreisLandKarte_Sumpfgebiet = 500
        self.KaufPreisLandKarte_Wiesengebiet = 1250
        self.Kauf_kleiner_Rucksack = 20
        self.Kauf_Normaler_Rucksack = 60
        self.Kauf_Großer_Rucksack = 180
        self.Kauf_Riesiger_Rucksack = 460
        self.KaufPreisHolzschwert = 50


        #------ VERKAUF ---------------
        self.VerkaufPreisGnomMuetze = 0
        self.VerkaufPreisKoboldohr = 0

        #------ WEITERENTWICKLUNG -----
        self.gesamtMuenzen = 0
        self.UpgradeBenoetigteMuenzen = 0
        self.Stufe = 0

#----------------------------- Haupthand -----------------------

class Kurzschwert:
    def __init__(self):
        self.name = None
        self.titel = None
        self.PhysischerSchaden = 0
        self.typ = "Kurzschwert"
        self.Ausrüstungsplatz = "Haupthand"
        self.imBesitz = False



class Axt:
    def __init__(self):
        self.name = None
        self.titel = None



class Streitkolben:
    def __init__(self):
        self.name = None
        self.titel = None



class Lehrlingstab:
    def __init__(self):
        self.name = None
        self.titel = None



class Adeptenstab:
    def __init__(self):
        self.name = None
        self.titel = None

#----------------------------- Nebenhand -----------------------



class Eckschild:
    def __init__(self):
        self.name = None
        self.titel = None



class Rundschild:
    def __init__(self):
        self.name = None
        self.titel = None



class Turmschild:
    def __init__(self):
        self.name = None
        self.titel = None

#----------------------------- Rüstung ---------------------

class Kopfschutz:
    def __init__(self):
        self.name = None
        self.titel = None



class Brustschutz:
    def __init__(self):
        self.name = None
        self.titel = None



class Armschutz:
    def __init__(self):
        self.name = None
        self.titel = None



class Hose:
    def __init__(self):
        self.name = None
        self.titel = None



class Beinschutz:
    def __init__(self):
        self.name = None
        self.titel = None



#----------------------------- Schmuck ---------------------

class Ring:
    def __init__(self):
        self.name = None
        self.titel = None



class Amulett:
    def __init__(self):
        self.name = None
        self.titel = None