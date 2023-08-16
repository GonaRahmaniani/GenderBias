#Takes CSV files with ads separated by region, population size, political party
#creates three different CSV files for regions, sizes, and politics
#containing the gender percentage data in each category
import pandas

CLASSES = [
    'political',
    'size',
    'region',
]

NAMES = {
    'political' : ['politics.csv', ['liberal.csv', 'bloc.csv', 'conservative.csv', 'green.csv', 'ndp.csv']],
    'size' : ['size.csv', ['rural.csv', 'small.csv', 'medium.csv', 'large.csv', 'remote.csv']],
    'region' : ['region.csv', ['atlantic.csv', 'bc.csv', 'north.csv', 'prairies.csv', 'quebec.csv', 'ontario.csv']]
}

for CLASS in CLASSES:

    true = 'y'
    type_list=[]
    fem=[]
    neu=[]
    mas=[]
    no=[]

    for file in NAMES[CLASS][1]:
        df=pandas.read_csv(file)
        type_name=file.rsplit('.csv', 1)[0]
        fem_counter=0
        neutral_counter=0
        mas_counter=0
        no_counter=0
        i=0
        
        df["Decoder 1"]=df["Decoder 1"].apply(str)
        df["Decoder 2"]=df["Decoder 2"].apply(str)
        df["Decoder 4"]=df["Decoder 4"].apply(str)
        df["Decoder 6"]=df["Decoder 6"].apply(str)

        while i<len(df['Decoder 1']):
            if "Female" in df['Decoder 1'][i]:
                fem_counter+=1
            if "Female" in df['Decoder 2'][i]:
                fem_counter+=1
            if "Female" in df['Decoder 4'][i]:
                fem_counter+=1
            if "Female" in df['Decoder 6'][i]:
                fem_counter+=1

                
            if "Neutral" in df['Decoder 1'][i]:
                neutral_counter+=1
            if "Neutral" in df['Decoder 2'][i]:
                neutral_counter+=1
            if "Neutral" in df['Decoder 4'][i]:
                neutral_counter+=1
            if "Neutral" in df['Decoder 6'][i]:
                neutral_counter+=1

            if "Male" in df['Decoder 1'][i]:
                mas_counter+=1
            if "Male" in df['Decoder 2'][i]:
                mas_counter+=1
            if "Male" in df['Decoder 4'][i]:
                mas_counter+=1
            if "Male" in df['Decoder 6'][i]:
                mas_counter+=1

            if "Nothing" in df['Decoder 1'][i]:
                no_counter+=1
            if "Nothing" in df['Decoder 2'][i]:
                no_counter+=1
            if "Nothing" in df['Decoder 4'][i]:
                no_counter+=1
            if "Nothing" in df['Decoder 6'][i]:
                no_counter+=1
                
            i +=1
        
        total=fem_counter+mas_counter+neutral_counter+no_counter
        if fem_counter != 0:
            fem_percent=(fem_counter/total)*100
        else:
            fem_percent = 0
        if neutral_counter != 0:
            neu_percent=(neutral_counter/total)*100
        else:
            neu_percent = 0
        if mas_counter != 0:
            mas_percent=(mas_counter/total)*100
        else:
            mas_percent = 0
        if no_counter != 0:
            no_percent=(no_counter/total)*100
        else:
            no_percent = 0
        
        type_list.append(type_name)
        
        neu_percent = no_percent + neu_percent
        mas.append(mas_percent)
        neu.append(neu_percent)
        fem.append(fem_percent)
        
    final_df=pandas.DataFrame({
        'Type':type_list,
        'Feminine (%)':fem,
        'Neutral (%)':neu,
        'Masculine (%)':mas,
    })

    final_df.to_csv(NAMES[CLASS][0])
