def saisir_AEF():
    # un aef est une liste d'états représentés par des dictionnaires
    AEF = []
    alphabets = input("Symboles de l'alphabet (séparés par des espaces) : ").split()
    n = int(input("Combien d'états dans l'AEF : "))
    etats_finaux = input("États finaux (séparés par des espaces) : ").split()

    for i in range(n):
        etat = {}
        print(f"État {i} :")
        for alphabet in alphabets:
            transitions = input(f"États atteints avec '{alphabet}' (séparés par des espaces) : ").split()
            if transitions:
                etat[alphabet] = [int(indice) for indice in transitions]
            else:
                etat[alphabet] = []
        
        if (str(i) in etats_finaux):
            etat["final"] = True
            etat["initial"] = False
        else :
            etat["final"] = False
            etat["initial"] = False
        AEF.append(etat)

    # Par défaut, on prend l'état 0 comme état initial
    AEF[0]["initial"] = True

    return AEF

def symbole_aef(aef):
    symboles = set()

    for etat in aef:
        symboles.update(etat.keys())

    # Retire les clés "final" et "initial" des symboles
    symboles.discard('final')
    symboles.discard('initial')

    return sorted(list(symboles)) #range dans l'orde alphabétique

def Affichage(AEF):
    print(f"Nombre d'états : {len(AEF)}")
    etat_initial = [j for j, etat in enumerate(AEF) if etat["initial"]] # on récupère liste etats initiaux
    print("Etat initial : ", ", ".join(f"q{etat}" for etat in etat_initial))
    etats_finaux = [i for i, etat in enumerate(AEF) if etat["final"]] # on récupère liste etats finaux
    print("Etats finaux :", ", ".join(f"q{etat}" for etat in etats_finaux))
    symboles = symbole_aef(AEF)
    print("Symboles de l'AEF :", ", ".join(f"{symbole}" for symbole in symboles))
    print("Transitions : ")
    for i, etat in enumerate(AEF):
        for symbole, destinations in etat.items():
            if symbole not in ["final", "initial"]:
                for dest in destinations:
                    print(f"q{i} -{symbole}-> q{dest} ")
    

# Programme principal
mesAEF = [] # Liste contenant tous les aef généres
if __name__ == "__main__": 
    while True: 
        print("\nMenu :")
        print("1. Saisir un AEF")
        print("2. Afficher l'AEF")
        print("0. Quitter")

        choice = input("Entrez votre choix : ")

        if choice == '1':
            aef = saisir_AEF()
            mesAEF.append(aef)

        elif choice == '2':
            for i, aef in enumerate(mesAEF):
                print(f"AEF n°{i} : {aef}")
            indice = int(input("Choisissez le numero de l'aef que vous voulez afficher : "))
            Affichage(mesAEF[indice])

        elif choice == '0':
            break
        
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")
