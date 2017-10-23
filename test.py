#!/usr/bin/python
# coding: utf-8
def fct_test (): #/ Definition d'une fonction
    print ("Hello world !")

def env_py(): #/ Recup version Pyton
    #/ Si pas de retour, pas d'env_phy
    #/ Sinon recup verion.
    #/ Note de version : Compatible  2.7.12

def recup_file(): #/Recuperation du contenu du fichier
    #/


def


# main() utiliser de maniere conventionnel

# variale # si mis au début : c'est une variable globale
# si pas mis dans un contexte, c'est une var global

def appelvariable():
    vartoto = "aaaaa"
    print(vartoto)

appelvariable()

# range : que des nombres
# rzange(-2,5)
for x in range(10):
    # instruction a suivre
    # if (x%2 == 0):
    if (x%2 == 0):
        print x, "est pair"
    else:
        print x, "est impair"

with open("./bidon", "rw") as result_bidon:
    tmp = result_bidon.read()
    print(tmp)
    pass
