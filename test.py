import numpy as np
import tflearn
import csv
import os
import warnings



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
    warnings.filterwarnings("ignore")
    my_test=np.zeros([6,7])
    i=0
    csv_reader = csv.reader(open('/home/ziqiangren/ziqiangren/tflearn_sensor/birth_features.csv', encoding='utf-8'))

    for row in csv_reader:
	    my_test[i]=row
	    i=i+1

    my_test[0],my_test[1],my_test[2],my_test[3],my_test[4],my_test[5] = preprocess([my_test[0],my_test[1],my_test[2],my_test[3],my_test[4],my_test[5]], to_ignore)

    
    network=create_net()
    pred = predict(network, '/home/ziqiangren/ziqiangren/tflearn_sensor/model_save.model',my_test)

    print("\nNow is the testing phase of a sequence of password 185092 :\n")
    print("output label (motion vector from '1' to '8'):", pred[0].index(max(pred[0])))
    print("output label (motion vector from '8' to '5'):", pred[1].index(max(pred[1])))
    print("output label (motion vector from '5' to '0'):", pred[2].index(max(pred[2])))
    print("output label (motion vector from '0' to '9'):", pred[3].index(max(pred[3])))
    print("output label (motion vector from '9' to '2'):", pred[4].index(max(pred[4])))
    print("output label (motion vector from '2' to 'Enter'):", pred[5].index(max(pred[5])))

    input=[pred[0].index(max(pred[0])),pred[1].index(max(pred[1])),pred[2].index(max(pred[2])),pred[3].index(max(pred[3])),pred[4].index(max(pred[4])),pred[5].index(max(pred[5]))]
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
