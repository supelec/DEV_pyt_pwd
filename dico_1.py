#!/usr/bin/python3
# coding: utf-8

import hashlib
import time

def main(argv):
    with open('shadow', 'r') as f:
        for line in f:
            if (len(line.split(':')) == 9):
                print("Parse du compte dans shadow OK")
            else:
                print("Mauvais parse de la ligne; ligne non traitée")

def splitfile(fichier):
    with open(fichier, 'r') as fo: #/Ouvrir fichier des coomptes et MDP
        tabRecup = []
        for ligne in fichier:
            valLigne = ligne.split(':')

def recu

if __name__ == "__main__":
    main("")

'''    with open('shadow', 'r') as f: #/Ouvrir fichier des coomptes et MDP
        tabRecup = []
        for line in f:
            valrecup = line.split(':', 2)
            user = valrecup[0]
            tab = valrecup[1].split('$')
            #print(tab)
            if (len(tab) > 2):
                hpass2 = tab[2]
                hpass1 = tab[1]
                tabRecup.append([user, hpass1, hpass2])

    #print(tabRecup)

    with open('dico_mini_fr', 'r') as g: #/Ouvrir fichier des coomptes et MDP
        for line1 in g:
            timestart = time.time()
            outhash = hashlib.md5(line1.strip().encode())
            valgen = outhash.hexdigest()
            x = 0
            for z in tabRecup:
                #print(z[2] + " " + valgen)
                if (valgen == z[2]):
                    timestop = time.time() - timestart
                    print('Find ' + z[0] +' in : ' + str(timestop))
                x += 1
                #if (tabRecup[x,3] == outhash):
                #    print("Merci")
'''

    #
