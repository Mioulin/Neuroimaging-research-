from cleaner import *
import pandas as pd


df = pd.read_csv('basic.csv')
df = df.merge(pd.read_csv('BasicALL.csv')[['PMID', 'MNCS']], how='left', left_on='PM', right_on='PMID').drop(columns='PMID')
df = get_kw(df)
df = remove(df)
df = replace(df)
df.to_csv('test.csv')
pass

