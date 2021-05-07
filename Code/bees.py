"""
# Independent Project: Automatic Bee Identification
To predict the species of a bee, given its description in text format, using Information Retrieval, Natural Language Processing and Machine Learning techniques.
"""

import numpy as np
import pandas as pd

f = open('dataset bees.txt', 'r', encoding='utf8')

x = f.read()

x = x[x.index('}}')+2:]
samples = {}
s = x.split('\n')
s = [i for i in s if i != '']

samples = {}
i = 0
while i < len(s)-1:
  samples[s[i]] = s[i+1]
  i+=2

import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import string
from nltk.stem import WordNetLemmatizer 
stop_words = set(stopwords.words('english'))

punc = string.punctuation
lem = WordNetLemmatizer()
for i in samples:
  samples[i] = samples[i].lower()
  samples[i] = samples[i].strip()
  for ele in samples[i]:  
    if ele in punc:  
        samples[i] = samples[i].replace(ele, "")  
  toks = word_tokenize(samples[i])
  fil = [w for w in toks if not w in stop_words] 
  fil = [lem.lemmatize(w) for w in fil ]
  samples[i] = fil

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

tfIdfVectorizer=TfidfVectorizer(use_idf=True)
tf = tfIdfVectorizer.fit_transform(samples)

df = pd.DataFrame(tf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
df = df.sort_values('TF-IDF', ascending=False)

def computeTFReview(review):
    reviewTFDict = {}
    for word in review:
        if word in reviewTFDict:
            reviewTFDict[word] += 1
        else:
            reviewTFDict[word] = 1
    for word in reviewTFDict:
        reviewTFDict[word] = reviewTFDict[word] / len(review)
    return reviewTFDict

tfDict = {}
reviewNo = 1
for review in samples:
    tfDict['review: ' + str(reviewNo)] = computeTFReview(samples[review])
    reviewNo += 1

vocab = []
for i in tfDict:
  vocab+=list(tfDict[i].keys())
vocab = list(set(vocab))

def computeCountDict(tfDict):
    countDict = {}
    for review in tfDict:
        for word in tfDict[review]:
            if word in countDict:
                countDict[word] += 1
            else:
                countDict[word] = 1
    return countDict

countDict = computeCountDict(tfDict)

def computeIDF(countDict, n):
    import math
    idfDict = {}
    for word in countDict:
        idfDict[word] = math.log(n / countDict[word])
    return idfDict

idfDict = computeIDF(countDict, len(samples[review]))

def computeTFIDF(review, idfDict):
    tfidfDict = {}
    for word in review:
        tfidfDict[word] = review[word] * idfDict[word]
    return tfidfDict

tfidfDict = {}
review_no = 0
for review in tfDict:
    tfidfDict['review: ' + str(review_no)] = computeTFIDF(tfDict[review], idfDict)
    review_no += 1

tfidfDict['review: 1']
for i in tfidfDict:
  x = (sorted(tfidfDict[i].items(), key=lambda item: item[1]))

def prepro(s):
  punc = string.punctuation
  lem = WordNetLemmatizer()
  s = s.lower()
  s = s.strip()
  for ele in s:  
    if ele in punc:  
        s = s.replace(ele, "")  
    toks = word_tokenize(s)
    fil = [w for w in toks if not w in stop_words] 
    fil = [lem.lemmatize(w) for w in fil ]
  ans = []
  for i in fil:
    if(i in vocab):
      ans.append(i)
  return ans

"""### 1. Raw TF-IDF"""

def rank_raw(q):
  q1toks = prepro(q)
  score = {}
  for i in tfidfDict.keys():
    score[i] = 0
  for i in q1toks:
    for j in tfidfDict:
      if( i in tfidfDict[j]):
        score[j]+= tfidfDict[j][i]
  score = dict(sorted(score.items(), key=lambda item: item[1]))
  ans = list(score.keys())[-15:]
  ans = [int(x[-2:]) for x in ans]
  sk = list(samples.keys())
  topten = [sk[i] for i in ans]
  return topten

"""### 2. Boolean TF-IDF"""

def rank_bool(q):
  q1toks = prepro(q)
  score = {}
  for i in tfidfDict.keys():
    score[i] = 0
  qlis = {}
  for i in q1toks:
    if i in qlis:
      qlis[i]+=1
    else:
      qlis[i] = 1
  for i in range(len(q1toks)):
    for j in tfidfDict:
      if( q1toks[i] in tfidfDict[j]):
        score[j]+= tfidfDict[j][q1toks[i]]*qlis[q1toks[i]]
  score = dict(sorted(score.items(), key=lambda item: item[1]))
  ans = list(score.keys())[-15:]
  ans = [int(x[-2:]) for x in ans]
  sk = list(samples.keys())
  topten = [sk[i] for i in ans]
  return topten

"""### 3. Log-Normalised TF-IDF"""

import math
def rank_lognorm(q):
  q1toks = prepro(q)
  score = {}
  for i in tfidfDict.keys():
    score[i] = 0
  qlis = {}
  for i in q1toks:
    if i in qlis:
      qlis[i]+=1
    else:
      qlis[i] = 1
  for i in qlis:
    qlis[i]*= abs(idfDict[i])
    qlis[i] = math.log(1+qlis[i])
  for i in range(len(q1toks)):
    for j in tfidfDict:
      if( q1toks[i] in tfidfDict[j]):
        score[j]+= math.log(1+tfidfDict[j][q1toks[i]])*qlis[q1toks[i]]
  score = dict(sorted(score.items(), key=lambda item: item[1]))
  ans = list(score.keys())[-15:]
  ans = [int(x[-2:]) for x in ans]
  sk = list(samples.keys())
  topten = [sk[i] for i in ans]
  return topten

"""### Rank after combining all the TF-IDF Algorithms"""

def merge(a,b,c):
  saare = {}
  tot = [a, b, c]
  for x in tot:
    for i in range(len(x)):
      if x[i] in saare:
        saare[x[i]]+= i
      else:
        saare[x[i]] = i
  saare = sorted(saare.items(), key= lambda item: item[1])
  toans = saare[-15:]
  ans = []
  for i in range(len(toans)-1,-1, -1):
    ans.append(toans[i][0])
  return ans

def find_ranks(q):
  a = rank_raw(q)
  b = rank_bool(q)
  c = rank_lognorm(q)
  x = merge(a,b,c)
  return x