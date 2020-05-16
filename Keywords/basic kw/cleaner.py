import pandas as pd
from collections import Counter
from pprint import pprint


def get_kw(df):
    def clean(x):
        if pd.isnull(x):
            return []
        return x.strip('; ').lower().split('; ')
    df['KW'] = (df['ID'].map(clean) + df['DE'].map(clean))
    return df


def count(df):
    c = Counter((df['ID'].fillna('').str.lower().str.split('; ') + df['DE'].fillna('').str.lower().str.split('; ')).sum())
    pprint(c.most_common())


def remove(df):
    to_remove = ['fmri']
    df['KW'] = df['KW'].map(lambda x: [s for s in x if s.lower() not in to_remove])
    return df


def replace(df):
    def merge_dicts(dict_args):
        result = {}
        for dictionary in dict_args:
            result.update(dictionary)
        return result
    # Заменяются все, кроме последнего на последний в списке
    to_replace = [['major depressive disorder', 'dementia', 'depression', ],
                  ['low-grade gliomas', 'brain-tumor', 'tumor',],
                  ['alzheimers-disease', 'mild cognitive impairment', 'neuroimaging initiative adni',
                  'mild alzheimers-disease', 'alzheimer-disease', 'dementia'],
                  ['brain-development', 'pediatric brain-development', 'developmental dyslexia',
                   'human cortical development', 'development'],
                  ['late-life depression', 'treatment-resistant depression', 'major depressive disorder', 'depression'],
                  ['multiple-sclerosis', 'multiple-sclerosis brain', 'remitting multiple-sclerosis',
                   'progressive multiple-sclerosis'],
                  ['1st episode schizophrenia’, ‘1st episode schizophrenia’, ‘1st-episode psychosis’, ‘childhood-onset schizophrenia’, ‘first-episode schizophrenia’, ‘recent-onset schizophrenia’,’ episode schizophrenia’, shizophrenia'],
                  ['emotion regulation’, ‘emotion'],
                  ['adult age-differences', 'age', 'age-related-changes', 'age-related decline', 'aging'],
                  ['attention deficit/hyperactivity disorder', 'deficit hyperactivity disorder', 'ADHD'],
                  ['absence seizures', 'childhood absence epilepsy', 'seizure onset', 'temporal-lobe epilepsy'],
                  ['partial epilepsy', 'focal epilepsy', 'seizures'],
                  ['alcohol-use disorders', 'drug-addiction', 'addiction'],
                  ['appearing white-matter', 'white-matter', 'white-matter', 'white-matter alteration',
                   'white-matter damage', 'white-matter development', 'white-matter hyperintensities',
                   'white-matter integrity', 'white-matter microstructure', 'white-matter microstructure',
                   'white-matter tracts', 'frontal white-matter', 'white matter'],
                  ['gray-level index', 'gray-matter atrophy', 'gray-matter loss', 'gray-matter volume',
                   'cerebral gray-matter', 'grey matter'],
                  ['auditory signal-detection', 'auditory-cortex', 'auditory-feedback control',
                   'primary auditory-cortex', 'left auditory-cortex', 'human auditory-cortex', 'audition'],
                  ['human cerebral-cortex', 'human motor cortex', 'human occipitotemporal cortex',
                   'human orbitofrontal cortex', 'human parietal operculum', 'human sensorimotor cortex',
                   'human temporal-lobe', 'human visual-cortex', 'human extrastriate cortex',
                   'inferior prefrontal cortex', 'inferior frontal-cortex', 'medial prefrontal cortex',
                   'medial temporal-lobe', 'cerebral-cortex', 'ventromedial prefrontal cortex', 'ventral visual-cortex',
                   'cortex activity', 'cortical atrophy', 'cortical activity', 'cortical areas', 'cortical development',
                   'cortical effective connectivity', 'cortical excitability', 'cortical integration',
                   'cortical networks', 'cortical representation', 'cortical surface', 'cortical surface',
                   'cortical thickness', 'cortical underconnectivity', 'corticocortical', 'motor cortex',
                   'orbitofrontal cortex', 'prefrontal cortex', 'temporal cortex', 'cortex'],
                  ['automated image registration', 'registration', 'image registration'],
                  ['axon diameter distribution', 'axonal damage', 'axonal plasticity', 'axonal projections', 'axon'],
                  ['blood oxygenation changes', 'bold hemodynamic-responses', 'bold signal fluctuations',
                   'bold-contrast sensitivity', 'bold signal', 'bold'],
                  ['brains default network', 'default mode', 'default mode network', 'default network', 'default-mode',
                   'default-mode network', 'resting state networks', 'DMN'],
                  ['blood-flow changes', 'cerebral-blood-flow', 'CBF'],
                  ['cognitive control', 'cognitive function', 'cognitive impairment', 'cognitive therapy',
                   'social cognition', 'cognitive control', 'cognitive impairment', 'cognitive neuroscience',
                   'cognitive performance', 'cognition'],
                  ['brain connectivity', 'connectivity mri', 'connectivity-based parcellation',
                   'functional connectivity', 'intrinsic functional connectivity', 'state functional connectivity',
                   'functional connectivity mri', 'connectivity'],
                  ['atlas-based segmentation', 'automatic segmentation', 'tractography-based parcellation',
                   'segmentation'],
                  ['autobiographical memory retrieval', 'recognition memory', 'semantic memory', 'short-term-memory',
                   'working-memory', 'working-memory load', 'working-memory performance', 'memory'],
                  ['brain functional networks', 'functional brain networks', 'complex brain networks',
                   'functional network'],
                  ['deep brain-stimulation', 'transcranial magnetic stimulation', 'transcranial dc stimulation',
                   'noninvasive brain-stimulation', 'direct-current stimulation', 'DBS'],
                  ['brain computer interface', 'brain-computer communication', 'brain-computer interface', 'BCI']
                  ]
    to_replace = merge_dicts([{t: x[-1] for t in x[:-1]} for x in to_replace])
    df['KW'] = df['KW'].map(lambda x: [to_replace.get(s, s) for s in x])
    # Удаление повторов
    df['KW'] = df['KW'].map(lambda x: list(set(x)))
    return df
