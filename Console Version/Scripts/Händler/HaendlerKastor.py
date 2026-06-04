import Scripts.Händler.HaendlerWerte as HaendlerWerte
import Scripts.Funktionen.ClearScreen as ClearScreen
import Scripts.Spieler.Spieler as spieler


#-------------------------------------
# Händler Kastor Funktion
#-------------------------------------
def Kastor_Haendler():
        print()
        ClearScreen.clear_screen()
        print()
        print()
        print("                 Händler")
        print()
        print()
        print()
        print("                 Verkaufen")
        print()
        print("      1   ---     Gnommützen verkaufen /",HaendlerWerte.Kastor.VerkaufPreisGnomMuetze)
        print("      2   ---     Koboldohren verkaufen /",HaendlerWerte.Kastor.VerkaufPreisKoboldohr)
        print()
        print("Du hast ",spieler.stats.muenzen," Münzen")
        print()
        print()
        if spieler.stats.muenzen >= 5:
            print("Guten Tag werter Abenteurer.")
            print("Mein Name ist",HaendlerWerte.Kastor.name,HaendlerWerte.Kastor.titel)
            print("Was darf ich ihnen anbieten?")
        if spieler.stats.muenzen < 5:
            print("Bitte verschwenden sie meine Zeit nicht.")
            print("Kommen sie wieder wenn sie genügend Münzen haben")
            print("Oder verkauf was brauchbares")
        print()
        HaendlerAuswahl = input("... ") 
        if HaendlerAuswahl == "1" and spieler.inventar.InventarGnomMuetze >= 1:
            print()
            print("Du verkaufst dem Händler eine GnomMütze für",HaendlerWerte.Kastor.VerkaufPreisGnomMuetze,"Münzen")
            spieler.inventar.InventarGnomMuetze -= 1
            spieler.inventar.InventarKapazitaet -= 1
            spieler.stats.muenzen += HaendlerWerte.Kastor.VerkaufPreisGnomMuetze
            print()
            Stopper = input("... ")
        elif HaendlerAuswahl == "1" and spieler.inventar.InventarGnomMuetze <= 0:
            print()
            print("Du hast nicht genügend GnomMütze dabei")
            Stopper = input("... ") 
        if HaendlerAuswahl == "2" and spieler.inventar.InventarKoboldohr >= 1:
            print()
            print("Du verkaufst dem Händler eine GnomMütze für",HaendlerWerte.Kastor.VerkaufPreisKoboldohr,"Münzen")
            spieler.inventar.InventarKoboldohr -= 1
            spieler.inventar.InventarKapazitaet -= 1
            spieler.stats.muenzen += HaendlerWerte.Kastor.VerkaufPreisKoboldohr
            print()
            Stopper = input("... ")
        elif HaendlerAuswahl == "2" and spieler.inventar.InventarKoboldohr <= 0:
            print()
            print("Du hast nicht genügend Kobold Ohren dabei")
            Stopper = input("... ") 
