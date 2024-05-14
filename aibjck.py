# aibjck / i,j,k>0

import re;

def ordreSansMelange(mot : str) -> bool :
    return bool(re.match(r'^(a*b*c*)$' , mot))

def appartenirLangage(mot : str) -> bool:
    if ordreSansMelange(mot) == True:
        return True;

chaine = input("entrez un mot : ")

if(len(chaine)== 0):
    print("le mot vide n'appartient pas !");
elif appartenirLangage(chaine) == True:
    print("il appartient au langage");
else:
    print("il n'appartient pas au langage");