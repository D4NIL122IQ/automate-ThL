# (ab)icj 

def appartenirAlphabet(mot):
    for cara in mot:
        if not cara == "a" and not cara =="b" and not cara == "c":
            return False ;
    return True;

def ordreAB(mot):
    lastB = mot.rfind("b");
    for i in range(0, lastB):
        if i == 0:
            if not mot[i] == "a" :
                return False;
        elif not (mot[i] == "b" and mot[i-1] == "a" or mot[i] == "a" and mot[i-1] == "b"):
            return False;
    return True

def ordreC(mot):
    firstC = mot.find("c");
    for cara in mot[firstC : len(mot)]:
        if not cara == "c":
            return False;
    return True;

def appartenirLangage(mot):
    if appartenirAlphabet(mot) == True:
        if ordreAB(mot) == True and ordreC(mot) == True:
            return True;


mot = input("entrez une chaine : ");

if len(mot) == 0:
    print("le mot vide appartient a ce langage");
elif appartenirLangage(mot) == True: 
    print("le mot appartient au langage");
else:
    print("le mot n'apprtient pas au langage");