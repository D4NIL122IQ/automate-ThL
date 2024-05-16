#mix en utilisant re pour anbj tel que j>n>0

import re;

def appartenirAlphabet(mot):
    for cara in mot:
        if not cara =="a" and not cara == "b" :
            return False;
    return True;

def NbrSupAqueB(mot):
    if len(re.findall(r'b', mot)) > len(re.findall(r'a', mot)):
        return True

def ordreSansMelange(mot):
    for cara in mot[mot.find("b") : len(mot)]:
        if cara == "a" :
            return False;
    return True;
   
def appartenirLangage(mot):
    if appartenirAlphabet(mot) == True:
        if ordreSansMelange(mot) == True:
            if NbrSupAqueB(mot) == True:
                return True;

mot = input("entrez une chaine : ");

if len(mot) == 0:
    print("le mot vide n'appartient pas a ce langage");
elif appartenirLangage(mot) == True: 
    print("le mot appartient au langage");
else:
    print("le mot n'apprtient pas au langage");
