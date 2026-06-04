import Scripts.Händler.HaendlerWerte as HaendlerWerte
import Scripts.Gegenstände.Gegenstände as Gegenstände
import Scripts.Funktionen.ClearScreen as ClearScreen
import Scripts.Spieler.Spieler as spieler



#-------------------------------------
# Händler Emmil Funktion
#-------------------------------------
def Emmil_Haendler():
    print()
    ClearScreen.clear_screen()
    print()
    print()
    print("                 Händler")
    print()
    print("      1   ---     Heiltrank kaufen / ",HaendlerWerte.Emmil.KaufPreisHeiltrank)
    print("      2   ---     Manatrank kaufen / ",HaendlerWerte.Emmil.KaufPreisManatrank)
    print("      3   ---     Landkarte Stadt kaufen / ",HaendlerWerte.Emmil.KaufPreisLandKarte_Stadtgebiet)
    print("      4   ---     Kleinen Rucksack kaufen / ",HaendlerWerte.Emmil.Kauf_kleiner_Rucksack)
    if Gegenstände.Holzschwert.imBesitz == False:
        print("      5   ---     Holzschwert kaufen / ",HaendlerWerte.Emmil.KaufPreisHolzschwert)
    print()
    print("                 Verkaufen an Händler ")
    print()
    print("      6   ---     Gnommützen verkaufen /",HaendlerWerte.Emmil.VerkaufPreisGnomMuetze)
    print("      7   ---     Koboldohren verkaufen /",HaendlerWerte.Emmil.VerkaufPreisKoboldohr)
    print()
    print("Du hast ",spieler.stats.muenzen," Münzen")
    print()
    print()
    if spieler.stats.muenzen >= 5:
        print("Guten Tag werter Abenteurer.")
        print("Mein Name ist",HaendlerWerte.Emmil.name,HaendlerWerte.Emmil.titel)
        print("Was darf ich ihnen anbieten?")
    if spieler.stats.muenzen < 5:
        print("Bitte verschwenden sie meine Zeit nicht.")
        print("Kommen sie wieder wenn sie genügend Münzen haben")
        print("Oder verkauf was brauchbares")
    print()
    HaendlerAuswahl = input("...")
    if HaendlerAuswahl == "1" and spieler.stats.muenzen >= HaendlerWerte.Emmil.KaufPreisHeiltrank:
        print()
        if spieler.inventar.InventarKapazitaet < spieler.inventar.InventarMaxKapazitaet:
            spieler.stats.muenzen -= HaendlerWerte.Emmil.KaufPreisHeiltrank
            print("Du hast einen Heiltrank gekauf")
            spieler.inventar.InventarHeiltrank += 1
            spieler.inventar.InventarKapazitaet += 1
            print()
            Stopper = input("... ")
        elif spieler.inventar.InventarKapazitaet >= spieler.inventar.InventarMaxKapazitaet:
            print()
            print()
            print("Du hast leider kein Platz mehr im Inventar und kaufst den Gegenstand nicht")
            print()
            Stopper = input("... ")
    elif HaendlerAuswahl == "1" and spieler.stats.muenzen < HaendlerWerte.Emmil.KaufPreisHeiltrank:
        print()
        print("Du kannst dir keinen Heiltrank leisten")
        print()
        Stopper = input("... ")
    if HaendlerAuswahl == "2" and spieler.stats.muenzen >= HaendlerWerte.Emmil.KaufPreisManatrank:
        print()
        if spieler.inventar.InventarKapazitaet < spieler.inventar.InventarMaxKapazitaet:
            spieler.stats.muenzen -= HaendlerWerte.Emmil.KaufPreisManatrank
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
    elif HaendlerAuswahl == "2" and spieler.stats.muenzen < HaendlerWerte.Emmil.KaufPreisManatrank:
        print()
        print("Du kannst dir keinen Manatrank leisten")
        print()
        Stopper = input("...")
    if HaendlerAuswahl == "3" and spieler.stats.muenzen >= HaendlerWerte.Emmil.KaufPreisLandKarte_Stadtgebiet and spieler.inventar.Karte_Stadtgebiet == True:
        print()
        print("Du Besitzt diese Karte bereits")
        print()
        Stopper = input("... ")
    if HaendlerAuswahl == "3" and spieler.stats.muenzen >= HaendlerWerte.Emmil.KaufPreisLandKarte_Stadtgebiet and spieler.inventar.Karte_Stadtgebiet == False:
        print()
        spieler.stats.muenzen -= HaendlerWerte.Emmil.KaufPreisLandKarte_Stadtgebiet
        print("Du hast einen Landkarte für das Stadtgebiet gekauft")
        spieler.inventar.Karte_Stadtgebiet = True
        print()
        Stopper = input("... ")
    elif HaendlerAuswahl == "3" and spieler.stats.muenzen < HaendlerWerte.Emmil.KaufPreisLandKarte_Stadtgebiet:
        print()
        print("Du kannst dir die Landkarte für das Stadtgebiet nicht leisten")
        print()
        Stopper = input("... ")

    if HaendlerAuswahl == "4" and spieler.stats.muenzen >= HaendlerWerte.Emmil.Kauf_kleiner_Rucksack and spieler.inventar.kleiner_Rucksack == False:
        print()
        spieler.stats.muenzen -= HaendlerWerte.Emmil.KaufPreisLandKarte_Stadtgebiet
        print("Du hast einen kleinen Rucksack gekauft. Deine Tragekapazität hat sich erhöht.")
        spieler.inventar.kleiner_Rucksack = True
        spieler.inventar.InventarMaxKapazitaet += spieler.inventar.kleiner_Rucksack_Tragekapazität
        print()
        Stopper = input("... ")
    elif HaendlerAuswahl == "4" and spieler.stats.muenzen < HaendlerWerte.Emmil.Kauf_kleiner_Rucksack:
        print()
        print("Du kannst dir den kleinen Rucksack nicht leisten")
        print()
        Stopper = input("... ")

    

    if HaendlerAuswahl == "5" and spieler.stats.muenzen >= HaendlerWerte.Emmil.KaufPreisHolzschwert and Gegenstände.Holzschwert.imBesitz == False:
        print()
        Gegenstände.Holzschwert.imBesitz = True
        spieler.inventar.InventarKapazitaet += 1
        spieler.stats.muenzen -= 5
        print("Du hast dir ein Holzschwert gekauft")
        if spieler.inventar.AusrüstungHaupthand == False:
            spieler.inventar.AusrüstungHaupthand = True
            spieler.inventar.AusrüstungHaupthandGegenstand = Gegenstände.Holzschwert.name
            spieler.inventar.InventarKapazitaet -= 1
            spieler.stats.PhysischerSchaden += Gegenstände.Holzschwert.PhysischerSchaden
            print()
            print("Und hast es direkt ausgerüstet")
    elif HaendlerAuswahl == "5" and spieler.stats.muenzen < HaendlerWerte.Emmil.KaufPreisHolzschwert:
        print()
        print("Du kannst dir das Holzschwert nicht leisten")
        print()
        Stopper = input("... ")



    if HaendlerAuswahl == "6" and spieler.inventar.InventarGnomMuetze >= 1:
        print()
        print("Wie viele GnomMützen willst du mir verkaufen?")
        print("Du hast derzeit ",spieler.inventar.InventarGnomMuetze," zum verkaufen")
        print()
        Menge = input("... ")
        Menge = int(Menge)
        for verkaufsmenge in range(Menge):
            if spieler.inventar.InventarGnomMuetze >= 1:
                print()
                print("Du verkaufst dem Händler eine GnomMütze für",HaendlerWerte.Emmil.VerkaufPreisGnomMuetze,"Münzen")
                spieler.inventar.InventarGnomMuetze -= 1
                spieler.inventar.InventarKapazitaet -= 1
                spieler.stats.muenzen += HaendlerWerte.Emmil.VerkaufPreisGnomMuetze
                verkaufsmenge += 1
                print()
            elif spieler.inventar.InventarGnomMuetze <= 0:
                print("Du hast keine GnomMützen mehr!")
                break
        Stopper = input("... ")
    elif HaendlerAuswahl == "6" and spieler.inventar.InventarGnomMuetze <= 0:
        print()
        print("Du hast nicht genügend GnomMütze dabei")
        Stopper = input("... ")



    if HaendlerAuswahl == "7" and spieler.inventar.InventarKoboldohr >= 1:
        print()
        print("Wie viele Kobold Ohren willst du mir verkaufen?")
        print("Du hast derzeit ",spieler.inventar.InventarKoboldohr," zum verkaufen")
        print()
        Menge = input("... ")
        Menge = int(Menge)
        for verkaufsmenge in range(Menge):
            if spieler.inventar.InventarKoboldohr >= 1:
                print()
                print("Du verkaufst dem Händler eine Kobold Ohren für",HaendlerWerte.Emmil.VerkaufPreisKoboldohr,"Münzen")
                spieler.inventar.InventarKoboldohr -= 1
                spieler.inventar.InventarKapazitaet -= 1
                spieler.stats.muenzen += HaendlerWerte.Emmil.VerkaufPreisKoboldohr
                verkaufsmenge += 1
                print()
            elif spieler.inventar.InventarKoboldohr <= 0:
                print("Du hast keine Kobold Ohren mehr!")
                break

        Stopper = input("... ")
    elif HaendlerAuswahl == "7" and spieler.inventar.InventarKoboldohr <= 0:
        print()
        print("Du hast nicht genügend Kobold Ohren dabei")
        Stopper = input("... ")
