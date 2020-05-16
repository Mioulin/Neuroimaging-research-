from cleaner import *
import pandas as pd


df = pd.read_csv('clinical.csv')
df = df.merge(pd.read_csv('Highly-Cited_clinical_PMID.csv')[['PMID', 'MNCS']], how='left', left_on='PM', right_on='PMID').drop(columns='PMID')
df = get_kw(df)
df = remove(df)
df = replace(df)
df.to_csv('test_cl.csv')
pass

