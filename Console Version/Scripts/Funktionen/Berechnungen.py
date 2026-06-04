import Scripts.funktionen as funktionen
import Scripts.Spieler.Spieler as spieler


def PhysischerAngriffBerechnung():
    spieler.stats.Gesamtschaden = (((
        spieler.stats.PhysischerSchaden - funktionen.Angriff.AktuellerGegner.Rüstung)
          / 100 ) * funktionen.Angriff.AktuellerGegner.PhysischeResistenz)
    spieler.stats.Gesamtschaden = spieler.stats.Gesamtschaden + spieler.stats.PhysischerSchaden + spieler.stats.FeuerSchaden + spieler.stats.GiftSchaden
    funktionen.Angriff.AktuellerGegner.Gesamtschaden = funktionen.Angriff.AktuellerGegner.Gesamtschaden + funktionen.Angriff.AktuellerGegner.PhysischerSchaden + funktionen.Angriff.AktuellerGegner.FeuerSchaden + funktionen.Angriff.AktuellerGegner.GiftSchaden