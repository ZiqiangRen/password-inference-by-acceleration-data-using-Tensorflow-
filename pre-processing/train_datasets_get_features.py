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
        #print(row)
        speed=zeros(int(row[1])-int(row[0]))
        for i in range(int(row[1])-int(row[0])):
            speed[i]=sum(input_[int(row[0]):int(row[0])+i])    
        shift.append(sum(speed))
        #print('var=',np.var(speed))
        #print(shift)
        variance.append(np.var(speed))
        shift_max_speed.append(sum(speed)/max(speed))
        mean_speed.append(mean(speed))        
    result=np.transpose([shift,variance,shift_max_speed,mean_speed])
    return result[0:20]



for num in range(2,32,2):
    
    txtname='mf'+str(num)+'.'+str(num+1)+'_1.txt'
    csvname='index/'+str(num)+'.'+str(num+1)+'_features.csv'
    pdfname='index/'+str(num)+'.'+str(num+1)+'_shift.pdf'
    indexname='index/'+str(num)+'.'+str(num+1)+'.csv'
    print('loading ',txtname,'...')
    my=np.loadtxt(txtname, skiprows=20)
    x_total=my[1:len(my),0]
    y_total=my[1:len(my),1]
    label=[[num],[num+1]]*10 
    '''
    shift=[]
    variance=[]
    shift_max_speed=[]
    mean_speed=[]
    index=[]
    print(txtname)
    for row in csv_reader:
        #print(row)
        speed=zeros(int(row[1])-int(row[0]))
        for i in range(int(row[1])-int(row[0])):
            speed[i]=sum(x_total[int(row[0]):int(row[0])+i])    
        shift.append(sum(speed))
        #print('var=',np.var(speed))
        #print(shift)
        variance.append(np.var(speed))
        shift_max_speed.append(sum(speed)/max(speed))
        mean_speed.append(mean(speed))
    #plt.figure(figsize=(10,10))
    #plt.plot(shift,'o',color='red')
    #plt.grid(True)
    #plt.show()   
    to_save_x=np.transpose([shift,variance,shift_max_speed,mean_speed]) 
    '''    
    to_save_x=get_features(indexname,x_total)
    to_save_y=get_features(indexname,y_total)    
    #print('to_save_x=',to_save_x)
    #print("to_save_y=",to_save_y)
    to_save = np.append(to_save_x, to_save_y, axis = 1)   
    to_save = np.append(to_save,label,axis = 1)
    #print("to_save=",to_save)
    #plt.savefig(pdfname)
    np.savetxt(csvname, to_save, fmt='%f,%f,%f,%f,%f,%f,%f,%f,%d',delimiter = ',')
    print('writting ',csvname,'...')

print("train datasets get features -- mission acomplished! \n")

