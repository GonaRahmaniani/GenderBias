#summarizes the percentage of ads labelled Feminine, Neutral or Masculine
#and writes to separate csv file
import pandas

FINAL_FILENAME = 'gender_percentage_chart.csv'

FILENAMES = [
    'cs_data.csv',
    'cs_data_d.csv',
    'cs_data_q.csv',
    'cs_data_r.csv',
    'eng_data.csv',
    'eng_data_d.csv',
    'eng_data_q.csv',
    'eng_data_r.csv',
    'nurse_data.csv',
    'nurse_data_d.csv',
    'nurse_data_q.csv',
    'nurse_data_r.csv',
]

#enter descriptions for gender percentage charts
DESCRIPTIONS = [
    'Computer Science Whole Ads',
    'Computer Science Descriptions',
    'Computer Science Qualifications',
    'Computer Science Responsibilities',
    'Engineering Whole Ads',
    'Engineering Descriptions',
    'Engineering Qualifications',
    'Engineering Responsibilities',
    'Nursing Whole Ads',
    'Nursing Descriptions',
    'Nursing Qualifications',
    'Nursing Responsibilities',
]

#true = 'y'

type_list=[]
fem=[]
neu=[]
mas=[]
no=[]

index = 0
for file in FILENAMES:

    filename=file
    df=pandas.read_csv(filename)
    type_name=DESCRIPTIONS[index]
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
    fem_percent=(fem_counter/total)*100
    neu_percent=(neutral_counter/total)*100
    mas_percent=(mas_counter/total)*100
    no_percent=(no_counter/total)*100

    neu_percent=neu_percent + no_percent
    
    type_list.append(type_name)
    
    mas.append(mas_percent)
    neu.append(neu_percent)
    fem.append(fem_percent)
    no.append(no_percent)
    
    index += 1
    
final_df=pandas.DataFrame({
'Type':type_list,
'Feminine (%)':fem,
'Neutral (%)':neu,
'Masculine (%)':mas,
                          })


final_df.to_csv(FINAL_FILENAME,index=False)

        

        
