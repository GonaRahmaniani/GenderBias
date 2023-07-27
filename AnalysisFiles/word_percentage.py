#calculates percenetage of ads each gendered word appears in
#results written under 'Percentage of Ads Containing Feminine Word'
#and 'Percentage of Ads Containing Masculine Word' columns
import pandas as pd
import numpy as np

FILENAMES= [
    'cs_data.csv',
    'eng_data.csv',
    'nurse_data.csv',
]

index = 0
for file in FILENAMES:

    df = pd.read_csv(file)
    fem_words_ad = df['Feminine words'].tolist()
    masc_words_ad = df['Masculine words'].tolist()
    word_gender = df['Gender of Word'].tolist()
    word_gender = [gender for gender in word_gender if pd.isna(gender) != True]
    words = df['Words'].tolist()
    words = [word for word in words if pd.isna(word) != True]
    fem_words = []
    masc_words = []

    for i in range(0, len(word_gender)):
        if word_gender[i] == 'Female':
            fem_words.append(words[i])
        else:
            masc_words.append(words[i])

    fem_words_count = []
    for word in fem_words:
        fem_words_count.append(0)
    masc_words_count = []
    for word in masc_words:
        masc_words_count.append(0)

    for list in fem_words_ad:
        list = eval(list)
        index = 0
        for fem_word in fem_words:
            found = False
            for word in list:
                if word.startswith(fem_word):
                    found = True
            if found:
                fem_words_count[index] = fem_words_count[index] + 1
            index += 1

    for list in masc_words_ad:
        list = eval(list)
        index = 0
        for masc_word in masc_words:
            found = False
            for word in list:
                if word.startswith(masc_word):
                    found = True
            if found:
                masc_words_count[index] = masc_words_count[index] + 1
            index += 1

    titles = df['Job Title'].tolist()
    total_ads = len(titles)

    masc_words_per = [count/total_ads*100 for count in masc_words_count]
    fem_words_per = [count/total_ads*100 for count in fem_words_count]

    temp_df_f = pd.DataFrame({
        'Feminine Words (for percentage)' : fem_words,
        'Percentage of Ads Containing Feminine Word' : fem_words_per,
    })

    temp_df_m = pd.DataFrame({
        'Masculine Words (for percentage)' : masc_words,
        'Percentage of Ads Containing Masculine Word' : masc_words_per,
    })

    df = pd.concat([df,temp_df_f,temp_df_m], axis=1)
    df.to_csv(file)

    index += 1