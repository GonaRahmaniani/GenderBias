import pandas

filename=input("please write in csv file: ")
finalname=input("please write new csv filename to be saved: ")
df=pandas.read_csv(filename)
word=[]
male=[]
female=[]

df=df.sort_values(by='Count of Word',ascending=False)
df=df.drop(df.index[list(range(20,len(df['Count of Word'])))])
df=df.reset_index()
word=df['Words']

for i in range(20):
    if df['Gender of Word'][i]=='Female':
        female.append(df['Count of Word'][i])
        male.append(' ')
    else:
        male.append(df['Count of Word'][i])
        female.append(' ')

final_df=pandas.DataFrame({
    
    'Word':word,
    'Female':female,
    'Male':male
    
    })

final_df.to_csv(finalname,index=False)
