import csv
import math
import pandas as pd

def data_process(file):
	Source,Target,Weight = [],[],[]
	data = []
	with open(file) as f1:
		reader = csv.reader(f1)
		header_row = next(reader)
		for row in reader:
			try:
				source = int(row[0])
				target = int(row[1])
				weight = int(row[2])			
			except ValueError:
				print(current_date,'missing data')
			else:
				Source.append(source)
				Target.append(target)
				Weight.append(weight)
	print(Source)
	data.append(Source)
	print(Target)
	data.append(Target)
	print(Weight)
	data.append(Weight)
	return data
	
def Sigmoid(data):
	sigmoid = []
	for x in data[2]:
		s = 1.0/(1 + math.exp(-x*1.0))
		sigmoid.append(s)
	#print(sigmoid)
	data.append(sigmoid)
	return data

def write_sig(file,data):
	dataframe = pd.DataFrame({'Source':data[0],'Target':data[1],'Weight':data[2],'Sigmoid':data[3]})
	dataframe.to_csv(file,index=False,sep=',')

file1 = 'edge2015_1.csv'
data1 = data_process(file1)	
#print(weight1)
data1 = Sigmoid(data1)
print(data1[3])
write_sig(file1,data1)
