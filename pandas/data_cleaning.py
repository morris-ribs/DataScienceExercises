import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

files = glob.glob("states*.csv")

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)

us_census.Income  = us_census.Income.replace('[\$,]', '', regex=True)
split_df = us_census['GenderPop'].str.split('_', expand=True)

us_census['Men'] = pd.to_numeric(split_df[0].replace('M', '', regex=True))
us_census['Women'] = pd.to_numeric(split_df[1].replace('F', '', regex=True))

us_census = us_census.fillna(value={"Women":(us_census.TotalPop-us_census.Men)})
duplicates = us_census.duplicated()
us_census = us_census.drop_duplicates()

us_census.Hispanic = pd.to_numeric(us_census.Hispanic.replace('[\%,]', '', regex=True))
us_census.White = pd.to_numeric(us_census.White.replace('[\%,]', '', regex=True))
us_census.Black = pd.to_numeric(us_census.Black.replace('[\%,]', '', regex=True))
us_census.Native = pd.to_numeric(us_census.Native.replace('[\%,]', '', regex=True))
us_census.Asian = pd.to_numeric(us_census.Asian.replace('[\%,]', '', regex=True))
us_census.Pacific = pd.to_numeric(us_census.Pacific.replace('[\%,]', '', regex=True))
us_census = us_census.fillna(value={"Hispanic":0, "White":0, "Black":0, "Native":0, "Asian":0, "Pacific":0})
print(us_census.head())

plt.scatter(us_census.Women, us_census.Income) 
plt.scatter(us_census.Hispanic, us_census.Income) 
plt.scatter(us_census.White, us_census.Income) 
plt.scatter(us_census.Black, us_census.Income) 
plt.scatter(us_census.Native, us_census.Income) 
plt.scatter(us_census.Asian, us_census.Income) 
plt.scatter(us_census.Pacific, us_census.Income) 
plt.show()