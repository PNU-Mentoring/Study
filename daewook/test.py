import pandas as pd
import sklearn

df = pd.read_csv('basic1.csv')
age_mean = df['age'].mean()

print(age_mean)