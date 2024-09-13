import pandas as pd

df=pd.read_csv("basic1.csv")
avg = df['age'].mean()
print(avg)
