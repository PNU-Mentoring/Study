import sklearn
import pandas


data = pandas.read_csv('basic1.csv')

mean_age = data['age'].mean()
print(mean_age)
