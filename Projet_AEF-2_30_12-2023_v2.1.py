
import copy

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

#emma 30-12-2023

def saisir_AEF_produit():
    AEF = []
    alphabets = input("Symboles de l'alphabet (séparés par des espaces) : ").split()
    n = int(input("Combien d'états dans l'AEF : "))
    etats_finaux = input("États finaux (séparés par des espaces) : ").split()

    for i in range(n):
        etat = {}
        etat["index"] = i
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

def supprimerAEF(AEF):
    print(f"Suppression du dernier AEF généré : {AEF}")
    AEF.clear()
    
def complementAEF(AEF):
    AEF_C = [copy.deepcopy(etat) for etat in AEF]
    for etat in AEF_C:
        if etat["final"]:
            etat["final"] = False
        else:
            etat["final"] = True
    return AEF_C

#emma 30-12-2023

def produit_AEF():

    #AEF_1 = saisir_AEF_produit()
    #AEF_2 = saisir_AEF_produit()
    #AEF_1 = [{"index" : 0,'a': [0], 'b': [1], 'final': False, 'initial': True},
               #{"index" : 1,'a': [0], 'b': [2], 'final': False, 'initial': False},
               #{"index" : 2,'a': [1], 'b': [], 'final': True, 'initial': False}]
    AEF_1 = [{"index" : 0,'a': [0,1], 'b': [], 'final': False, 'initial': True},
               {"index" : 1,'a': [], 'b': [1], 'final': True, 'initial': False}]
            
    
    for i, etat in enumerate(AEF_1):
                print(f"{i} = {etat}")

    AEF_2 = [{"index" : 0,'a': [1], 'b': [], 'final': False, 'initial': True},
               {"index" : 1,'a': [], 'b': [0], 'final': True, 'initial': False}]
    
    #AEF_2 = [{"index" : 0,'a': [], 'b': [1], 'final': False, 'initial': True},
               #{"index" : 1,'a': [0], 'b': [2], 'final': False, 'initial': False},
               #{"index" : 2,'a': [1], 'b': [], 'final': True, 'initial': False}]
    
    for i, etat in enumerate(AEF_2):
                print(f"{i} = {etat}")
    AEF_P = []
    
    for etat_1 in AEF_1:
        for etat_2 in AEF_2:
            
            #etats initiaux
            if etat_1["initial"] == True and etat_2["initial"] == True:
                etat_p = {}
                etat_p["initial"] = True
                etat_p["final"] = False
                
                for transition_1 in etat_1:
                    if transition_1 == "initial" or transition_1 == "final" or transition_1 == "index":
                        continue
                    for transition_2 in etat_2:
                        if transition_2 == "initial" or transition_2 == "final" or transition_2 == "index":
                            continue
                        if transition_1 == transition_2:
                            etat_p[transition_1] = []
                            if len(etat_1[transition_1]) > 0 and len(etat_2[transition_2]) > 0:
                                for item_1 in etat_1[transition_1]:
                                    for item_2 in etat_2[transition_2]:
                                        etat_p_1 = []
                                        etat_suivant_1 = item_1
                                        etat_suivant_2 = item_2                 
                                        etat_p_1.append(etat_suivant_1)
                                        etat_p_1.append(etat_suivant_2)
                                        etat_p[transition_1].append(etat_p_1)
                                      
                AEF_P.append(etat_p)
            #etats intermédiaires et finaux
            elif etat_1["index"] == etat_suivant_1 and etat_2["index"] == etat_suivant_2:
                etat_p = {}
                if etat_1["final"] == True and etat_2["final"] == True:
                    etat_p["initial"] = False
                    etat_p["final"] = True
                else:
                    etat_p["initial"] = False
                    etat_p["final"] = False

                for transition_1 in etat_1:
                    if transition_1 == "initial" or transition_1 == "final" or transition_1 == "index":
                        continue
                    for transition_2 in etat_2:
                        if transition_2 == "initial" or transition_2 == "final" or transition_2 == "index":
                            continue
                        
                        if transition_1 == transition_2:
                            etat_p[transition_1] = []
                            if len(etat_1[transition_1]) > 0 and len(etat_2[transition_2]) > 0:
                                   for item_1 in etat_1[transition_1]:
                                        for item_2 in etat_2[transition_2]:
                                            etat_p_1 = []
                                            etat_suivant_1 = item_1
                                            etat_suivant_2 = item_2
                                            etat_p_1.append(etat_suivant_1)
                                            etat_p_1.append(etat_suivant_2)
                                            etat_p[transition_1].append(etat_p_1)
                                           
                            
                AEF_P.append(etat_p)

    return AEF_P
            
def miroir(AEF): 
    count = 0
    for etat in AEF:
        if etat["final"]:
            count += 1
    if count > 1: # si l'état a plusieurs états finaux
        print("Transformation impossible : l'AEF contient plusieurs états finaux") # car on ne peut pas avoir plusieurs états initiaux avec notre modèle d'aef
        return AEF
    
    AEF_M = [copy.deepcopy(etat) for etat in AEF]

    symboles = symbole_aef(AEF)
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
                        AEF_M[dest][symbole].append(i) # on inverse le sens de la transition
    
    print("Le miroir de l'AEF a été généré")
    return AEF_M
        
def estDeterministe(AEF):
    symboles = symbole_aef(AEF)
    for etat in AEF:
        for symbole in symboles:
            if len(etat[symbole])>1: # si l'état un plusieurs destinations
                return False
    return True

def rendre_deterministe(AEF):
    
    AEF_det = []  # Nouvel AEF déterministe vide
    file = []  # File pour stocker les nouveaux états à traiter
    dico = {}  # Dictionnaire pour associer les nouveaux états à des indices
    indice = 0  # Compteur d'indices initialisé
    alphabets = symbole_aef(AEF)
    etat_initial = [0]  # l'état initial est toujours 0 par défaut
    etats_finaux = [i for i, etat in enumerate(AEF) if etat["final"]]

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
                if tuple(etat_suivant) not in dico:  # Si cet état n'a pas encore été traité (tuple nous permet de considérer plusieurs état comme un seul)
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

def estComplet(AEF):
    symboles = symbole_aef(AEF)
    for etat in AEF:
        for symbole in symboles:
            if len(etat[symbole])==0: # si l'état n'a aucune destination
                return False
    return True

def Rendre_Complet(AEF):
    AEF_Complet = [copy.deepcopy(etat) for etat in AEF]
    alphabets = symbole_aef(AEF)

    phi = {} # création de l'état puit
    for alphabet in alphabets:
        phi[alphabet] = [len(AEF_Complet)] # phi reboucle sur lui-même avec tous les symboles
    AEF_Complet.append(phi)
    for etat in AEF_Complet:
        for alphabet in alphabets:
            if len(etat[alphabet])==0: # si l'état n'est pas complet (aucune destination)
                etat[alphabet] = [len(AEF_Complet) - 1] # car on ajouté l'état phi
                
    phi["final"] = False
    phi["initial"] = False
    return AEF_Complet
  
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

def est_reconnu(aef, mot):
    symboles = symbole_aef(aef)
    etats_courants = {0}

    for symbole in mot:
        if symbole not in symboles:
            print(f"Le symbole '{symbole}' ne fait pas partie des symboles de l'aef.")
            return False

        nouveaux_etats = set()

        for etat in etats_courants:
            for nouvel_etat in aef[etat][symbole]:
                nouveaux_etats.add(nouvel_etat)

        etats_courants = nouveaux_etats


        if not etats_courants:
            return False

    return any(aef[etat]["final"] for etat in etats_courants)

def sauvegarder_aef(aef, nom_fichier):
    symboles = symbole_aef(aef)

    with open(nom_fichier, 'w') as fichier:
        # Écriture des symboles de l'alphabet
        fichier.write(','.join(symboles) + '\n')

        # Écriture du nombre d'états
        fichier.write(str(len(aef)) + '\n')

        # Écriture des états finaux
        etats_finaux = [str(i) for i, etat in enumerate(aef) if etat['final']]
        fichier.write(','.join(etats_finaux) + '\n')

        # Écriture des transitions pour chaque état
        for i, etat in enumerate(aef):
            transitions = []
            for symbole, destinations in etat.items():
                if symbole not in {'final', 'initial'}:
                    destinations_str = ','.join(map(str, destinations))
                    transitions.append(f"{symbole}:{destinations_str}")
            fichier.write(' '.join(transitions) + '\n')

def importer_aef(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()

    symboles = lignes[0].strip().split(',')  # Récupérer les symboles de l'alphabet
    nombre_etats = int(lignes[1].strip())  # Récupérer le nombre d'états

    # Initialiser l'automate
    aef = [{} for _ in range(nombre_etats)]

    # Ajouter les états finaux et initiaux
    etats_finaux = list(map(int, lignes[2].strip().split(',')))
    for etat_final in etats_finaux:
        aef[etat_final]['final'] = True

    # Marquer l'état 0 comme initial
    aef[0]['initial'] = True

    # Ajouter les transitions pour chaque état
    for i in range(3, len(lignes)):
        transitions_str = lignes[i].strip().split(' ')
        for transition_str in transitions_str:
            parts = transition_str.split(':')
            symbole = parts[0]
            destinations_str = parts[1] if len(parts) > 1 else ''
            destinations = [] if destinations_str == '' else list(map(int, destinations_str.split(',')))
            aef[i - 3][symbole] = destinations

    # Ajouter les clés "final" et "initial" à la fin de chaque dictionnaire
    for etat in aef:
        etat['final'] = etat.get('final', False)
        etat['initial'] = etat.get('initial', False)

    return aef, symboles

def ajouter_etat(aef):
    
    nouvel_etat = {}

    # Spécifier les transitions
    symboles = input("Symboles de transition (séparés par des espaces) : ").split()
    for symbole in symboles:
        destinations = list(map(int, input(f"États de destination pour '{symbole}' (séparés par des espaces) : ").split()))
        nouvel_etat[symbole] = destinations

    # Spécifier s'il est final et/ou initial
    nouvel_etat["final"] = input("Est-ce un état final ? (Oui/Non) : ").lower() == "oui"
    nouvel_etat["initial"] = input("Est-ce un état initial ? (Oui/Non) : ").lower() == "oui"

    # Ajouter le nouvel état à l'AEF
    aef.append(nouvel_etat)

    return aef

def modifier_aef(aef):
   
    print("\nActions disponibles:")
    print("1. Ajouter un état")
    print("2. Supprimer un état")
    print("3. Ajouter une transition")
    print("4. Supprimer une transition") 
    action = input("Choisissez une action : ")

    if action == "1":
        aef = ajouter_etat(aef)
    elif action == "2":
        etat = int(input("Indiquez l'index de l'état à supprimer : "))
        if aef[etat]["initial"] == True or aef[etat]["final"] == True:
            print("Impossible de supprimer un état final ou initial")
        elif 0 <= etat < len(aef):
            del aef[etat]
            for etat_courant in aef:
                for symbole, dest in etat_courant.items():
                    if symbole not in ["final", "initial"]:
                        etat_courant[symbole] = [d for d in dest if d != etat]
        else:
            print("Index d'état non valide.")
    elif action == "3":
        etat = int(input("Indiquez l'index de l'état : "))
        symbole = input("Indiquez le symbole de la transition : ")
        destinations = list(map(int, input("Indiquez les états de destination (séparés par des espaces) : ").split()))
        if 0 <= etat < len(aef):
            if symbole in aef[etat]:
                aef[etat][symbole] += destinations  # Ajouter les destinations sans supprimer les anciennes
            else:
                aef[etat][symbole] = destinations
        else:
            print("Index d'état non valide.")
    elif action == "4":
        etat = int(input("Indiquez l'index de l'état : "))
        symbole = input("Indiquez le symbole de la transition à supprimer : ")
        if 0 <= etat < len(aef) and symbole in aef[etat]:
            aef[etat][symbole] = []
        else:
            print("Index d'état non valide ou symbole de transition non trouvé.")
    else:
        print("Action non reconnue.")

    return aef

def supprimer_etat(aef, etat):
    if etat == 0: # on ne peut pas supprimer l'état initial
        return
    
    del aef[etat]
    for etat_courant in aef:
        for symbole, dest in etat_courant.items():
            if symbole not in ["final", "initial"]:
                etat_courant[symbole] = [d for d in dest if d != etat] # on supprime l'état dans les destinations

def est_accessible(aef, indice_etat):
    # accessible = chemin de 0 vers i
    liste_etats_accessibles = []

    for i in range(len(aef)):
        for symbole, destinations in aef[i].items(): # on accède à l'état 
            if symbole not in ["final", "initial"]:
                for dest in destinations:
                    if i == 0: # car tt les dest de etat0 sont etats accessibles
                        liste_etats_accessibles.append(dest)
                    elif i in liste_etats_accessibles:
                        liste_etats_accessibles.append(dest)
    
    if indice_etat in liste_etats_accessibles:
        return True
    else:
        return False

def est_coaccessible(aef, indice_etat):
    # coaccessible = chemin de i vers un etat final
    liste_etats_coaccessibles = []
    liste_etats_finaux = [i for i, etat in enumerate(aef) if etat["final"]]

    for i in range(len(aef)):
        for symbole, destinations in aef[i].items(): # on accède à l'état 
            if symbole not in ["final", "initial"]:
                for dest in destinations:
                    if dest in liste_etats_finaux: # si l'etat i va vers un etat final
                        liste_etats_coaccessibles.append(i)
                    elif dest in liste_etats_coaccessibles: # si l'etat i va vers un etat co-accessible
                        liste_etats_coaccessibles.append(i)
    
    if indice_etat in liste_etats_coaccessibles:
        return True
    else:
        return False

def rendre_emonde(aef):
    aef_emonde = aef.copy()
    etats_a_supp = []

    for i, etat in enumerate(aef):
        if not est_accessible(aef, i) or not est_coaccessible(aef, i): # on supp etats non accessibles ou bien non co-accessibles
            etats_a_supp.append(i)

    etats_a_supp.sort(reverse=True) # on range dans ordre décroissant pour supp les états par la fin 
    for j in etats_a_supp:
        supprimer_etat(aef_emonde, j)

    return aef_emonde  

# Programme principal
mesAEF = []
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
        print("13. Miroir de l'AEF")
        print("14. Extraire l'expression régulière d'un AEF")
        print("15. Rendre un AEF émondé")
        print("16. Faire le produit de deux AEFs")
        print("0. Quitter")

        choice = input("Entrez votre choix : ")

        if choice == '1':
            aef = saisir_AEF()
            mesAEF.append(aef)
        
        elif choice == '2':
            aef, symboles = importer_aef('H:/Desktop/ING 1/05 - Python/aef_22.txt')
            print("L'AEF a été importé") 
            mesAEF.append(aef)  
        
        elif choice == '3':
            sauvegarder_aef(aef, 'H:/Desktop/ING 1/05 - Python/aef_22.txt') 
            print("L'AEF a été sauvegardé") 
         
        elif choice == '4':
            aef = modifier_aef(aef)
        
        elif choice == '5':
            mot = input("Entrez un mot à vérifier : ")
            if est_reconnu(aef, mot):
                print("Le mot est reconnu par l'AEF.")
            else:
                print("Le mot n'est pas reconnu par l'AEF.") 
        
        elif choice == '6':
            if estComplet(aef):
                print("L'AEF est complet")
            else:
                print("L'AEF n'est pas complet")    
        
        elif choice == '7':
            if estComplet(aef):
                print("L'AEF est déjà complet")
            else: 
                aef_complet = Rendre_Complet(aef)
                print("L'AEF a été rendu complet")
                mesAEF.append(aef_complet)
        
        elif choice == '8':
            if estDeterministe(aef):
                print("L'AEF est déterministe")
            else:
                print("L'AEF n'est pas déterministe")
        
        elif choice == '9':
            if estDeterministe(aef):
                print("L'AEF est déjà déterministe")
            else: 
                aef_deterministe = rendre_deterministe(aef)
                print("L'AEF a été rendu déterministe")
                mesAEF.append(aef_deterministe)

        elif choice == '10':
            for i, aef in enumerate(mesAEF):
                print(f"AEF n°{i} : {aef}")
            indice = int(input("Choisissez le numero de l'aef que vous voulez afficher : "))
            Affichage(mesAEF[indice])

        elif choice == '11':
            supprimerAEF(aef)
            mesAEF.remove(aef)
        
        elif choice == '12':
            aef_c = complementAEF(aef)
            mesAEF.append(aef_c)
            print("Le complément de l'AEF a été généré")
        
        elif choice == '13':
            aef_m = miroir(aef)
            mesAEF.append(aef_m)
        
        elif choice == '14':
            """ # aef_d = rendre_deterministe(aef, symboles, etats_finaux)
            aef = [{'a': [0], 'b': [1], 'final': False, 'initial': True},
               {'a': [2], 'b': [0], 'final': False, 'initial': False},
               {'a': [1], 'b': [2], 'final': True, 'initial': False}]
            expression_reguliere = arden_lemma(aef)
            print(expression_reguliere) """

        elif choice == '15':
            aef_emonde = rendre_emonde(aef)
            mesAEF.append(aef_emonde)
            print("L'émondé de l'AEF a été généré")

            #emma 30-12-2023
            
        elif choice == '16':
            aef = produit_AEF()

         
            
            for i, etat in enumerate(aef):
                print(f"{i} = {etat}")
            print("Voici le produit des deux aefs saisis")

        elif choice == '0':
            break
        
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")
