"""
 saisie d’un entier avec gestion des erreurs
Ecrire un programme permettant de saisir un entier. Si l’utilisateur saisit autre chose qu’un entier,
afficher un message d’erreur en gérant l’exception ValueError. Le programme doit boucler
jusqu’à ce que l’utilisateur saisisse bien un entier
"""
def saisieEntier():
    while True:
        try:
            entier = int(input("enter val:"))
            break  # Si l'utilisateur saisit un entier valide, sortir de la boucle
        except ValueError:
            print("Veuillez saisir un entier valide.")

    print("Vous avez saisi un entier valide :", entier) 
saisieEntier()



    
