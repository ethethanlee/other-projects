import pandas as pd


df = pd.read_csv('/Users/ethanlee/Downloads/obj1.csv')
for n, item in enumerate(df['ra']):
    temp = []
    temp = item.split()
    item = float(temp[0]) + float(float(temp[1])/60) + float(float(temp[2])/3600)
    df.loc[n,'ra'] = item
    print(item)

for n, item in enumerate(df['dec']):
    temp = []
    temp = item.split()
    item = float(temp[0]) + float(float(temp[1])/60) + float(float(temp[2])/3600)
    df.loc[n,'dec'] = item
    print(item)

for n,item in enumerate(df['time']):
    temp = []
    tempp = []
    temppp = []
    temp = item.split()
    tempp = temp[0].split('/') 
    temppp = temp[1].split(':')
    item = float(tempp[1])*24 + float(temppp[0]) + (float(temppp[1])/60)
    df.loc[n,'time']=item  
df.to_csv('result.csv', index = False)  