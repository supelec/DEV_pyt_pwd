#/usr/bin/python
# encode: UTF-8
# Code By supelec
# Thanks to sleepy & max
# To project crypto

import hashlib

#/ def main():


def hashed_password(passfind):
    return hashlib.md5(passfind.encode());
    # print hash_object

def comparestring(hashed_password, pwdfile):
    compar = hashed_password.hexdigest()
    pw2hash = pwdfile.hexdigest()
    return compar == pw2hash

passwordin = 'brazil';
passwordout = 'brazil';
hashed_passin = hashed_password(passwordin); #/ Génération du hashpass
hashed_passout =  hashed_password(passwordout);

print(hashed_passin.hexdigest()); #/ Un petit controle pour la valeur

if comparestring(hashed_passin, hashed_passout): #/ Lancement du test comparaison val
    print('Trouvé :-) ' + 'Mdp clair : ' + passwordout + ' Valeur Hash : ' + hashed_passin.hexdigest())
else:
    print('Pas Trouvé :-( ' + hashed_passout.hexdigest() + ' / Mdp généré : ' + passwordout + ' Valeur Hash : ' + hashed_passin.hexdigest())

tabRecup = [] # Création tableau pour recup info du fichier shadow

with open('shadow', 'r') as f: #/Ouvrir fichier des coomptes et MDP
    for line in f:
        valrecup = line.split(':', 2)
        user = valrecup[0]
        tab = valrecup[1].split('$')
        if (len(tab) > 2):
            hpass2 = tab[2]
            hpass1 = tab[1]
            tabRecup.append([user, hpass1, hpass2])
print(tabRecup)
        #print(user, hpass1, hpass2)
        #print(valrecup[1])
        #decoup = [str(e) for e in valrecup]
        #user, hashme = decoup
        #print(user, hashme)
        #print(hashme)
        #print(other)
    #pass














#/
