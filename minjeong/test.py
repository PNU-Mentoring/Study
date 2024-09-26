import pandas
import sklearn

df=pandas.read_csv('basic1.csv')
age=df.age
print(age.mean())

#age 평균값 출력
df.age.mean()