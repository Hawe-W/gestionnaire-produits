#=====================================
#GESTIONNAIRE DE PRODUIT
#=====================================

def produit_cher(prix):

    return prix >= 100


produits = []

nombre = int(input("Combien de produit ?"))

for i in range(nombre):

    nom = input("Nom du produit : ")
    prix = float(input("Prix : "))

    produit = {
        "nom": nom,
        "prix": prix
    }

    produits.append(produit)

print()
print("---------- PRODUITS CHERS ----------")

for produit in produits:

    if produit_cher(produit["prix"]):

        print(produit)