# aibj / i,j>=0

mot = input("entrez une chaine : ");

def appartenirAlphabet(mot):
    for cara in mot:
        if not cara == "a" and not cara =="b":
            return False ;
    return True;

def pasDeMelange(mot ):
    debutB = mot.find("b");
    finB = mot.rfind("b")
    sousMot =mot[debutB:finB]
    for cara in sousMot:
        if not cara =="b":
            return False;
    return True;

def appartenirLangage(mot):
    if appartenirAlphabet(mot) == True:
        if len(mot) - 1 == mot.rfind("b"):
            if pasDeMelange(mot) == True:
                return True;




if len(mot) == 0:
    print("le mot vide appartient a ce langage");
elif appartenirLangage(mot) == True: 
    print("le mot appartient au langage");
else:
    print("le mot n'apprtient pas au langage");