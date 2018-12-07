import csv
import math
import pandas as pd
#数据处理
def data_process(file):
	Source,Target,Parameter = [],[],[]
	data = []
	with open(file) as f:
		reader = csv.reader(f)
		header_row = next(reader)
		for row in reader:
			source = row[0]
			target = row[1]
			parameter = row[2]
			Source.append(source)
			Target.append(target)
			Parameter.append(parameter)
	data.append(Source)
	data.append(Target)
	data.append(Parameter)
	return data
#sigmoid归一化处理	
def Sigmoid(data):
	sigmoid = []
	for a in data[2]:
		s = 1.0/(1 + math.exp(-float(a)*1.0))
		sigmoid.append(s)
	data[2] = sigmoid
	return data
#将处理后的数据写回文件
def write_sig(file,data):
	dataframe = pd.DataFrame({'Source':data[0],'Target':data[1],'Sigmoid':data[2]})
	dataframe.to_csv(file,index=False,sep=',')
#计算α	
def get_Alpha():
	α = 0.3
	return α
#使用已有的文件按要求生成新文件	
def combine_files(file1,file2,x):
	α = get_Alpha()
	data1 = data_process(file1)
	data2 = data_process(file2)
	new_source,new_target,new_sigmoid = [],[],[]
	data = []
	for (s1,t1,si1) in zip(data1[0],data1[1],data1[2]):
		j = 0
		flag = 0	#标记是否找到相同数据
		for (s2,t2,si2) in zip(data2[0],data2[1],data2[2]):
			if s1 == s2 and t1 == t2:
				flag = 1
				new_s = s1
				new_t = t1
				new_si = (α * float(si1)) + ((1-α) * float(si2))
				for i in range(0,3):	#删除已计算的数据项
					del data2[i][j]
			j = j + 1
		if flag == 0:
			new_s = s1
			new_t = t1
			new_si = (α * float(si1))
		new_source.append(new_s)
		new_target.append(new_t)
		new_sigmoid.append(new_si)
	for (s2,t2,si2) in zip(data2[0],data2[1],data2[2]):
		new_s = s2
		new_t = t2
		new_si = ((1-α) * float(si2))
		new_source.append(new_s)
		new_target.append(new_t)
		new_sigmoid.append(new_si)
	data.append(new_source)
	data.append(new_target)
	data.append(new_sigmoid)
	file = str(x)+'.csv'
	write_sig(file,data)
	print('文件'+str(x)+'.csv已生成')	
	return file	
		
def main():	
	file = []
	file.append('edge2015_1.csv')
	file.append('edge2015_2.csv')
	file.append('edge2016_1.csv')
	file.append('edge2016_2.csv')
	file.append('edge2017_1.csv')
	file.append('edge2017_2.csv')
	file.append('edge2018_1.csv')
	for i in range(0,7):			#依次处理所有文件的数据			
		data = Sigmoid(data_process(file[i]))
		write_sig(file[i],data)
	x=1
	for i in range(0,12,2):
		f=combine_files(file[i],file[i+1],x)
		file.insert(i+2,f)
		x=x+1
	
main()
