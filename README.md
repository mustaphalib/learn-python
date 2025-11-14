# Introduction
## Les commandes

```bash
git add .
git commit -m "message"
git push -u origin main
```

# Exercice 1:
### Ecrire un algorithme Python permettant d'échanger le premier élément avec le dernier élément d'une liste donnée.
### Exemple:
```python
L = ["Python", "Java", "C ++", "Javascript"]
```

### l'algorithme renvoie la liste:
```python
["Javascript", "Java", "C ++", "Python"]
```

# Solutions
```python
Box = L[0]
L[0] = L[-1]
L[-1] = Box
print(L)
```

# Excercice 2:
### Etant donné une liste d'entiers L, écrire un programme en Python qui renvoie la somme des éléments de la liste L.
```python
M = [6 ,1 ,4 , 7, 8, 4, 1, 3, 5]
```

```python
# S = 0
# for i in M : 
#     # la variable i prend directement les valeurs de M (1, 2, 7) et non leurs indices.
#     S = i + S

# print(S)
```

```python
print(sum(M))
minimum = M[0]
maximum = M[0]

for i in M :
    if i < minimum :
        minimum = i

for i in M :
    if i > maximum :
        maximum = i

print(min(M))
print(max(M))

print("""hello 
salut
ca va
""")
```