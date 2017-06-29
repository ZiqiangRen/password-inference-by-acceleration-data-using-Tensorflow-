import matplotlib
import scipy.io as sio  
import matplotlib.pyplot as plt
from pylab import *
import numpy as np  
import string
import csv

def get_features(index_name,input_):
    csv_reader = csv.reader(open(index_name, encoding='utf-8'))
    variance=[]
    shift_max_speed=[]
    mean_speed=[]
    index=[]
    shift=[]    
    for row in csv_reader:
        speed=zeros(int(row[1])-int(row[0]))
        for i in range(int(row[1])-int(row[0])):
            speed[i]=sum(input_[int(row[0]):int(row[0])+i])    
        shift.append(sum(speed))

        variance.append(np.var(speed))
        shift_max_speed.append(sum(speed)/max(speed))
        mean_speed.append(mean(speed))        
    result=np.transpose([shift,variance,shift_max_speed,mean_speed])
    return result[0:20]


txtname='mf_birth.txt'
csvname='/home/ziqiangren/ziqiangren/tflearn_sensor/birth_features.csv'
indexname='index/birth.csv'
my=np.loadtxt(txtname, skiprows=20)
x_total=my[1:len(my),0]
y_total=my[1:len(my),1]

to_save_x=get_features(indexname,x_total)
to_save_y=get_features(indexname,y_total)
to_save=np.append(to_save_x, to_save_y, axis = 1)
to_save=np.delete(to_save,6,axis=1)
np.savetxt(csvname, to_save, fmt='%f,%f,%f,%f,%f,%f,%f',delimiter = ',')
print("test datasets get features -- mission acomplished!\n")

