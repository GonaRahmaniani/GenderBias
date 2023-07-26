from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

TOPIC = 'Nurse'

NAMES_DICT = {
    'Computer Science' : ['Computer Science', 'cs_data.csv', 'cs_word_bins.png'],
    'Engineer' : ['Engineering', 'eng_data.csv', 'eng_word_bins.png'],
    'Nurse' : ['Nursing', 'nurse_data.csv', 'nurse_word_bins.png'],
}

df = pd.read_csv(NAMES_DICT[TOPIC][1])

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

b1 = plt.bar(interval - 0.2, fem_bins, width, color='pink')
b2 = plt.bar(interval + 0.2, masc_bins, width, color='blue')

name = 'Amount of Gendered Words per Word Count for the ' + NAMES_DICT[TOPIC][0] + ' Job Adverts'
plt.title(name)
plt.xticks(interval, labels)
plt.xlabel('Gendered Words per Total Number of Words (%)')
plt.ylabel('Percentage of Ads (%)')
plt.legend([b1, b2], ['Feminine', 'Masculine'], bbox_to_anchor = (1.3, 0.5))

plt.savefig(NAMES_DICT[TOPIC][2], dpi=300, bbox_inches = 'tight')
plt.show()