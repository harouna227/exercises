# L'utilisateur doit rentrer deux nombres
# On prend deux variable var1 et var2
# L'utilisateur doit entre l'opérateur(+, -, *, /)
# Affichage du resultat à l'écran

var1 = input('Entrer 1er nombre: ')
var2 = input("Entrer le second nombre: ")
operateur = input("Entrer l'opérateur: ")

if operateur:
    if operateur == '+':
        resul1 = int(var1) + int(var2)
        print("Le resultat: ", resul1)
    elif operateur == '-':
        resul2 = int(var1) - int(var2)
        print("Le resultat: ", resul2)
    elif operateur == '*':
        resul3 = int(var1) * int(var2)
        print("Le resultat: ", resul3)
    elif operateur == '/':
        resul4 = int(var1) / int(var2)
        print("Le resultat: ", resul4)
    else:
        print()
        print('Vous devez entrer soit +, -, * ou /')       
else:
    print()
    print("Vous n'avez rien entré comme opérateur de calcul \nVous devez entré soit +, -, * ou / ")