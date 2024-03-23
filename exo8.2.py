def saisieEntier(message):
    while True:
        try:
            entier = int(input(message))
            break  # Si l'utilisateur saisit un entier valide, sortir de la boucle
        except ValueError:
            print("Erreur : Veuillez saisir un entier valide.")

    return entier

def calculerDuree(distance, vitesse):
    try:
        if vitesse == 0:
            raise ZeroDivisionError("La vitesse ne peut pas être égale à zéro.")
        duree = distance / vitesse
        return duree
    except ZeroDivisionError as e:
        print("Erreur :", e)#e recupere lobj dans un var
        return None  # Retourner None en cas d'erreur

# Saisie de la distance à parcourir et de la vitesse moyenne
distance = saisieEntier("Entrez la distance à parcourir (en km) : ")
vitesse = saisieEntier("Entrez la vitesse moyenne (en km/h) : ")

# Calcul de la durée nécessaire pour parcourir la distance spécifiée à la vitesse spécifiée
duree = calculerDuree(distance, vitesse)
if duree is not None:
    print("Durée nécessaire pour parcourir la distance spécifiée à la vitesse spécifiée :", duree, "heures.")
