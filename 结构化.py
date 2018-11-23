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

def data_process_2(file):
	Source,Target,Weight,Sigmoid = [],[],[],[]
	data = []
	with open(file) as f1:
		reader = csv.reader(f1)
		header_row = next(reader)
		for row in reader:
			source = int(row[0])
			target = int(row[1])
			weight = int(row[2])
			sigmoid = row[3]
						
			Source.append(source)
			Target.append(target)
			Weight.append(weight)
			Sigmoid.append(sigmoid)
	data.append(Source)
	data.append(Target)
	data.append(Weight)
	data.append(Sigmoid)
	return data
	
def get_Alpha():
	Alpha = 0.3
	return Alpha
	
def combine_files(file1,file2):
	alpha = get_Alpha()
	data1 = data_process_2(file1)
	data2 = data_process_2(file2)
	new_source,new_target,new_weight = [],[],[]
	data = []
	i=0
	for (s1,t1,w1,si1) in zip(data1[0],data1[1],data1[2],data1[3]):
		j=0
		flag = 0
		for (s2,t2,w2,si2) in zip(data2[0],data2[1],data2[2],data2[3]):
			if s1==s2 and t1==t2:
				flag = 1
				new_s = s1
				new_t = t1
				new_w = int(alpha * w1) + int((1-alpha) * w2)
				del data2[0][j]
				del data2[1][j]
				del data2[2][j]
				del data2[3][j]
			j = j + 1
		if flag == 0:
			new_s = s1
			new_t = t1
			new_w = int(alpha * w1)
		new_source.append(new_s)
		new_target.append(new_t)
		new_weight.append(new_w)
	for (s2,t2,w2,si2) in zip(data2[0],data2[1],data2[2],data2[3]):
		new_s = s2
		new_t = t2
		new_w = int((1-alpha) * w2)
		new_source.append(new_s)
		new_target.append(new_t)
		new_weight.append(new_w)
	data.append(new_source)
	data.append(new_target)
	data.append(new_weight)
	file = '1.csv'
	data = Sigmoid(data)
	write_sig(file,data)	
	return file		
	
file = []
file.append('edge2015_1.csv')
file.append('edge2015_2.csv')
file.append('edge2016_1.csv')
file.append('edge2016_2.csv')
file.append('edge2017_1.csv')
file.append('edge2017_2.csv')
file.append('edge2018_1.csv')
for i in range(0,7):
	data1 = data_process(file[i])	
	#print(weight1)
	data1 = Sigmoid(data1)
	print(data1[3])
	write_sig(file[i],data1)

combine_files(file[0],file[1])
