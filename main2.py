import pandas as pd
from pprint import pprint
from func import *
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_pickle('pickled/df_all_stemmed')#[['AB', 'AB_m', 'TI', 'TI_m']]
df['kw'] = df['ID'].fillna('').map(lambda x: split_m(x.lower(), '; ')) + df['DE'].fillna('').map(lambda x: split_m(x.lower(), '; '))
df['kw'] = df['kw'].map(lambda x: list(set(x)))
pd.DataFrame(df['kw'].to_list()).stack().reset_index(level=1, drop=True).value_counts().to_frame().to_csv('freqs.csv')
pass
