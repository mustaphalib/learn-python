# print("hello world")

# a = 10
# b = 16

# if a>b :
#     print("true")
# else :
#     print("false")

# liste = [1,2,3,4,5,6,7,8,9]

# for i in liste:
#     print(i)

# rs= input("saisir un nombre reel : ")
# print("le nombre saisi est :",rs)

# k = 10 
# while k< 14 :
#     print("le nombre",k)
#     k+=1
# print("fin")
# # somme de deux nombre 

# nb1 = int(input("number 1 : "))  # a definir en int sinon va pas marcher sans déclaration 
# nb2 = int(input("number 2 : "))

# somme = nb1 + nb2 

# print("la somme de deux nombres est :", somme)
# print(("pa"+"la")*2) # affichage palapala

# print("hello word")  ; print("bonjour")

# age= 20
# Nom= "Mustapha"

# #print("mon nom est",Nom,"et mon age est", age)

# print(f"{Nom} à {age} ans ")  # ecriture formatée f-strings


# # faire la division ///

# div= nb1/nb2
# print(f"la division est {div : .4f}")


# print(f"le resultat de 5*5 est {5*5}")

# # min max et min 

# lista = [ 1,2,3,4,5,6,7,8,9]
# minimum = min(lista)
# maximum =max(lista)
# somme= sum(lista)
# print(f"le minimum est {minimum} et le maximum est {maximum} et la somme de la liste est {somme}")

# ## *****************  liste & indice (page 28)  ****************************** 

animaux = ["girafe", "souris", "lion", "vache", "chat", "chien"]
# indice :    0         1        2        3         4      5

# for hay in animaux :  # no animaux[hay] ----> Faux 
#     print(hay)  
# print("fin")
# print(len(animaux))

def afficher_animaux():
    print(animaux)

longueur = len(animaux)
# print(longueur)
animal = "souris"
# print("Emplacement du {}:".format(animal), animaux.index(animal))

# on veut afficher ["souris", "lion", "vache"]
# print(animaux[1:4])

# pour vider la liste
# animaux.clear()

# animaux2 = animaux.copy()
# animaux2.append("elephant")
# print(animaux2)
# liste_numerique = [1,4,2,5,3,6,2,5,2,4,1,4,1,6,7,1,4,1,3,1,3,1,5,4,2,5,1,4,3,1,1]
# print(liste_numerique.count(2))
# animaux2 = ["mustapha", "hassan", "rachid"]
# animaux.extend(animaux2)
# print(len(animaux))

# l'indice
# print(animaux.index("souris"))

# supprimer la derniere valeur dans la liste
# afficher_animaux()
# animaux.pop()
# afficher_animaux()

# afficher_animaux()
# animaux.remove("vache")
# afficher_animaux()


# afficher_animaux()
# animaux.insert(2, "elephant")
# afficher_animaux()

# afficher_animaux()
# animaux.reverse()
# afficher_animaux()

# afficher_animaux()
# animaux.sort(reverse=True)
# afficher_animaux()


# print("animaux avant append", animaux)
# animaux.append("oiseau")
# print("animaux après append", animaux)

# for i in range(len(animaux)):
#     print(i)

liste_numerique = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# for i in range(1, len(liste_numerique), 5):
#     print(i)

# liste_numerique_x_2 = []

# for i in liste_numerique:
#     if i%5 != 0:
#         liste_numerique_x_2.append(i*2)

# print(liste_numerique_x_2)


liste_numerique_x_2 = [i*2 for i in liste_numerique if i%5 != 0]
print(liste_numerique_x_2)



# ## *******************  rajouter a la liste  *********************************

# animaux.append("chien") 

# print(animaux)

# ## ****************** Tranche d'une liste ****************************

# print(animaux[0 : 2]) # dans ce cas l'indice 2 est exclu ( va afficher que 'girafe' & 'tigre')


# ##********************** Fonction len() = longueur de la liste  ******************************

# print(len(animaux))

# ## ********* fonction range() et list() pour generer des nombres entiers ************

# vay= list(range(7)) 

# print(vay)  # ----> [0, 1, 2, 3, 4, 5, 6]

# vay2=list(range(15,20))

# print(vay2)  # ----> [15, 16, 17, 18, 19]

# vay3 = list(range(15,20,2)) 

# print(vay3)  # ----> [15, 17, 19]