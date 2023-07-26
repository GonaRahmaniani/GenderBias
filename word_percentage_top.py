import pandas as pd
import numpy as np

TOPIC = 'Nurse'

NAME_DICTS = {
    'Computer Science' : ['cs_data.csv', 'cs_fem_word_percentage_graph.csv', 'cs_masc_word_percentage_graph.csv'],
    'Engineer' : ['eng_data.csv', 'eng_fem_word_percentage_graph.csv', 'eng_masc_word_percentage_graph.csv'],
    'Nurse' : ['nurse_data.csv', 'nurse_fem_word_percentage_graph.csv', 'nurse_masc_word_percentage_graph.csv'],
}

df_f = pd.read_csv(NAME_DICTS[TOPIC][0])
df_m = pd.read_csv(NAME_DICTS[TOPIC][0])
df_f = df_f.sort_values(by='Percentage of Ads Containing Feminine Word', ascending=False)
df_m = df_m.sort_values(by='Percentage of Ads Containing Masculine Word', ascending=False)
df_f = df_f.drop(df_f.index[list(range(20,len(df_f['Percentage of Ads Containing Feminine Word'])))])
df_m = df_m.drop(df_m.index[list(range(20,len(df_m['Percentage of Ads Containing Masculine Word'])))])
df_f = df_f.reset_index()
df_m = df_m.reset_index()

df_m = df_m[['Masculine Words (for percentage)', 'Percentage of Ads Containing Masculine Word']]
df_f = df_f[['Feminine Words (for percentage)', 'Percentage of Ads Containing Feminine Word']]
df_f.to_csv(NAME_DICTS[TOPIC][1])
df_m.to_csv(NAME_DICTS[TOPIC][2])