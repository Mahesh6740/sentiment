# -*- coding: utf-8 -*-
"""Sentiment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i7o5neU0uNT2UlMJ6LGOpVcYLmxai665
"""

import pandas as pd

data= pd.read_csv('/content/Reviews.csv')
data

data.head()

data.tail()

data.info()

data.describe()

data.isnull().sum()

data.duplicated()

value_counts= data['Liked'].value_counts()
print(value_counts)

pip install matplotlib

import matplotlib.pyplot as plt
import seaborn as sns

value_counts.plot(kind='bar',color=['blue','green'])
plt.title("Sentiment value counts")
plt.xlabel('Liked')
plt.ylabel('Count')
plt.xticks(ticks=[0,1] , labels=['Postive','Negative'],rotation=0)
plt.show()

from wordcloud import WordCloud

combined_text = " ".join(data['Review'])
wordcloud = WordCloud(width = 800 , height = 400 ,background_color = 'white').generate(combined_text)
plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.title('Word Cloud of Reviews')
plt.show()

from collections import Counter

target_words = ['food','place','restaurant']
all_words = " ".join(data['Review']).lower().split()
word_counts = Counter(all_words)
target_word_counts = {word:word_counts[word] for word in target_words}
plt.figure(figsize=(8,6))
plt.bar(target_word_counts.keys(),target_word_counts.values() , color = ['blue','green','orange'])
plt.xlabel('words')
plt.ylabel('Frequenecy')
plt.title('Frequency of specific words in Reviews')
plt.show()

lowercased_text = data['Review'].str.lower()

print(lowercased_text)