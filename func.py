import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem.snowball import EnglishStemmer
import string
i = 0
punctuation = ''.join([s for s in string.punctuation if s != '-']) + "«»‹›—"


def split_m(s, subs):
    return [x for x in s.split(subs) if x]


def load_and_pickle():
    file_names = [f'{n + 1}-{n + 500}.txt' for n in range(0, 51000, 500)] + ['51001-51223.txt']
    dfs = []
    for file_name in file_names:
        with open(f'texts/{file_name}', encoding='utf-8') as f:
            text = f.read()
            text = text[text.index('\nPT') + 1:]
            text = text.replace('\n   ', ' ')
            articles = text.split('\n\n')[:-1]
            article_dicts = [{line[:2]: line[3:] for line in article.split('\n')} for article in articles]
            df = pd.DataFrame(article_dicts)
            df['year'] = df.apply(lambda x: int((x['PY'] if pd.notnull(x['PY']) else x['EA'])[-4:]), axis=1)
            dfs.append(df)
            print(file_name, df.shape[0])
    df_all = pd.concat(dfs, ignore_index=True, sort=True)
    df_all.to_pickle('pickled/df_all')


def text_process_and_pickle(df):
    df['TI_m'] = df['TI'].map(text_process)
    df['AB_m'] = df['AB'].map(text_process)
    df.to_pickle('pickled/df_all_stemmed')


def text_process(mess):
    global i
    print(i)
    i += 1
    # Выкидываем знаки препинания, переводим в lowercase и выбрасываем stopwords
    if pd.isnull(mess):
        mess = ''
    nopunc = ''.join([char.replace('-', ' ') for char in mess if char not in punctuation])
    nopunc = nopunc.lower()
    # stemmer = EnglishStemmer()
    return ' '.join(word for word in nopunc.split() if word not in stopwords.words('english'))
