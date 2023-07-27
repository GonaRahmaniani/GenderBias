#This file will run once for the total ads and component data
#Graphs can be made for a subset of the data by separating the total data into smaller
#sections and running this file using the new filename
#One stacked bar graph will be created indicating the percentage of ad labelled
#feminine, neutral or masculine

from matplotlib import pyplot as plt
from matplotlib import patches as mp
import numpy as np
import pandas as pd

FILENAME = 'gender_percentage_chart.csv'

#e.g.: 'Engineering Components', 'Qualifications', etc.
NAME = 'Ads'

FINALNAME = 'total_gender_percentage.png'

df = pd.read_csv(FILENAME)
fig, ax = plt.subplots()

types = df.Type.tolist()
feminine = df['Feminine (%)'].tolist()
neutral = df['Neutral (%)'].tolist()
masculine = df['Masculine (%)'].tolist()
#nothing = df['Nothing (%)'].tolist()

#combining neutral and nothing percentages (this gets done by another file now)
''''for i in range(0, len(neutral)):
    neutral[i] = neutral[i] + nothing[i]
'''
title = 'Percentage of ' + NAME + ' Labelled Female-associated, Neutral or Male-associated'
plt.title(title)

b1 = plt.barh(types, feminine, color='orange')
ax.bar_label(b1, label_type='center', fmt='%.2f')
left = feminine
b2 = plt.barh(types, neutral, left=left, color='yellow')
ax.bar_label(b2, label_type='center', fmt='%.2f')
for i in range(0, len(neutral)):
    left[i] = left[i] + neutral[i]
b3 = plt.barh(types, masculine, left=left, color='skyblue')
ax.bar_label(b3, label_type='center', fmt='%.2f')

plt.legend([b1, b2, b3], ['Female-associated (%)', 'Neutral (%)', 'Male-associated (%)'], bbox_to_anchor = (1.5, 0.5))

plt.savefig(FINALNAME, dpi=300, bbox_inches='tight')
#plt.show()
