#creates one bar chart per file in FILENAMES
#graph shows percentage of ads that fall into each bin
#data is taken from the columns created when running 'strength_count.py'
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

FILENAMES = [
    'cs_data.csv',
    'eng_data.csv',
    'nurse_data.csv',
]

FINALNAMES = [
    'cs_word_bins.png',
    'eng_word_bins.png',
    'nurse_word_bins.png',
]

NAMES = [
    'Computer Science',
    'Engineering',
    'Nursing',
]

index = 0
for file in FILENAMES:

    df = pd.read_csv(file)

    labels = df['Labels per Total'].tolist()
    labels.remove('0')
    labels = [label for label in labels if pd.isna(label) != True]
    fem_bins = df['Fem total bins'].tolist()
    fem_bins.remove(0.0)
    fem_bins = [bin for bin in fem_bins if pd.isna(bin) != True]
    masc_bins = df['Masc total bins'].tolist()
    masc_bins.remove(0.0)
    masc_bins = [bin for bin in masc_bins if pd.isna(bin) != True]

    #turn values into percentages
    for i in range(0, len(fem_bins)):
        fem_bins[i] = fem_bins[i] * 100
        masc_bins[i] = masc_bins[i] * 100

    interval = np.arange(len(fem_bins))
    width = 0.4

    b1 = plt.bar(interval - 0.2, fem_bins, width, color='green')
    b2 = plt.bar(interval + 0.2, masc_bins, width, color='orange')

    name = 'Amount of Gendered Words per Word Count for the ' + NAMES[index] + ' Job Adverts'
    plt.title(name)
    plt.xticks(interval, labels)
    plt.xlabel('Gendered Words per Total Number of Words (%)')
    plt.ylabel('Percentage of Ads (%)')
    plt.legend([b1, b2], ['Female Associated', 'Male Associated'], bbox_to_anchor = (1.4, 0.5))

    plt.savefig(FINALNAMES[index], dpi=300, bbox_inches = 'tight')
    plt.clf()
    #plt.show()
    index += 1