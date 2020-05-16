import pandas as pd
df = pd.read_csv('Clinical_Imaging Techniques.csv')
df = df.merge(pd.read_csv('Highly-Cited_clinical_PMID.csv')[['PMID', 'MNCS']], how='left', left_on='PM', right_on='PMID').drop(columns='PMID')
df['methods'] = df['methods'].map(eval).map(lambda x: x if x else ['nomethod'])
df = df.join(pd.DataFrame(df['methods'].tolist()).stack().reset_index(level=1, drop=True).rename('methods2'))
df.to_csv('ct.csv')