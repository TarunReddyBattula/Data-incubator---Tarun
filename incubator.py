from pandas import DataFrame, read_csv

import pandas as pd
import maptolib as plt
# 1) Unique number of clinicians can be taken by NPI as unique PAC ID is greater than NPI, and NPI can not have duplicates
df = pd.read_csv(r'C:\trial.csv')

df['new'] = df['NPI'].map(str) + df['PAC ID'].map(str)
null_columns=df.columns[df.isnull().any()]
print(df[df["Gender"].isnull()][null_columns])

count=df.new.nunique()
count3=df.NPI.nunique()
count4=df['PAC ID'].nunique()
print(count,count3,count4)

# 2) Gender ratio for male to females calculated

span = df.drop_duplicates(subset=['NPI'])

count=span.groupby('Gender').size()
print(count)
print("Ratio=", count[1]/count[0])

# 3) Remove duplicated w.r.t NPI in (Physician_Compare_2015_Individual_EP_Public_Reporting___Performance_Scores.csv) -> Group by credentials and store each credential data in a new dataframe -> find respective ratios and store in an array -> Find highest value in the array
# 4)
#count2=span.nunique()
#print(count2)
#print(new)
#grouped = span.groupby(['Gender'], as_index=False)
#print(grouped)
