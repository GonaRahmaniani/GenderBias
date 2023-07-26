from matplotlib import pyplot as plt
from matplotlib import patches as mp
import pandas as pd
import numpy as np

TOPIC = 'Nurse'

NAMES_DICT = {
    'Computer Science' : ['Computer Science', 'cs_graph.csv', 'common_words_cs_2023.png'],
    'Engineer' : ['Engineering', 'eng_graph.csv', 'common_words_eng_2023.png'],
    'Nurse' : ['Nursing', 'nurse_graph.csv', 'common_words_nurse_2023.png'],
}

df = pd.read_csv(NAMES_DICT[TOPIC][1])

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

plt.title("Most Common Words in " + NAMES_DICT[TOPIC][0] + " Ads")
plt.xticks(rotation=45, fontsize=5)
plt.xlabel('Words')
plt.ylabel('Count of Word')

female = mp.Patch(color='green', label='Female')
male = mp.Patch(color='orange', label='Male')
plt.legend(handles =[female,male])

plt.savefig(NAMES_DICT[TOPIC][2], dpi=300, bbox_inches='tight')
plt.show()