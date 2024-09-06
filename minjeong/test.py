import pandas
import sklearn

df=pandas.read_csv('basic1.csv')
age=df.age
print(age.mean())
