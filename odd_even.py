# 1. Utilisateur doit rentre un nombre entier(int)
# 2. Vérification du nombre si c'est pair ou impair
# 3. Un nombre est pair si la division entiére du nombre par 2 donne zéro
# 4. Un nombre est impair si la division entiére du nombre par est différent de zéro


# Une Vraible est conteneur
# str -> une chaine de caratere
# int -> un entier
# float -> un nombre decimal (nombre à virgule)
# bool -> renvoi vrai ou faux
# le modulo -> %

# Instruction conditionnelle (si...sinon)


variable = (input('Entre le nombre entier ')) # renvoit une chaine de caratere 

if isinstance(variable, int):
    if variable % 2 == 0:
        print("Le nombre entré par l'utilisateur est pair")
    else:
        print("Le nombre entré par l'utilisateur est impair")
else:
    print('Vous devez entrer un nombre entier!')


