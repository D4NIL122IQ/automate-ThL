# l'automate suivant reconnais un langage tel que anbm et m>n>0

import re;


def compterNbrCaractereSpecifique(mot,caractere):
    cmptCaractere =0;
    for lettre in mot :
        if lettre == caractere:
            cmptCaractere +=1;
    return cmptCaractere;

def appartenirAlphabet(mot):
    return bool(re.match(r'^[ab]+$',mot));

def queDesBDroite(mot):
    return bool(re.match(r'^[^b]*b[b]*$',mot))

def appartenirLagage(mot):
    if appartenirAlphabet(mot) == True:
        if queDesBDroite(mot) == True:
            if compterNbrCaractereSpecifique(mot , "b") > compterNbrCaractereSpecifique(mot , "a"):
                return True;
    else:
        return False;

chaine = input("entrez un mot pour verifier son appartenance au langage : ");

if len(chaine) == 0:
    print("le mot vide n'appartient pas a ce langage");
elif appartenirLagage(chaine) == True: 
    print("le mot appartient au langage");
else:
    print("le mot n'apprtient pas au langage");
