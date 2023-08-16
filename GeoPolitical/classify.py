#make sure 'cities.csv' is in the same directory
# takes CSV files of ads and adds city name, size and political stance under 
#'City', 'Size', and 'Political Stance' (Data from 'cities.csv')
#Adds ad location's region under Region
import pandas

#names of ad files to be classified
FILENAMES = [
    'cs_data.csv',
    'nurse_data.csv',
    'eng_data.csv',
]

#file containing city, population, political data
CITIES = 'cities.csv'
city_df = pandas.read_csv(CITIES)
city_names = city_df['City']
city_sizes = city_df['Classification']
city_politics = city_df['Political Stance']

REGIONS = [
    'Atlantic',
    'Quebec',
    'Ontario',
    'Prairies',
    'British Columbia',
    'Northern Canada',
]

province_names = {
    'Atlantic' : ['NL', 'Newfoundland', 'PE', 'Prince Edward Island', 'NS', 'Nova Scotia', 'NB', 'New Brunswick'],
    'Quebec' : ['QC', 'Quebec'],
    'Ontario' : ['ON' , 'Ontario'],
    'Prairies' : ['MB', 'Manitoba', 'AB', 'Alberta', 'SK', 'Saskatchewan'],
    'British Columbia' : ['BC', 'British Columbia'],
    'Northern Canada' : ['YT', 'Yukon', 'NT', 'Northwest Territories', 'NU', 'Nunavut'],
}

for file in FILENAMES:

    df = pandas.read_csv(file)

    province_list = []
    city_list = []
    population_size_list = []
    political_list = []

    for title in df['Job Title']:
        found = False
        for region in REGIONS:
            for var in province_names[region]:
                check = ' ' + var + ' '
                if ((check in title) and (not found)):
                    province_list.append(region)
                    found = True
        if not found:
            province_list.append('Nothing')

        found = False
        index=0
        for city in city_names:
            check = city
            if ((check in title) and (not found)):
                city_list.append(city)
                population_size_list.append(city_sizes[index])
                political_list.append(city_politics[index])
                found = True
            index += 1
        if not found:
            city_list.append('Nothing')
            population_size_list.append('Nothing')
            political_list.append('Nothing')

    df = pandas.DataFrame({
        'Job Title' : df['Job Title'],
        'Region' : province_list,
        'City' : city_list,
        'Size' : population_size_list,
        'Political Stance' : political_list,
        'Job Ad' : df['Job Ad'],
        'Decoder 1' : df['Decoder 1'],
        'Decoder 2' : df['Decoder 2'],
        'Decoder 4' : df['Decoder 4'],
        'Decoder 6' : df['Decoder 6'],
    })

    df.to_csv(file, index=False)
