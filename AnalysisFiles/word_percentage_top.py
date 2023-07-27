#calculates top 20 words that appear in the highest percentage of ads
#for each gender and places into file for feminine words or masculine words
import pandas as pd
import numpy as np

FILENAMES = [
    'cs_data.csv',
    'eng_data.csv',
    'nurse_data.csv',
]

FINALNAMES_FEM_LIST = [
    'cs_fem_word_percentage_chart.csv',
    'eng_fem_word_percentage_chart.csv',
    'nurse_fem_word_percentage_chart.csv',
]

FINALNAMES_MASC_LIST = [
    'cs_masc_word_percentage_chart.csv',
    'eng_masc_word_percentage_chart.csv',
    'nurse_masc_word_percentage_chart.csv',
]

index = 0
for file in FILENAMES:
    df_f = pd.read_csv(file)
    df_m = pd.read_csv(file)
    df_f = df_f.sort_values(by='Percentage of Ads Containing Feminine Word', ascending=False)
    df_m = df_m.sort_values(by='Percentage of Ads Containing Masculine Word', ascending=False)
    df_f = df_f.drop(df_f.index[list(range(20,len(df_f['Percentage of Ads Containing Feminine Word'])))])
    df_m = df_m.drop(df_m.index[list(range(20,len(df_m['Percentage of Ads Containing Masculine Word'])))])
    df_f = df_f.reset_index()
    df_m = df_m.reset_index()

    df_m = df_m[['Masculine Words (for percentage)', 'Percentage of Ads Containing Masculine Word']]
    df_f = df_f[['Feminine Words (for percentage)', 'Percentage of Ads Containing Feminine Word']]
    df_f.to_csv(FINALNAMES_FEM_LIST[index])
    df_m.to_csv(FINALNAMES_MASC_LIST[index])

    index += 1