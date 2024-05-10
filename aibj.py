# cet automate reconnais aibj tel que j,i>=0 et e represente le mot vide
import re;

def appartenirLangage(mot):
    return bool(re.match(r'^[ab]*$',mot))

def presenceUnCaractectereDroite(mot):
    return bool(re.match(r'^[^b]*b[b]*$',mot))

def langageVoulu(mot):
    if appartenirLangage(mot)== True:
        if mot.find("b") == -1:
            return True;
        elif presenceUnCaractectereDroite(mot) ==True:
            return True;
    else:
        return False;

mot = input("Entrez un mot pour verifier son appartenance : ");

if len(mot) == 0:
    print("le mot vide appartient");
elif langageVoulu(mot) == True:
    print(mot + " appartient au langage aibj");
else:
    print(mot +" n'appartient pas au langage aibj")
    