import Scripts.Händler.HaendlerWerte as HaendlerWerte
import Scripts.Funktionen.ClearScreen as ClearScreen
import Scripts.Spieler.Spieler as spieler

#-------------------------------------
# Händler Horus Funktion
#-------------------------------------

def Horus_Haendler():
        print()
        ClearScreen.clear_screen()
        print()
        print()
        print("                 Händler")
        print()
        print("      1   ---     Manatrank kaufen / ",HaendlerWerte.Horus.KaufPreisManatrank)
        print("      2   ---     Landkarte Berggebiet kaufen / ",HaendlerWerte.Horus.KaufPreisLandKarte_Berggebiet)
        print()
        print("                 Verkaufen")
        print()
        print("      3   ---     Gnommützen verkaufen /",HaendlerWerte.Horus.VerkaufPreisGnomMuetze)
        print()
        print()
        print("Du hast ",spieler.stats.muenzen," Münzen")
        print()
        print()
        if spieler.stats.muenzen >= 5:
            print("Guten Tag werter Abenteurer.")
            print("Mein Name ist",HaendlerWerte.Horus.name,HaendlerWerte.Horus.titel)
            print("Was darf ich ihnen anbieten?")
        if spieler.stats.muenzen < 5:
            print("Bitte verschwenden sie meine Zeit nicht.")
            print("Kommen sie wieder wenn sie genügend Münzen haben")
            print("Oder verkauf was brauchbares")
        print()
        HaendlerAuswahl = input("... ") 
        if HaendlerAuswahl == "1" and spieler.stats.muenzen >= HaendlerWerte.Horus.KaufPreisManatrank:
            print()
            if spieler.inventar.InventarKapazitaet <= spieler.inventar.InventarMaxKapazitaet:
                spieler.stats.muenzen -= HaendlerWerte.Horus.KaufPreisManatrank
                print("Du hast einen Manatrank gekauf")
                spieler.inventar.InventarManatrank += 1
                spieler.inventar.InventarKapazitaet += 1
                print()
                Stopper = input("... ")
            elif spieler.inventar.InventarKapazitaet >= spieler.inventar.InventarMaxKapazitaet:
                print()
                print()
                print("Du hast leider kein Platz mehr im Inventar und kaufst den Gegenstand nicht")
                print()
                Stopper = input("... ")
        elif HaendlerAuswahl == "1" and spieler.stats.muenzen < HaendlerWerte.Horus.KaufPreisManatrank:
            print()
            print("Du kannst dir keinen Manatrank leisten")
            print()
            Stopper = input("... ") 
        if HaendlerAuswahl == "2" and spieler.stats.muenzen >= HaendlerWerte.Horus.KaufPreisLandKarte_Berggebiet and spieler.inventar.Karte_Berggebiet == True:
            print()
            print("Du Besitzt diese Karte bereits")
            print()
            Stopper = input("... ")
        if HaendlerAuswahl == "2" and spieler.stats.muenzen >= HaendlerWerte.Horus.KaufPreisLandKarte_Berggebiet and spieler.inventar.Karte_Berggebiet == False:
            print()
            spieler.stats.muenzen -= HaendlerWerte.Horus.KaufPreisLandKarte_Berggebiet
            print("Du hast einen Landkarte für das Berggebiet gekauft")
            spieler.inventar.Karte_Berggebiet = True
            print()
            Stopper = input("... ")
        elif HaendlerAuswahl == "2" and spieler.stats.muenzen < HaendlerWerte.Horus.KaufPreisLandKarte_Berggebiet:
            print()
            print("Du kannst dir die Landkarte für das Berggebiet nicht leisten")
            print()
            Stopper = input("... ") 
        if HaendlerAuswahl == "3" and spieler.inventar.InventarGnomMuetze >= 1:
            print()
            print("Du verkaufst dem Händler eine GnomMütze für",HaendlerWerte.Horus.VerkaufPreisGnomMuetze,"Münzen")
            spieler.inventar.InventarGnomMuetze -= 1
            spieler.inventar.InventarKapazitaet -= 1
            spieler.stats.muenzen += HaendlerWerte.Horus.VerkaufPreisGnomMuetze
            print()
            Stopper = input("... ")
        elif HaendlerAuswahl == "3" and spieler.inventar.InventarGnomMuetze <= 0:
            print()
            print("Du hast nicht genügend GnomMütze dabei")
            Stopper = input("... ")
