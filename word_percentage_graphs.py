from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

TOPIC = 'Masculine'

NAME_DICT = {
    'Feminine' : ['Feminine', 'cs_fem_word_percentage_graph.csv', 'eng_fem_word_percentage_graph.csv', 'nurse_fem_word_percentage_graph.csv', 'Feminine Words (for percentage)', 'Percentage of Ads Containing Feminine Word', 'fem_word_percentage.png'],
    'Masculine' : ['Masculine', 'cs_masc_word_percentage_graph.csv', 'eng_masc_word_percentage_graph.csv', 'nurse_masc_word_percentage_graph.csv', 'Masculine Words (for percentage)', 'Percentage of Ads Containing Masculine Word', 'masc_word_percentage.png'],
}

df_cs = pd.read_csv(NAME_DICT[TOPIC][1])
df_eng = pd.read_csv(NAME_DICT[TOPIC][2])
df_nurse = pd.read_csv(NAME_DICT[TOPIC][3])

nurse_words = df_nurse[NAME_DICT[TOPIC][4]].tolist()
eng_words = df_eng[NAME_DICT[TOPIC][4]].tolist()
cs_words = df_cs[NAME_DICT[TOPIC][4]].tolist()

nurse_per = df_nurse[NAME_DICT[TOPIC][5]].tolist()
eng_per = df_eng[NAME_DICT[TOPIC][5]].tolist()
cs_per = df_cs[NAME_DICT[TOPIC][5]].tolist()

nurse_dict = {}
index = 0
for word in nurse_words:
    nurse_dict[word] = nurse_per[index]
    index += 1

eng_dict = {}
index = 0
for word in eng_words:
    eng_dict[word] = eng_per[index]
    index += 1

cs_dict = {}
index = 0
for word in cs_words:
    cs_dict[word] = cs_per[index]
    index += 1

common_words = []

for word in cs_words:
    if (word in nurse_words) and (word in eng_words):
        common_words.append(word)

common_words = sorted(common_words)
nurse_per.clear()
cs_per.clear()
eng_per.clear()
for word in common_words:
    nurse_per.append(nurse_dict[word])
    cs_per.append(cs_dict[word])
    eng_per.append(eng_dict[word])

interval = np.arange(len(common_words))
width = 0.2

b1 = plt.bar(interval - 0.2, eng_per, width, color='green')
b2 = plt.bar(interval, cs_per, width, color='blue')
b3 = plt.bar(interval + 0.2, nurse_per, width, color='orange')

name = 'Most Common ' + NAME_DICT[TOPIC][0] + ' Words by Percentage'
plt.title(name)
plt.xticks(interval, common_words, rotation=45, fontsize=5)
name = NAME_DICT[TOPIC][0] + 'Words'
plt.xlabel(name)
plt.ylabel('Percentage of Ads that Words Were Found In (%)')

plt.legend([b1, b2, b3], ['Engineering', 'Computer science', 'Nursing'], bbox_to_anchor = (1, 0.5))

plt.savefig(NAME_DICT[TOPIC][6], dpi=300, bbox_inches ='tight')
plt.show()
