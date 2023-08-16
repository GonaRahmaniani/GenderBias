#takes csv files with ads that have already been classified by 'classify.py'
#Creates separate CSV files that contain all of the ads for each
#region, population size, political party
import pandas

#name of files containing ads to be separated by classification
FILENAMES = [
    'cs_data.csv',
    'eng_data.csv',
    'nurse_data.csv',
]

REGIONS = [
    'Atlantic',
    'Quebec',
    'Ontario',
    'Prairies',
    'British Columbia',
    'Northern Canada',
]

REGIONSF = {
    'Atlantic' : 'atlantic.csv',
    'Quebec' : 'quebec.csv',
    'Ontario' : 'ontario.csv',
    'Prairies' : 'prairies.csv',
    'British Columbia' : 'bc.csv',
    'Northern Canada' : 'north.csv',
}

PARTIES = [
    'Liberal',
    'Conservative',
    'NDP',
    'Green',
    'Bloc'
]

PARTIESF = {
    'Liberal' : 'liberal.csv',
    'Conservative' : 'conservative.csv',
    'NDP' : 'ndp.csv',
    'Green' : 'green.csv',
    'Bloc' : 'bloc.csv',
}

SIZES = [
    'rural',
    'small',
    'medium',
    'large',
    'remote',
]

SIZESF = {
    'rural' : 'rural.csv',
    'small' : 'small.csv',
    'medium' : 'medium.csv',
    'large' : 'large.csv',
    'remote' : 'remote.csv',
}

for region in REGIONS:
    frame = pandas.DataFrame()
    frame.to_csv(REGIONSF[region])
for party in PARTIES:
    frame = pandas.DataFrame()
    frame.to_csv(PARTIESF[party])
for size in SIZES:
    frame = pandas.DataFrame()
    frame.to_csv(SIZESF[size])

for file in FILENAMES:
    df = pandas.read_csv(file)

    for region in REGIONS:
        dfs = pandas.read_csv(REGIONSF[region])
        df_region = df[df['Region'] == region]
        final = pandas.concat([dfs, df_region], ignore_index=True)
        final.to_csv(REGIONSF[region])

    for party in PARTIES:
        dfs = pandas.read_csv(PARTIESF[party])
        df_party = df[df['Political Stance'] == party]
        final = pandas.concat([dfs, df_party], ignore_index=True)
        final.to_csv(PARTIESF[party])

    for size in SIZES:
        dfs = pandas.read_csv(SIZESF[size])
        df_size = df[df['Size'] == size]
        final = pandas.concat([dfs, df_size], ignore_index=True)
        final.to_csv(SIZESF[size])
