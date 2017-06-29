import matplotlib
import scipy.io as sio  
import matplotlib.pyplot as plt
from pylab import *
import numpy as np  
import string

txtname='mf_birth.txt'
csvname='index/birth'+'.csv'
my=np.loadtxt(txtname, skiprows=20)
ban=25 

x_total=my[1:len(my),0]
y_total=my[1:len(my),1]

plt.figure(figsize=(15,20))
energy=x_total**2+y_total**2
window_length=25
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

#print('windows_energy=',windows)  
plt.plot(x_total,color="blue")
#plt.plot(y_total,color="black")
#plt.plot(windows,color="blue")
plt.xlabel("No of samples(i)")
plt.ylabel("energy")
#plt.show()
if len(left)!=20:
    print(txtname)
#print("left=",left)
#print("right=",right)
plt.figure(figsize=(15,20))
plt.plot(y_total,color="black")
plt.plot(left,0.*np.ones(len(left)),'o',color="blue")
plt.plot(right,0.*np.ones(len(left)),'o',color="blue")
#plt.savefig(pdfname)
#plt.show()
l=list(zip(left,right))
#print(l)
np.savetxt(csvname, l, fmt='%d',delimiter = ',')  
print('writting ',csvname,'...')
print("test datasets segmetation -- mission accomplished! \n")

