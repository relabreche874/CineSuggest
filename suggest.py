import nltk

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
import pandas as pd
import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv('imdb.csv')

df['Overview'] = df['Overview'].str.lower()
df['Overview'] = df['Overview'].apply(lambda i: re.sub('[^a-zA-Z]', ' ', i))
df['Overview'] = df['Overview'].apply(lambda i: re.sub('\s+', ' ', i))
df['Overview'] = df['Overview'].apply(lambda i: nltk.word_tokenize(i))

word_rem = nltk.corpus.stopwords.words('english')
temp_list = []
for sent in df['Overview']:
    temp = []
    for word in sent:
        if word not in word_rem and len(word) >= 3:
            temp.append(word)
    temp_list.append(temp)

df['Overview'] = temp_list

df['Genre'] = df['Genre'].apply(lambda i: i.split(','))
df['Actors'] = df['Star1'] + ',' + df['Star2'] + ',' + df['Star3'] + ',' + df['Star4']
df['Actors'] = df['Actors'].apply(lambda i: i.split(','))
df['Director'] = df['Director'].apply(lambda i: i.split(','))


def lowlow(lst):
    temp_lst = []
    for i in lst:
        temp_lst.append(i.lower().replace(' ', ''))
    return temp_lst


df['Genre'] = [lowlow(x) for x in df['Genre']]
df['Actors'] = [lowlow(x) for x in df['Actors']]
df['Director'] = [lowlow(x) for x in df['Director']]

col_list = ['Overview', 'Genre', 'Director', 'Actors']
new_list = []
for i in range(len(df)):
    words = ''
    for col in col_list:
        words += ' '.join(df[col][i]) + ' '
    new_list.append(words)

df['Overview'] = new_list
df = df[['Series_Title', 'Overview']]

tfi_vect = TfidfVectorizer()

feats = tfi_vect.fit_transform(df['Overview'])

cos_sim = cosine_similarity(feats, feats)

index = pd.Series(df['Series_Title'])


def suggest(title):
    movies = []
    idx = index[index == title].index[0]
    # print(idx)
    sims = pd.Series(cos_sim[idx]).sort_values(ascending=False)
    top3 = list(sims.iloc[1:4].index)
    # print(top3)
    print("\nRecommended movies:\n")
    for i in top3:
        movie_title = df.iloc[i]['Series_Title']
        movies.append(movie_title)
        print(f'\t- {movie_title}')



