import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import nltk
from nltk.corpus import stopwords
from sklearn.metrics import accuracy_score


data = pd.read_csv("./spam.csv",encoding='latin-1')
data.drop(['Unnamed: 2','Unnamed: 3','Unnamed: 4'],axis=1,inplace=True)
data.loc[data['v1']=='spam','v1']=1
data.loc[data['v1']=='ham','v1']=0

spam_words = ' '.join(list(data[data['v1']==1]['v2']))
#x = WordCloud().generate(spam_words)
#plt.figure(figsize=(10,8),facecolor='k')
#plt.axis('off')
#plt.imshow(x)


data['legnth'] = data['v2'].apply(len)
#data.loc[data['v1']==1,'legnth'].hist()
#data.loc[data['v1']==0,'legnth'].hist()

messages = data['v2'].copy()
def process(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word.lower() for word in text.split() if word.lower() not in stopwords.words('english')]
    return ''.join(text)
messages.apply(process)

vec = TfidfVectorizer('english')
messages = vec.fit_transform(messages)
def vectorize_train(message):
    text = vec.transform(message)
    return text

X,Y,X_label,Y_label= train_test_split(messages,data['v1'])
X_label = X_label.astype('int')
Y_label = Y_label.astype('int')

mnb = MultinomialNB(alpha=0.2)
mnb.fit(X,X_label)
#pred = pd.Series(mnb.predict(Y))
#print(accuracy_score(pred,Y_label))
