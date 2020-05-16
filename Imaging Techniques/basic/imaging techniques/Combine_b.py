import numpy
import pandas as pd
df_all =  pd.DataFrame()
file_names = ['b01txt.txt', 'b02.txt', 'b03.txt']
for file_name in file_names:
    with open(file_name) as f:
        text = f.read()
        text = text[text[:100].index('\nPT') + 1:]
        articles = text.split('\n\n')[:-1]
        article_dicts = []
        for article in articles:
            article_dict = {}
            for line in article.split('\n'):
                article_dict[line[:2]] = line[3:]
            article_dicts.append(article_dict)
        df = pd.DataFrame(article_dicts)
        df_all = df_all.append(df, ignore_index=True, sort=False)
        df_all.to_csv('basic.csv')
pass
