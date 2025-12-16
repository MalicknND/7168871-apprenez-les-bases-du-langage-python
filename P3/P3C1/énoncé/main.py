# Ecrivez votre code ici !
from operations import addition, multiplication

num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le deuxième nombre : "))

somme = addition(num1, num2)
produit = multiplication(num1, num2)

print(f"La somme de {num1} et {num2} est : {somme}")
print(f"Le produit de {num1} et {num2} est : {produit}")
