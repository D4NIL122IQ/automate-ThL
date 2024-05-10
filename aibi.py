# cet automate reconnais aibi tel que i>=0 et e represente le mot vide
import re;

#pour verifier que la chaine de caractere contient que l'alphabet de mon langage
def appartenirLangage(mot):
    return bool(re.match(r'^(?=.*a)(?=.*b)[ab]*$',mot))

def partiedeDroite(chaine):
    motif = r'^[^b]*b[b]*$'
    return bool(re.match(motif, chaine))

def motDuLangage(mot):
    if appartenirLangage(mot) == True:
        if mot.find("b") == int(len(mot)/2):
            if partiedeDroite(mot):
                return True;
    else: 
        return False; 


mot = input("entrez un mot dans le langage aibi : ")


if mot == "e":
    print(mot +" apartient au langage")
elif motDuLangage(mot) == True:
    print(mot +" appartient au langage");
else:
    print(mot+" n'appartient pas au langage");