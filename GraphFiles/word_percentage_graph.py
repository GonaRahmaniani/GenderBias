#runs once for Masculine Words and once for feminine
#Creates grouped bar charts with gendered words common to all job categories
#indicates percentage of ads each word was found in
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

NAMES = [
    ['Female Associated', 'cs_fem_word_percentage_chart.csv', 'eng_fem_word_percentage_chart.csv', 'nurse_fem_word_percentage_chart.csv', 'Feminine Words (for percentage)', 'Percentage of Ads Containing Feminine Word', 'fem_word_percentage.png'],
    ['Male Associated', 'cs_masc_word_percentage_chart.csv', 'eng_masc_word_percentage_chart.csv', 'nurse_masc_word_percentage_chart.csv', 'Masculine Words (for percentage)', 'Percentage of Ads Containing Masculine Word', 'masc_word_percentage.png'],
]

i = 0
for list in NAMES:
    df_cs = pd.read_csv(list[1])
    df_eng = pd.read_csv(list[2])
    df_nurse = pd.read_csv(list[3])

    nurse_words = df_nurse[list[4]].tolist()
    eng_words = df_eng[list[4]].tolist()
    cs_words = df_cs[list[4]].tolist()

    nurse_per = df_nurse[list[5]].tolist()
    eng_per = df_eng[list[5]].tolist()
    cs_per = df_cs[list[5]].tolist()

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

    b1 = plt.bar(interval - 0.2, eng_per, width, color='limegreen')
    b2 = plt.bar(interval, cs_per, width, color='cornflowerblue')
    b3 = plt.bar(interval + 0.2, nurse_per, width, color='orange')

    name = 'Most Common ' + list[0] + ' Words by Percentage'
    plt.title(name)
    plt.xticks(interval, common_words, rotation=45, fontsize=5)
    name = list[0] + ' Words'
    plt.xlabel(name)
    plt.ylabel('Percentage of Ads that Words Were Found In (%)')

    plt.legend([b1, b2, b3], ['Engineering', 'Computer science', 'Nursing'], bbox_to_anchor = (1, 0.5))

    plt.savefig(list[6], dpi=300, bbox_inches ='tight')
    plt.clf()
    #plt.show()

i += 1