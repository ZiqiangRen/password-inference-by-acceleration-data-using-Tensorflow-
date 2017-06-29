import matplotlib
import scipy.io as sio  
import matplotlib.pyplot as plt
from pylab import *
import numpy as np  
import string
import csv

for num in range(2,32,2):
    tmp=[]
    csvname='index/'+str(num)+'.'+str(num+1)+'_features.csv'
    my_matrix = np.loadtxt(open(csvname,"rb"),delimiter=",",skiprows=0)  
    #print(my_matrix)
    if num==2:
        to_save=my_matrix
    else:            
        to_save = np.row_stack([to_save,my_matrix])
    #print(to_save)
to_save=np.delete(to_save,6,axis=1)
np.savetxt('index/total_features.csv', to_save, fmt='%f,%f,%f,%f,%f,%f,%f,%d',delimiter = ',')
print("train datasets simplification -- mission accomplished!\n")
