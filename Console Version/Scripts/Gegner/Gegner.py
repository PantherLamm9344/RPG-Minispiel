import Scripts.Werte.Stats as Stats
from random import randrange
#---------------------------------
#------- GEGNER DATEN ------------
#---------------------------------
placeholder = Stats.Gegner()
placeholder.name = "placeholder"
placeholder.hp_max = 0
placeholder.hp_current = 0
placeholder.hp_start = 0
placeholder.hp_min = 0
placeholder.Gesamtschaden = 0
placeholder.PhysischerSchaden = 0
placeholder.GiftSchaden = 0
placeholder.FeuerSchaden = 0
placeholder.Rüstung = 0
placeholder.PhysischeResistenz = 0
placeholder.GiftResistenz = 0
placeholder.FeuerResistenz = 0



gnom = Stats.Gegner()
gnom.name = "Gnom"
gnom.hp_max = 75
gnom.hp_current = 50
gnom.hp_start = 50
gnom.hp_min = 0
gnom.Gesamtschaden = 0
gnom.PhysischerSchaden = 5
gnom.GiftSchaden = 0
gnom.FeuerSchaden = 0
gnom.Rüstung = 0
gnom.PhysischeResistenz = 0
gnom.GiftResistenz = 0
gnom.FeuerResistenz = 0
gnom.drop_gnommuetzen = randrange(3)



kobold = Stats.Gegner()
kobold.name = "Kobold"
kobold.hp_max = 50
kobold.hp_current = 25
kobold.hp_start = 25
kobold.hp_min = 0
kobold.Gesamtschaden = 0
kobold.PhysischerSchaden = 9
kobold.GiftSchaden = 0
kobold.FeuerSchaden = 0
kobold.Rüstung = 5
kobold.PhysischeResistenz = 0
kobold.GiftResistenz = 0
kobold.FeuerResistenz = 0
kobold.drop_koboldohr = randrange(3)



Oger = Stats.Gegner()
Oger.name = "Oger"
Oger.hp_max = 50
Oger.hp_current = 25
Oger.hp_start = 25
Oger.hp_min = 0
Oger.Gesamtschaden = 0
Oger.PhysischerSchaden = 12
Oger.GiftSchaden = 0
Oger.FeuerSchaden = 0
Oger.Rüstung = 3
Oger.PhysischeResistenz = 0
Oger.GiftResistenz = 0
Oger.FeuerResistenz = 0
Oger.drop_OgerZahn = 3



Troll = Stats.Gegner()
Troll.name = "Troll"
Troll.hp_max = 150
Troll.hp_current = 100
Troll.hp_start = 100
Troll.hp_min = 0
Troll.Gesamtschaden = 0
Troll.PhysischerSchaden = 14
Troll.GiftSchaden = 0
Troll.FeuerSchaden = 0
Troll.Rüstung = 7
Troll.PhysischeResistenz = 0
Troll.GiftResistenz = 0
Troll.FeuerResistenz = 0
Troll.drop_Trollhaut = 2



Koboldhauptmann = Stats.Gegner()
Koboldhauptmann.name = "Koboldhauptmann"
Koboldhauptmann.hp_max = 125
Koboldhauptmann.hp_current = 100
Koboldhauptmann.hp_start = 100
Koboldhauptmann.hp_min = 0
Koboldhauptmann.Gesamtschaden = 0
Koboldhauptmann.PhysischerSchaden = 13
Koboldhauptmann.GiftSchaden = 0
Koboldhauptmann.FeuerSchaden = 0
Koboldhauptmann.Rüstung = 5
Koboldhauptmann.PhysischeResistenz = 0
Koboldhauptmann.GiftResistenz = 0
Koboldhauptmann.FeuerResistenz = 0
Koboldhauptmann.drop_koboldohr = 4