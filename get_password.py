import numpy as np
import csv
import os
import matplotlib
import scipy.io as sio  
import matplotlib.pyplot as plt

#185092
#def password()

input=[27,3,29,20,29,20]
to_fig=np.zeros([7,2])
labels=[[0,0],[0,1],[0,-1],[0,2],[0,-2],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1],[1,2],[-1,-2],[1,-2],[-1,2],[2,0],[-2,0],[2,1],[-2,-1],[2,2],[-2,-2],[2,-1],[-2,1],[2,-2],[-2,2],[3,0],[-3,0],[3,1],[-3,-1],[3,-1],[-3,1]]
num=range(1,32)
n_dict=dict(zip(num,labels))

keybooard=[[0,-1],[-1,-2],[-1,-1],[-1,0],[-2,-2],[-2,-1],[-2,0],[-3,-2],[-3,-1],[-3,0],[0,0]]
key_num=range(0,11)
type_dict=dict(zip(key_num,keybooard))

for i in range(1,7):
    index=input[i-1]
    if i==1:
        to_fig[i]=n_dict[index]
    else:
        to_fig[i]=to_fig[i-1]+n_dict[index]   
#to_fig = to_fig.tolist()
#print('to-fig=',to_fig)
#print('to-fig-1=',to_fig-to_fig[-1])



to_find=to_fig-to_fig[-1]
to_find=to_find.tolist()

#plt.plot(to_fig[0:6,0],to_fig[0:6,1],'ro',label="point")
#plt.show()


#print(type_dict)
result=[]  
key_list=[]
value_list=[]
mydisc=type_dict
for key,value in mydisc.items( ):
    key_list.append(key)
    value_list.append(value)
    
for tmp in to_find:
    #print(tmp)
    if tmp in value_list:
        get_value_index = value_list.index(tmp) 
        #print(key_list[get_value_index])
        result.append(key_list[get_value_index])
    else:
        result.append('Unkown')    
print('result=',result[0:6])
