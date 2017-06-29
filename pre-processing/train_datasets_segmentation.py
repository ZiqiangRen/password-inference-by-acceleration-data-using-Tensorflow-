import matplotlib
import scipy.io as sio  
import matplotlib.pyplot as plt
from pylab import *
import numpy as np  
import string
import data_util


'''   
    print('energy=',energy)
    print('sumary=',sum(x_total))   #to sum up
    print('meanx=',np.mean(x_total))   #to get the mean value
    print('meany=',np.mean(y_total)) 
    print('var=',np.var(x_total))
    plt.savefig('test1.pdf')
    
    plt.figure(figsize=(10,12))
    fig, ax = plt.subplots()
    a=plt.subplot(211)
    plt.sca(a)
    plt.plot(my[1:len(my),0]) ;
    plt.xlabel("No of samples(i)")
    plt.ylabel("Acceleration_x")
    plt.ylim(-0.5,0.5)
    plt.plot([3+win-ban-5,3+win-ban],[0,1],color="green")
    plt.plot([3+win+ban-5,3+win+ban],[0,1],color="green")
    b=plt.subplot(212)
    plt.sca(b)
    plt.plot(my[1:len(my),1]) ;
    plt.xlabel("No of samples(i)")
    plt.ylabel("Acceleration_y")
    plt.ylim(-0.5,0.5)
    plt.plot([3+win-ban-5,3+win-ban],[0,1],color="green")
    plt.plot([3+win+ban-5,3+win+ban],[0,1],color="green")
    plt.show()
'''


for num in range(2,32,2):        
    txtname='mf'+str(num)+'.'+str(num+1)+'_1.txt'
    csvname='index/'+str(num)+'.'+str(num+1)+'.csv'
    pdfname='index/'+str(num)+'.'+str(num+1)+'.pdf'
    my=np.loadtxt(txtname, skiprows=20)
    print('loading ',txtname,'...')
    ban=25 
    x_total=my[1:len(my),0]
    y_total=my[1:len(my),1]
    plt.figure(figsize=(15,20))
    energy=x_total**2+y_total**2
    window_length=25   # the value is 20 before 3/31/2017 
    windows=zeros(len(energy))
    for win in range(len(energy)):
        windows[win]=sum(energy[win:win+window_length+1])
    left,right=[],[]    
    average=np.mean(windows)
    for win in range(10,len(energy)-1):
        if windows[win]>max(windows[win-10:win]) and windows[win]>max(windows[win+1:win+10]) and windows[win]>average:
            #print(win)
            #plt.plot(3+win,windows[win],'o',color="red")
            left_line=[(3+win-ban,0),(3+win-ban,1)]
            right_line=[(3+win+ban,0),(3+win+ban,1)]
            plt.plot([3+win-ban,3+win-ban],[-1,1],color="black")
            plt.plot([3+win+ban,3+win+ban],[-1,1],color="black")
            left.append(3+win-ban)
            right.append(3+win+ban)
    plt.plot(x_total,color="blue")
    plt.xlabel("No of samples(i)")
    plt.ylabel("energy")
    if len(left)!=20:
        print(txtname)    
    plt.figure(figsize=(15,20))
    plt.plot(y_total,color="black")
    plt.plot(left,0.*np.ones(len(left)),'o',color="blue")
    
    plt.plot(right,0.*np.ones(len(left)),'o',color="blue")
    #plt.savefig(pdfname)
    #plt.show()
    
    l=list(zip(left,right))    
    np.savetxt(csvname, l, fmt='%d',delimiter = ',')
    print('writting ',csvname,'...')
print("\ntrain datasets segmetation -- mission accomplished! \n")
