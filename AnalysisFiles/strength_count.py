#calculates percent of gendered words per word count for masculine and feminine words
#separates results into bins with a range of percentages
#results written under 'Fem total bins' and 'Masc total bins' columns
import pandas as pd
import re 
import math 

FILENAMES = [
    'cs_data.csv',
    'eng_data.csv',
    'nurse_data.csv',
]

def histogram_strength(val,gender,bins_total_m,bins_total_f):
	if gender == 'm':
		bins_total = bins_total_m
	else:
		bins_total = bins_total_f

	if val == 0: 
		bins_total[0] += 1

	elif val <= 2: 
		bins_total[1] += 1

	elif val <= 4:
		bins_total[2] += 1

	elif val <= 6:
		bins_total[3] += 1

	elif val <= 8:
		bins_total[4] += 1

	elif val <= 10:
		bins_total[5] += 1
	
	elif val <= 12:
		bins_total[6] += 1
	
	elif val <= 14:
		bins_total[7] += 1
	
	elif val <= 16:
		bins_total[8] += 1

	else:
		bins_total[9] += 1

def strength_count(filename): 
	file = pd.read_csv(filename)
	
	female_arr = []
	male_arr = []
	
	bins_total_label = ["0","(0-2]","(2-4]","(4-6]","(6-8]","(8-10]","(10-12]","(12-14]","(14-16]","16+"]
	bins_total_f = [0,0,0,0,0,0,0,0,0,0]
	bins_total_m = [0,0,0,0,0,0,0,0,0,0]

	for i in range(len(file['Word count'])): 
		count = int(file['Word count'][i])
		
		string_female = file['Feminine words'][i]
		string_male = file['Masculine words'][i]

		female_count = len(string_female.split(","))
		male_count = len(string_male.split(","))

		female_strength = (female_count/count)*100 
		male_strength = (male_count/count)*100

		female_arr.append(female_strength)
		male_arr.append(male_strength)

		histogram_strength(female_strength,'f',bins_total_m,bins_total_f)
		histogram_strength(male_strength,'m',bins_total_m,bins_total_f)

	file['Feminine Strength per total'] = female_arr
	file['Masculine Strength per total'] = male_arr

	bins_df_total = pd.DataFrame({
		'Labels per Total': bins_total_label,
		'Fem total bins':[val/len(file['Word count']) for val in bins_total_f], 
		'Masc total bins':[val/len(file['Word count']) for val in bins_total_m],
		})

	file = pd.concat([file,bins_df_total],axis=1)
	file.to_csv(filename,index=False) 

for file in FILENAMES:
	strength_count(file)