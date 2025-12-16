# Ecrivez votre code ici !

nombre1 = (input("Entrez le premier nombre entier : "))
nombre2 = (input("Entrez le deuxième nombre entier : "))

if nombre1.isnumeric() and nombre2.isnumeric():
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)
else:
    raise SystemExit(
        "Fin du programme. Veuillez entrer des nombres entiers valides.")

operation = input("Entrez l'opération (+, -, *, /) : ")

match operation:
    case "+":
        resultat = nombre1 + nombre2
    case "-":
        resultat = nombre1 - nombre2
    case "*":
        resultat = nombre1 * nombre2
    case "/":
        if nombre2 != 0:
            resultat = nombre1 / nombre2
        else:
            raise SystemExit("Erreur : Division par zéro.")
    case _:
        raise SystemExit("Opération invalide.")
print(f"Le résultat de {nombre1} {operation} {nombre2} est : {resultat}")
