from collections import Counter
from statistics import median
import csv

with open('SOCR-HeightWeight.csv',newline='') as f :
    reader =  csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
total=0
for x in new_data:
    total=total+x

mean = total/n
print("mean/average is: "+str(mean))


#for median
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
new_data.sort()

if n%2==0 :
    median1= float(new_data[n//2])
    median2= float(new_data[n//2-1])
    median=(median1+median2)/2
else :
    median= new_data[n//2]
    print(n)

print("median is: "+str(median))

#for mode
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

data = Counter(new_data)
mode_data_for_range = {
    "50-60":0,
    "60-70":0,
    "70-80":0,
}
for height,occurance in data.items():
    if 50<float(height)<60:
        mode_data_for_range["50-60"]+=occurance
    elif 60<float(height)<70:
        mode_data_for_range["60-70"]+=occurance
    elif 70<float(height)<80:
        mode_data_for_range["70-80"]+=occurance

mode_range,mode_occurance=0,0
for range,occurance in mode_data_for_range.items():
    if occurance>mode_occurance:
        mode_range,mode_occurance=[int(range.split("-")[0]),int(range.split("-")[1])],occurance
        

mode = float((mode_range[0]+mode_range[1])/2)
print("mode is "+str(mode))
    