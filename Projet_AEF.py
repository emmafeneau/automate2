import pandas as pd
import numpy as np
from pprint import pprint


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

    return AEF, alphabets, n

def supprimerAEF(AEF):
    AEF.clear()
    
def complementAEF(AEF):
    AEF_C = AEF
    for etat in AEF_C:
        if etat["final"] == True:
            etat["final"] = False
        else:
            etat["final"] = True
    return AEF_C
            
def miroir(AEF):
    temp_AEF = AEF
    for etat in temp_AEF:
        if etat["final"] and etat["initial"]:
            etat["initial"] = True
            etat["final"] = True
        elif etat["final"]:
            etat["initial"] = True
            etat["final"] = False
        elif etat["initial"]:
            etat["final"] = True
            etat["initial"] = False
            
        del etat["final"], etat["initial"]
        
        count = 0
        dictionnaire = {}
        AEF_M=[]
        
        for item in temp_AEF:
            pprint(item)
            for transitions, dest in item.items():
                myList = []
                for valeur in dest:
                    myList.append(dest)
                dictionnaire[transitions] = myList
            AEF_M.append(dictionnaire)
            count += 1
        
    
    #    pprint(AEF_M[idx])
        
    #    for transitions in etat[idx].keys():
     #       for dest in etat[idx][transitions]:
     #           AEF_M[dest][transitions] = idx
                
                    
        
        
    #    cles = etat.keys()
        
     #   count = 0
        
       # for cle in cles:
       #     print("cle", cle)
        #    for dest in etat[cle]:
                
           #     print("dest", dest)
          #      index = ord(cle)
          #      AEF_M[dest][count] = etat
          #  count += 1
        
    return AEF_M
        
        
            

def estDeterministe(AEF):
    for etat in AEF:
        cles=etat.keys()
        for cle in cles:
            if len(etat[cle])>1:
                return False
    return True

def Rendre_Deterministe(AEF):
    AEF_D = AEF
    if estDeterministe(AEF):
        print("L'AEF est déjà déterministe")
        return AEF
    else:
        for alphabet in alphabets:
            AEF[0][alphabet] = 0

def estComplet(AEF):
    for etat in AEF:
        cles=etat.keys()
        for cle in cles:
            if len(etat[cle])==0:
                return False
    return True

def Rendre_Complet(AEF, alphabets):
    AEF_Complet = AEF
    if estComplet(AEF):
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
                    etat[alphabet] = [len(AEF_Complet) - 1]
                    
        phi["final"] = False
        phi["initial"] = False
        return AEF_Complet
  
def Afficher_AEF(AEF):
    print("AEF saisi :")
    for i, etat in enumerate(AEF):
        print(f"{i} = {etat}")

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
        print("0. Quitter")

        choice = input("Entrez votre choix : ")

        if choice == '1':
            aef, alphabets, nb_etats = saisir_AEF()
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
            if estComplet(aef):
                print("L'AEF est complet")
            else:
                print("L'AEF n'est pas complet")    
        elif choice == '7':
            aef_complet = Rendre_Complet(aef, alphabets)
            print("L'AEF a été rendu complet")   
        elif choice == '8':
            if estDeterministe(aef):
                print("L'AEF est déterministe")
            else:
                print("L'AEF n'est pas déterministe")
        elif choice == '9':
            aef = rendreDeterministe(aef, alphabets)
            print("L'AEF a été rendu déterministe")
        elif choice == '10':
            Afficher_AEF(aef)
        elif choice == '11':
            supprimerAEF(aef)
            print("L'AEF a été supprimé")
        elif choice == '12':
            aef_c = complementAEF(aef)
            print("Complément de l'AEF")
        elif choice == '13':
            aef_m = miroir(aef)
            print("Miroir de l'AEF")
        elif choice == '0':
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")
