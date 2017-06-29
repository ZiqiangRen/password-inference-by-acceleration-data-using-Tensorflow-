#coding=utf-8

#urllib模块提供了读取Web页面数据的接口
import urllib.request
#re模块主要包含了正则表达式
import re


#for mom in range(1,10):
for idx in range(1,100):
    try:
        url='http://www.aafie.com/images/College/General/DT/FinalView/Slide'+str(idx)+'.JPG'
        name="Final_"+str(idx)+'.jpg'            
        urllib.request.urlretrieve(url,name )
        print(url)
    except:            
        break

            
    
       
print('end')


