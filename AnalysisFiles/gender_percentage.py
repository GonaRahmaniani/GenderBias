import pandas


true = 'y'
type_list=[]
fem=[]
neu=[]
mas=[]
no=[]

while true=='y':
    filename=input('write in csv')
    df=pandas.read_csv(filename)
    type_name=input('please enter type name: eg. Engineering Description')
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
    
    type_list.append(type_name)
    
    mas.append(mas_percent)
    neu.append(neu_percent)
    fem.append(fem_percent)
    no.append(no_percent)
    
    true = input("another csv file?")
    
final_df=pandas.DataFrame({
'Type':type_list,
'Feminine (%)':fem,
'Neutral (%)':neu,
'Masculine (%)':mas,
'Nothing (%)':no
                          })


final_df.to_csv(input('write in final name'),index=False)

        

        
