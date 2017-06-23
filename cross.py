import numpy as np
import tflearn
import csv
import os



def preprocess(data, columns_to_ignore):
    for id in columns_to_ignore:
        [r.pop(id) for r in data]
    return np.array(data, dtype=np.float32)

to_ignore=[]

def create_net():
    net = tflearn.input_data(shape=[None, 7]) 
    net = tflearn.fully_connected(net, 32)
    net = tflearn.fully_connected(net, 32)
    net = tflearn.fully_connected(net, 32, activation='softmax')
    net = tflearn.regression(net)
    return net


def predict(network, modelfile,inputs):
    model = tflearn.DNN(network)
    model.load(modelfile)
    return model.predict(inputs)

if __name__ == '__main__':
    print("\nNow is the 0.8/0.2 cross validation phase : \n")
    my_test=np.zeros([60,8])
    i=0
    csv_reader = csv.reader(open('/home/ziqiangren/ziqiangren/tflearn_sensor/total_features_2.csv', encoding='utf-8'))

    for row in csv_reader:
	    my_test[i]=row
	    i=i+1
    aa=my_test[0:60,0:7].tolist()
    aa = preprocess(aa, to_ignore)

    #print(aa)
    network=create_net()
    pred = predict(network, '/home/ziqiangren/ziqiangren/tflearn_sensor/model_save.model',aa)
    count=0
    for i in range(len(pred)):
        tmp=pred[i][:]
        tmp.sort()
        
        if my_test[i,7]!=pred[i].index(max(pred[i])):
            count=count+1
            print("ground truth:%d  result:%d %d %d %d %d   Error"%(my_test[i,7],pred[i].index(tmp[-1]),pred[i].index(tmp[-2]),pred[i].index(tmp[-3]),pred[i].index(tmp[-4]),pred[i].index(tmp[-5])))
        else:
            print("ground truth:%d  result:%d %d %d %d %d"%(my_test[i,7],pred[i].index(tmp[-1]),pred[i].index(tmp[-2]),pred[i].index(tmp[-3]),pred[i].index(tmp[-4]),pred[i].index(tmp[-5])))
    print('\n')
    print('the total test number is %d with an error rate of %f'%(len(pred),count/len(pred)))
#print("result:", pred[i].index(max(pred[i])))
