#Creates bar charts showing top 20 most common gendered words per ad category
#Creates separate graph for each filename specified below
from matplotlib import pyplot as plt
from matplotlib import patches as mp
import pandas as pd
import numpy as np

#Will be included in title of graphs
NAMES = [
    'Computer Science',
    'Engineering',
    'Nursing',
]

#files that were created previously using 'common_word_charts.py'
FILENAMES = [
    'cs_word_chart.csv',
    'eng_word_chart.csv',
    'nurse_word_chart.csv'
]

#name of files that will contain final graphs
FINALNAMES = [
    'common_words_cs_2023.png',
    'common_words_eng_2023.png',
    'common_words_nurse_2023.png',
]

i = 0
for file in FILENAMES:

    df = pd.read_csv(file)

    words = df.Word.tolist()

    fem_count = df.Female.tolist()
    male_count = df.Male.tolist()

    colours = []
    counts = []

    index = 0
    for count in fem_count:
        if fem_count[index] != ' ' and pd.isna(fem_count[index]) != True:
            colours.append('green')
            counts.append(float(fem_count[index]))
        else:
            colours.append('orange')
            counts.append(float(male_count[index]))
        index += 1

    plt.bar(x=words,height=counts,color=colours, width=0.8, align='center')

    plt.title("Most Common Gendered Words in " + NAMES[i] + " Ads")
    plt.xticks(rotation=45, fontsize=5)
    plt.xlabel('Words')
    plt.ylabel('Count of Word')

    female = mp.Patch(color='green', label='Female Associated')
    male = mp.Patch(color='orange', label='Male Associated')
    plt.legend(handles =[female,male])

    plt.savefig(FINALNAMES[i], dpi=300, bbox_inches='tight')
    plt.clf()
    #plt.show()

    i += 1