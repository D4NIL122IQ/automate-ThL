#aibjckbm / m >= k >j>= i>=0

import re;

def ordreSansMelange(mot:str) -> bool:
    return bool(re.match(r'^(a*b*c*d*)$',mot))

def compterNbrCaractere(mot : str, caractere : str) -> int:
    nbrcara = 0;
    for carac in mot :
        if carac == caractere :
             nbrcara += 1;
    return nbrcara;

def appartenirLangage(mot):
    if ordreSansMelange(mot) == True:
        if compterNbrCaractere(mot , "a") <= compterNbrCaractere(mot ,"b" ) < compterNbrCaractere(mot , "c") <= compterNbrCaractere(mot ,"d" ):
            return True;


chaine = input("entrez un mot : ")
if(len(chaine)== 0):
    print("le mot vide n'appartient pas !");
elif appartenirLangage(chaine) == True:
    print("il appartient au langage");
else:
    print("il n'appartient pas au langage");