import numpy as np
import pandas as pd
import gc

guardian = pd.read_csv('C:/Users/Thunder/Desktop/essay/guardian_articles.csv', encoding='ISO-8859-1')
bbc = pd.read_csv('C:/Users/Thunder/Desktop/essay/bbc.csv', encoding='ISO-8859-1')

### to find the content about russia and ukraine ###
def find_ur(element, sentence):
    result = False
    sentence = sentence.upper()
    for i in element:
        i = i.upper()
        if i in sentence:
            result = True
        else:
            continue
    return result

### clean the data ###
guardian_new = guardian.dropna()
bbc_new = bbc.dropna()

### set the politics part as our analysis target ###
guardian_politi = guardina_new[guardian_new['sectionName'] == 'Politics']


### find the russia and ukraine news after the war ###
element = {'Russ','ukra'}
number_g = np.array([])
number_b = np.array([])
for j in guardian_politi.index:
    if find_ur(element,guardian_new.iloc[:,4][j]):
        number_g = np.append(number_g,j)
for i in guardian_politi.index:
    if find_ur(element,bbc_new.iloc[:,4][i]):
        number_b = np.append(number_b,i)

### output the result ###


