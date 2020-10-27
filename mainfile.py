# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:59:36 2020

@author: Niketan
"""
import time
import pandas as pd
import numpy as np
import spacy
import string
from collections import Counter
import matplotlib.pyplot as plt
from statement import returnstat


def emotionproc(text):
    
    database=pd.read_csv('data.csv')
    database=database[['English (en)', 'Positive', 'Negative', 'Anger','Anticipation',\
                       'Disgust', 'Fear', 'Joy', 'Sadness', 'Surprise','Trust']]
    nlp=spacy.load('en_core_web_sm')
    stopwords=nlp.Defaults.stop_words
    
    
    txt=text
    txt=txt.split()
    for i in txt:
        if i in stopwords:
            txt.remove(i)
        if i in string.punctuation:
            txt.remove(i)
    txt=' '.join(txt)
    doc=nlp(txt)
    
    emotions=[]
    for token in doc:
        a=0
        #print(token.text,token.lemma_)            
        a=database.loc[database['English (en)']==token.lemma_]
        #print(database.loc[database['English (en)']==token.lemma_])
        a=a.values
        a=a[:,1:]
        a=sum(a.tolist(),[])
        columns=['Positive', 'Negative', 'Anger', 'Anticipation',
               'Disgust', 'Fear', 'Joy', 'Sadness', 'Surprise', 'Trust']
        dictionary={}
        for A,B in zip(columns,a):
            dictionary[A]=B
        #print(dictionary)  
        for key, value in dictionary.items(): 
             if value == 1: 
                 emotions.append(key)     
        #print(emotions)
   # print(Counter(emotions))
    
    w=Counter(emotions)
    
    plt.bar(w.keys(),w.values())
    plt.xticks(rotation=30)
    plt.ylabel('Count of your feelings')
    plt.tight_layout()
    t=w.keys()
    plt.savefig('E:\emotion\static\emot.png')
    
    positive_emo=['Positive', 'Anticipation', 'Joy', 'Surprise','Trust']
    sum_pos=0
    for i in list(t):
        if i in positive_emo:
     #       print(i,w[i])
            sum_pos=sum_pos+w[i]
    #print(sum_pos)
    
    negative_emo=['Negative', 'Anger','Disgust', 'Fear', 'Sadness']
    sum_neg=0
    for i in list(t):
        if i in negative_emo:
     #       print(i,w[i])
            sum_neg=sum_neg+w[i]
    #print(sum_neg)
    
    stri=returnstat(sum_pos,sum_neg)
    
    # if sum_neg > sum_pos:
    #    #print(" Don't be so negative . Try to be positive")
    #    stri=" Don't be so negative . Try to be positive"
    # elif sum_neg==0 and sum_pos==0:
    #    stri='Neutral Statement'
    #     #print('Neutral Statement')
    # else:
    #     stri='Very nice. positivity all the way'
    #     #print('Very nice. positivity all the way')
    
    return stri,w
