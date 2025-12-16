# Écrivez votre code ici !

fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange"
}

# Ajout de la clé "kiwi" avec la valeur "vert"
fruits["kiwi"] = "vert"
print(fruits)

# Accès à la valeur correspondant à la clé "banane"
couleur_banane = fruits["banane"]
print(couleur_banane)

# Modification de la valeur associée à la clé "pomme"
fruits["pomme"] = "vert"
print(fruits)

# Suppression de la clé "banane"
del fruits["banane"]
print(fruits)

# Affichage des clés restantes dans le dictionnaire
print(fruits.keys())
