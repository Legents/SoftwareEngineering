import pandas
import math
import csv

data = pandas.read_csv('edge2015_1.csv')
print(data)

sigmoid = []
for data in data['Weight']:
	s = 1.0/(1 + math.exp(-data*1.0))
	sigmoid.append(s)
data['Sigmoid']='1'
