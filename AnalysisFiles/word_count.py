#ensure word_strength.py and gendered_words.csv are in same directory when running this file
import pandas
import pandas
from word_strength import dict_f, dict_m
import re
import math
import word_strength
import numpy
# NUMBER 2
#This file counts the number of appearances of the words in the csv file 'gendered_words.csv'
# in the file you want to score and writes the results to said file

#list of files to be analyzed
FILENAMES = [
    'cs_data.csv',
    'cs_data_d.csv',
    'cs_data_q.csv',
    'cs_data_r.csv',
    'eng_data.csv',
    'eng_data_d.csv',
    'eng_data_q.csv',
    'eng_data_r.csv',
    'nurse_data.csv',
    'nurse_data_d.csv',
    'nurse_data_q.csv',
    'nurse_data_r.csv',
]

for file in FILENAMES:

    #filename = input('Please type in csv name with gendered words that need to be counted')
    filename = 'gendered_words.csv'
    word_df = pandas.read_csv(filename)

    filename2 = file
    df = pandas.read_csv(filename2)
    #print(df)

    wordcount_list=[]
    counter=0
    
    ##This part of the code should count the how many times the gendered word appears in the ads
    for item in word_df['Words']:
        for ad in df['Job Ad']:
            #print('\n\n\n')
            #print(ad)
            #print('\n\n\n')
            #exit
            words = str(ad).split()
            for word in words:
                if word.startswith(item):
                     counter+=1
        wordcount_list.append(counter)
        counter=0

    word_df['Count of Word']=wordcount_list

    df=pandas.concat([df,word_df],axis=1)

    f_lists = []
    m_lists = []
    fem_words = []
    masc_words = []

    #unweighted scores
    f_score = 0
    m_score = 0
    f_scores = []
    m_scores = []

    #weighted scores
    wf_score = 0
    wm_score = 0
    wf_scores = []
    wm_scores = []

    abs_score = [] #absolute score; total number of gendered words
    gen_score = [] #gender score; fem score - masc score

    per_fem = [] #percent female score; fem score/word count
    per_masc = [] #percent male score; masc score/word count
    per_abs = [] #percent total score; total score/word count
    per_gen = [] #percent gender score; #gendered words/word count

    #get the words from the csv
    df["Feminine words"]=df["Feminine words"].apply(str)
    for list in df["Feminine words"]:
        clean = re.split('\W+', list)
        filter = [x for x in clean if x.strip()]
        f_lists.append(filter)

    df["Masculine words"]=df["Masculine words"].apply(str)
    for list in df["Masculine words"]:
        clean = re.split('\W+', list)
        filter = [x for x in clean if x.strip()]
        m_lists.append(filter)

    f = word_strength.dict_f
    f_strength = [x for x in f.values()]

    m = word_strength.dict_m
    m_strength = [x for x in m.values()]

    allwords = [x for x in df["Words"] if str(x) != 'nan']
    allcounts = [x for x in df["Count of Word"] if math.isnan(x) is False]
    scores = []

    f_words = allwords[0:58]
    f_counts = allcounts[0:58]
    for x in range(0, len(f_words)):
        #print(f_counts[x]*f_strength[x])
        scores.append(f_counts[x]*f_strength[x])

    m_words = allwords[58:122]
    m_counts = allcounts[58:122]
    for x in range(0, len(m_words)):
        #print(m_counts[x]*m_strength[x])
        scores.append(m_counts[x]*m_strength[x])

    df["Word Scores"] = pandas.Series(scores)

    df.to_csv(filename2, index=False)