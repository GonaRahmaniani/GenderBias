from matplotlib import pyplot as plt
from matplotlib import patches as mp
import numpy as np
import pandas as pd

TOPIC = 'Descriptions'

NAMES_DICT = {
    'Total' : ['Ads', 'total_percentage.csv', 'total_percentage.png'],
    'Engineer' : ['Engineering Components', 'eng_percentage.csv', 'eng_percentage.png'],
    'Computer Science' : ['Computer Science Components', 'cs_percentage.csv', 'cs_percentage.png'],
    'Nurse' : ['Nursing Components', 'nurse_percentage.csv', 'nurse_percentage.png'],
    'Descriptions' : ['Descriptions', 'descrip_percentage.csv', 'descrip_percentage.png'],
    'Qualifications' : ['Qualifications', 'qual_percentage.csv', 'qual_percentage.png'],
    'Responsibilities' : ['Responsibilities', 'respon_percentage.csv', 'respon_percentage.png'],
    'Whole' : ['Whole Ads', 'whole_percentage.csv', 'whole_percentage.png'],

}

df = pd.read_csv(NAMES_DICT[TOPIC][1])
fig, ax = plt.subplots()

types = df.Type.tolist()
feminine = df['Feminine (%)'].tolist()
neutral = df['Neutral (%)'].tolist()
masculine = df['Masculine (%)'].tolist()
nothing = df['Nothing (%)'].tolist()

#combining neutral and nothing percentages
for i in range(0, len(neutral)):
    neutral[i] = neutral[i] + nothing[i]

title = 'Percentage of ' + NAMES_DICT[TOPIC][0] + ' Labelled Feminine, Neutral or Masculine'
plt.title(title)

b1 = plt.barh(types, feminine, color='green')
ax.bar_label(b1, label_type='center', fmt='%.2f')
left = feminine
b2 = plt.barh(types, neutral, left=left, color='grey')
ax.bar_label(b2, label_type='center', fmt='%.2f')
for i in range(0, len(neutral)):
    left[i] = left[i] + neutral[i]
b3 = plt.barh(types, masculine, left=left, color='orange')
ax.bar_label(b3, label_type='center', fmt='%.2f')

plt.legend([b1, b2, b3], ['Feminine (%)', 'Neutral (%)', 'Masculine (%)'], bbox_to_anchor = (1.4, 0.5))

plt.savefig(NAMES_DICT[TOPIC][2], dpi=300, bbox_inches='tight')
plt.show()
