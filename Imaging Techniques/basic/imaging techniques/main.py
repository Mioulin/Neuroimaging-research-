from func import *
import yaml
# load_and_pickle()
# text_process_and_pickle(pd.read_pickle('pickled/df_all'))
# df = pd.read_pickle('pickled/df_all_stemmed')#[['AB', 'AB_m', 'TI', 'TI_m']]
df['words'] = ' ' + df['AB_m'] + ' ' + df['TI_m'] + ' '
dict_with_words = yaml.full_load(open("methods.yaml", encoding='utf-8'))
dict_with_words = {k: [' ' + ' '.join([text_process(xx) for xx in x]) + ' ' for x in v] for k, v in dict_with_words.items()}
df['methods'] = df['words'].map(lambda x: [k for k, v in dict_with_words.items() if any([tag in x for tag in v])])
df[['AB', 'TI', 'year', 'PM', 'methods']].to_csv('output.csv')
pass


