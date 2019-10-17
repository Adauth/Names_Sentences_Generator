import csv
import string
import math
import random

nomVilles = []
ngrams = {}
ordre = 3
debut = []
txt = " "


with open('C:\Code\Python\communes-01012019.csv', encoding='UTF-8') as csvfile:
    reader = csv.DictReader(csvfile,delimiter =',')
    for row in reader:
        listeNom = row['libelle']
        nomVilles.append(listeNom)
        txt += listeNom
        txt += " "


for i in range(0,len(txt) - (ordre - 1)):
        gram = txt[i:i+ordre]

        if not ngrams.get(gram):
                ngrams[gram] = []
        
        if not i==len(txt) - ordre:
                ngrams[gram].append(txt[i+ordre])

for villes in nomVilles:
        debut.append(villes[0:ordre])

currentGram = random.choice(debut)
result = currentGram

for j in range(0, 10):
        possibilities = ngrams.get(currentGram)
        if not possibilities:
                break
        nextStr = random.choice(possibilities)
        result += nextStr
        taille = len(result)
        currrentGram = result[(taille - ordre):taille]
        
        if result[taille - 1] == ' ':
                break

print(result)
