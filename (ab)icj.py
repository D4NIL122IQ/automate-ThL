#(ab)icj / i,j>0

import re;

def ordreSansMelange(mot):
    return bool(re.match(r'^((ab)+c+)$',mot));

def appartenirLangage(mot):
    if ordreSansMelange(mot) == True:
        return True;

chaine = input("entrez un mot : ")
if(len(chaine)== 0):
    print("le mot vide n'appartient pas !");
elif appartenirLangage(chaine) == True:
    print("il appartient au langage");
else:
    print("il n'appartient pas au langage");