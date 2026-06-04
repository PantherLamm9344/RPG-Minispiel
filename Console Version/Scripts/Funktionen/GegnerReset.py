import Scripts.Gegner.Gegner as Gegner
from random import randrange



#-----------------------------------------------------
# Funktion zum Reseten der Gegner
#-----------------------------------------------------
def GegnerResetWaldgebiet():
    Gegner.gnom.hp_current = Gegner.gnom.hp_current + Gegner.gnom.hp_start
    Gegner.kobold.hp_current = Gegner.kobold.hp_current + Gegner.kobold.hp_start
    Gegner.gnom.drop_gnommuetzen = 0
    Gegner.gnom.drop_gnommuetzen = randrange(3)
    Gegner.kobold.drop_koboldohr = 0
    Gegner.kobold.drop_koboldohr = randrange(3)
    print(" *   *             *      *        *  *     *")
    print(" *     *              *           *        * ")
    print("    *     *       *        *     *     *    *")
    print(" *   *             *      *        *  *     *")
    print()
    print("Du rastest und ruhst dich aus. In der Nacht wachst du wegen geräusche von Kreaturen wieder auf.")
    print("Anscheinend sind wieder Monster aufgetaucht, und du beendest deine Rast.")
    print()
    print()
    Stopper = input("... ")

def GegnerResetBerggebiet():
    Gegner.Oger.hp_current  = Gegner.Oger.hp_current + Gegner.Oger.hp_start
    Gegner.Troll.hp_current = Gegner.Troll.hp_current + Gegner.Troll.hp_start
    Gegner.Koboldhauptmann.hp_current   = Gegner.Koboldhauptmann.hp_current + Gegner.Koboldhauptmann.hp_start
    Stopper = input("... ")
