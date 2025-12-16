# Ecrivez votre code ici !
# Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules (par exemple : "1,2,3,4").

nombres_str = input(
    "Veuillez saisir une liste de nombres séparés par des virgules : ")
nombres_str_list = nombres_str.split(",")
# Convertissez cette chaîne de caractères en une liste de nombres entiers.
nombres = [int(nombre) for nombre in nombres_str_list]
# Calculez la somme de ces nombres.
somme = sum(nombres)
# Affichez le résultat à l'utilisateur.
print("La somme des nombres est :", somme)

# calculer la moyenne des nombres
moyenne = somme / len(nombres)
print("La moyenne des nombres est :", moyenne)

# calculer et afficher le nombre de nombres dans la liste qui sont supérieurs à la moyenne
nombres_sup_moyenne = [nombre for nombre in nombres if nombre > moyenne]
print("Le nombre de nombres supérieurs à la moyenne est :", len(nombres_sup_moyenne))
