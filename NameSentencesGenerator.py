'''
NAMES AND/OR SENTENCES GENERATOR
IN FONCTION OF THE args AND THE str YOU PUT,
TOU CAN GENERATE A TEXT OR NAMES IN FUNCTION OF A ORIGINAL ONE

Author:EL HAJJAJI Adil
Date:10/17/2019
Version:1.0.1

code inspired from The Coding Train channel : https://youtu.be/eGFJ8vugIWA?list=PLRqwX-V7Uu6ZiZxtDDRCi6uhfTH4FilpH

'''

import random
import csv
import string
import math

txt = ""
nomsVilles = []#(optionnal)For my use, I needed a list of towns names to get the first n-grams of each 
debut = []#(optionnal)Like the previous list, I need a list to stock the first n-grams of each town in the csv file
ordre = 3 #You can change the order here.For my use, 3 is the optimal order
ngrams = {}#The dictionnary where i will stock the n-grams and their "what letter after" possibilities, according to the Markov Chain


'''
IN THIS EXAMPLE I USE A LIST FROM A CSV FILE,BUT YOU CAN REMOVE THE with open BLOCK
AND PUT YOUR OWN TXT IN A str VARIABLE
'''
with open('D:\EPSI\Python\TP_1\communes-01012019.csv', encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile,delimiter=',')
        listeA = ""
        for colonnes in reader:
                
                listeNom = colonnes["ncc"]
                nomsVilles.append(listeNom)
                txt = txt + listeNom
                txt = txt + " "
                

for i in range(0,len(txt) - (ordre - 1)):#get the n-grams in function of the order
    gram = txt[i:i+ordre]
    
    if not ngrams.get(gram):
        
        ngrams[gram] = []
        
   
    if not i==len(txt) - ordre :#To avoid the "Index Out of range" error
        ngrams[gram].append(txt[i + ordre])#for each n-grams, we allocate the letter or letters that follow   

for ville in nomsVilles:
    debut.append(ville[0:ordre])#get all the first n-garms of each town in the list

currentGram = random.choice(debut)
#currentGram = txt[0:ordre] This line is useful to generate a sentence: It takes the first n-gram of the original sentence

result = currentGram #For my use, randomly get the beginning of the generated word.
                    #Else you can put the word or syllabe you want to begin with 


for i in range(0,20):#Define the lenght of the generated word.For my use, 20 max is optimal.You can set more if you want to generate a sentence
    possibilities = ngrams.get(currentGram)#Get the possible letters that can follow the first n-gram
    if not possibilities:
        break
    nextStr = random.choice(possibilities)#randomly get a letter from the possibilities
    result = result + nextStr#concatenate
    taille = len(result)#get the lenght of the result
    currentGram = result[(taille - ordre):taille]#get the next n-gram of the result, then get the possibilities of letters 
                                                    #that follow this n-grams and et cetera...
    if result[taille - 1] == ' ':#(Optionnal)this block is only necessary if you want to generate a word.remove it to genearte a sentence
        break
print(result)

