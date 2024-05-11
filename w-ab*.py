# w € {a,b}* / |w|a=2k+1
import re;

def appartenirAlphabet(mot : str) -> bool:
    return bool(re.match(r'^[ab]*$',mot));

def nbrDeA(mot: str) -> int:
    compteA =0;
    for caractere in mot:
        if caractere == "a":
            compteA += 1;

    return compteA;

def appartenirLangage(mot)->bool:
    if appartenirAlphabet(mot) == True:
        if nbrDeA(mot) % 3 == 0:
            return True;
    else: 
        return False;

chaine = input("entrez un mot pour verifier son appartenance : ");

if len(chaine)==0:
    print("le mot vide appartient");
elif appartenirLangage(chaine )== True:
    print("le mot appartient au lengage");
else:
    print("le mot n'appatient pas au langage");