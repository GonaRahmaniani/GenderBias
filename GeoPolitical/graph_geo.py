#This file will run once for each CSV file created by 'percentage_chart_geo.py'
#One stacked bar graph per file will be created indicating the percentage of ad labelled
#female-associated, male-associated, or neutral

from matplotlib import pyplot as plt
from matplotlib import patches as mp
import numpy as np
import pandas as pd

CLASSES = [
    'size',
    'politics',
    'region',
]

#Change the title of the graph by editing the last variable in each list
NAMES = {
    'size' : ['size.csv', 'size_gender.png', 'Percentage of Ads Labelled Female-associated, Neutral or Male-associated by Size of City'],
    'politics' : ['politics.csv', 'politics_gender.png', 'Percentage of Ads Labelled Female-associated, Neutral or Male-associated by Political Stance of City'],
    'region' : ['region.csv', 'region_gender.png', 'Percentage of Ads Labelled Female-associated, Neutral or Male-associated by Geographical Region'],
}

for CLASS in CLASSES:

    df = pd.read_csv(NAMES[CLASS][0])
    fig, ax = plt.subplots()

    types = df.Type.tolist()
    index = 0
    for type in types:
        types[index] = type.upper()
        index += 1
    feminine = df['Feminine (%)'].tolist()
    neutral = df['Neutral (%)'].tolist()
    masculine = df['Masculine (%)'].tolist()

    title = NAMES[CLASS][2]
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

    plt.savefig(NAMES[CLASS][1], dpi=300, bbox_inches='tight')
