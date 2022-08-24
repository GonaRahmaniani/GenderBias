import pandas
import math
import word_strength
# NUMBER 3
filename = input("Enter .csv to calculate on: ")

df = pandas.read_csv(filename)

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

#if (input("Print to working .csv? (y/n) ")=='y'):
df.to_csv(filename, index=False)