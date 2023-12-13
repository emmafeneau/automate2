#import pandas as pd
#import numpy as np
import copy

def saisir_AEF():
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

    return AEF, alphabets, etats_finaux

def supprimerAEF(AEF):
    AEF.clear()
    
def complementAEF(AEF):
    AEF_C = [copy.deepcopy(etat) for etat in AEF]
    for etat in AEF_C:
        if etat["final"]:
            etat["final"] = False
        else:
            etat["final"] = True
    return AEF_C
            
def miroir(AEF, symboles): 
    count = 0
    for etat in AEF:
        if etat["final"]:
            count += 1
    if count > 1:
        print("Transformation impossible : l'AEF contient plusieurs états finaux")
        return AEF
    
    AEF_M = [copy.deepcopy(etat) for etat in AEF]

    for etat in AEF_M:
        for symbole in symboles:
            etat[symbole] = []

    for i, etat in enumerate(AEF_M):
        if etat["final"] and etat["initial"]:
            etat["initial"] = True
            etat["final"] = True
        elif etat["final"]:
            etat["initial"] = True
            etat["final"] = False
        elif etat["initial"]:
            etat["final"] = True
            etat["initial"] = False
        
        
        for symbole in symboles:
            dest_list = AEF[i][symbole]
            if dest_list:
                for dest in dest_list:
                        AEF_M[dest][symbole].append(i)
    
    print("Le miroir de l'AEF a été généré")
    return AEF_M
        
def estDeterministe(AEF, symboles):
    for etat in AEF:
        for symbole in symboles:
            if len(etat[symbole])>1:
                return False
    return True

def rendre_deterministe(AEF, alphabets, etats_finaux):
    if estDeterministe(AEF, alphabets):
        return AEF
    
    AEF_det = []  # Nouvel AEF déterministe vide
    file = []  # File pour stocker les nouveaux états à traiter
    dico = {}  # Dictionnaire pour associer les nouveaux états à des indices
    indice = 0  # Compteur d'indices initialisé

    etat_initial = [0]  # l'état initial est toujours 0 par défaut
    
    file.append(etat_initial)  
    dico[tuple(etat_initial)] = indice
    indice += 1
    AEF_det.append({alphabet:[] for alphabet in alphabets})  # Ajoute l'état initial à l'AEF déterministe avec la même structure qu'un AEF

    while file:  # Tant qu'il y a des états à traiter dans la file
        etat_courant = file.pop(0)  # le premier état de file va dans etat_courant
        for alphabet in alphabets:  # Pour chaque symbole de l'alphabet
            etat_suivant = []  # Ensemble des états accessibles depuis l'état courant avec ce symbole
            for i in etat_courant:  
                etat_suivant.extend(AEF[i][alphabet]) # rajoute les éléments séparemment dans etat_suivant
            etat_suivant = list(set(etat_suivant))  # set va éliminer les doublons dans etat_suivant
            if etat_suivant:  # Si cet ensemble n'est pas vide
                if tuple(etat_suivant) not in dico:  # Si cet état n'a pas encore été traité
                    dico[tuple(etat_suivant)] = indice
                    indice += 1
                    file.append(etat_suivant)
                    AEF_det.append({alphabet:[] for alphabet in alphabets})  # Ajoute un nouvel état à l'AEF déterministe avec la même structure qu'un AEF
                AEF_det[dico[tuple(etat_courant)]][alphabet] = [dico[tuple(etat_suivant)]]  # Ajoute la transition sous forme de liste

    for etat in dico:  # Détermine les états finaux de l'AEF déterministe
        final = False
        for i in etat:
            if str(i) in etats_finaux:
                final = True 
                break
        AEF_det[dico[etat]]["final"] = final
        AEF_det[dico[etat]]["initial"] = False
    
    AEF_det[0]["initial"] = True
    
    return AEF_det



def estComplet(AEF, symboles):
    for etat in AEF:
        for symbole in symboles:
            if len(etat[symbole])==0:
                return False
    return True

def Rendre_Complet(AEF, alphabets):
    AEF_Complet = [copy.deepcopy(etat) for etat in AEF]
    if estComplet(AEF, alphabets):
        print("L'AEF est déjà complet")
        return AEF
    else:
        phi = {}
        for alphabet in alphabets:
            phi[alphabet] = [len(AEF_Complet)]
        AEF_Complet.append(phi)
        for etat in AEF_Complet:
            for alphabet in alphabets:
                if len(etat[alphabet])==0:
                    etat[alphabet] = [len(AEF_Complet) - 1] # car on ajouté l'état phi
                    
        phi["final"] = False
        phi["initial"] = False
        return AEF_Complet
  
def Afficher_AEF(AEF):
    print("AEF saisi :")
    for i, etat in enumerate(AEF):
        print(f"{i} = {etat}")

def Affichage(AEF, symboles):
    print(f"Nombre d'états : {len(AEF)}")
    print("Etat initial : q0")
    etats_finaux = [i for i, etat in enumerate(AEF) if etat["final"]]
    print("Etats finaux :", ", ".join(f"q{etat}" for etat in etats_finaux))
    print("Symboles de l'AEF :", ", ".join(f"{symbole}" for symbole in symboles))
    print("Transitions : ")
    for i, etat in enumerate(AEF):
        for symbole, destinations in etat.items():
            if symbole not in ["final", "initial"]:
                for dest in destinations:
                    print(f"q{i} -{symbole}-> q{dest} ")

def expression_reguliere_from_aef(aef):
    # Initialisation de la matrice de transition
    n = len(aef)
    matrice_transition = [[''] * n for _ in range(n)]

    # Remplissage de la matrice de transition
    for i in range(n):
        for j in range(n):
            transitions = []
            for symbole, destinations in aef[i].items():
                # Exclure les clés "final" et "initial"
                if symbole not in ["final", "initial"]:
                    for dest in destinations:
                        transitions.append(symbole)
            # Construction de la partie initiale de l'expression pour cet état
            matrice_transition[i][j] = f"({'|'.join(transitions)})"

    # Application du lemme d'Arden
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Utilisation du lemme d'Arden pour mettre à jour la matrice de transition
                matrice_transition[i][j] = f"({matrice_transition[i][j]}|({matrice_transition[i][k]}({matrice_transition[k][k]})*{matrice_transition[k][j]}))"

    # La solution est dans la diagonale de la matrice
    expression_reg = [matrice_transition[i][i] for i in range(n)]

    return expression_reg[0]


#aef = [{'a': [0,1], 'b': [], 'final' : False, 'initial' : True}, {'a': [1], 'b': [1], 'final' : True, 'initial' : False}]

mesAEF = []
# Programme principal
if __name__ == "__main__": 
    while True: 
        print("\nMenu :")
        print("1. Saisir un AEF")
        print("2. Importer un AEF depuis un fichier")
        print("3. Sauvegarder un AEF dans un fichier")
        print("4. Modifier un AEF")
        print("5. Vérifier si un mot est reconnu par un AEF")
        print("6. Vérifier si un automate est complet")
        print("7. Rendre un automate complet")
        print("8. Vérifier si un automate est déterministe")
        print("9. Rendre un AEF déterministe")
        print("10. Afficher l'AEF")
        print("11. Supprimer l'AEF")
        print("12. Complément de l'AEF")
        print("13. miroir")
        print("14. Extraire l'expression régulière d'un AEF")
        print("0. Quitter")

        choice = input("Entrez votre choix : ")

        if choice == '1':
            aef, symboles, etats_finaux = saisir_AEF()
            mesAEF.append(aef)
        elif choice == '2':
            aef = Importer_AEF(input("Saisir le nom du fichier à importer : "))
            print("AEF importé :")
            #Afficher_AEF(aef)    
        elif choice == '3':
            filename = input("Entrez le nom du fichier pour la sauvegarde : ")
            sauvegarder_AEF(aef, filename)    
        elif choice == '4':
            modifier_AEF(aef)
        elif choice == '5':
            mot = input("Entrez un mot à vérifier : ")
            if is_accepted(aef, mot):
                print("Le mot est reconnu par l'AEF.")
            else:
                print("Le mot n'est pas reconnu par l'AEF.")
        elif choice == '6':
            if estComplet(aef, symboles):
                print("L'AEF est complet")
            else:
                print("L'AEF n'est pas complet")    
        elif choice == '7':
            aef_complet = Rendre_Complet(aef, symboles)
            print("L'AEF a été rendu complet")  
            mesAEF.append(aef_complet) 
        elif choice == '8':
            if estDeterministe(aef, symboles):
                print("L'AEF est déterministe")
            else:
                print("L'AEF n'est pas déterministe")
        elif choice == '9':
            aef_deterministe = rendre_deterministe(aef, symboles, etats_finaux)
            print("L'AEF a été rendu déterministe")
            mesAEF.append(aef_deterministe)
            
        elif choice == '10':
            #Afficher_AEF(aef)
            #Afficher_AEF(aef_deterministe)
            print(mesAEF)
            indice = int(input("Choisissez l'indice de l'aef que vous voulez afficher : "))
            Affichage(mesAEF[indice], symboles)

        elif choice == '11':
            supprimerAEF(aef)
            print("L'AEF a été supprimé")
        elif choice == '12':
            aef_c = complementAEF(aef)
            mesAEF.append(aef_c)
            print("Complément de l'AEF")
        elif choice == '13':
            # aef = [{'a': [0,1], 'b': [1], 'final': True, 'initial': True},
            #         {'a': [1], 'b': [0], 'final': True, 'initial': False}, 
            #         {'a': [2], 'b': [0,2],'final': False, 'initial': False}]
            aef_m = miroir(aef, symboles)
            mesAEF.append(aef_m)
        elif choice == '14':
            expression_reguliere = expression_reguliere_from_aef(aef)
            print("Expression régulière:", expression_reguliere)

        elif choice == '0':
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")
