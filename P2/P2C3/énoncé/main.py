# Ecrivez votre code ici

def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12


def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4


def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees


salaire_annuel = float(input("Entrez votre salaire annuel    : "))
nombre_heures = float(
    input("Entrez le nombre d'heures travaillées par semaine : "))

mensuel = salaire_mensuel(salaire_annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, nombre_heures)
print(f"Salaire mensuel  : {mensuel:.2f} ")
print(f"Salaire hebdomadaire : {hebdomadaire:.2f} ")
print(f"Salaire horaire : {horaire:.2f} ")
print("Merci d'avoir utilisé le calculateur de salaire !")
