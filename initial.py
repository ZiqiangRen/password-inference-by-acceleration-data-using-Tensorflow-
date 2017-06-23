import numpy as np
import tflearn
import csv
import os
# Load CSV file, indicate that the first column represents labels
from tflearn.data_utils import load_csv
data, labels = load_csv('/home/ziqiangren/ziqiangren/tflearn_sensor/total_features_1.csv', target_column=7,categorical_labels=True, n_classes=32)

# Preprocessing function
def preprocess(data, columns_to_ignore):
    for id in columns_to_ignore:
        [r.pop(id) for r in data]
    return np.array(data, dtype=np.float32)

# Ignore 2 columns (id 1 & 6 of data array)
#to_ignore=[1, 6]
to_ignore=[]

# Preprocess data
data = preprocess(data, to_ignore)

# Build neural network
net = tflearn.input_data(shape=[None, 7]) #7 features for each sample
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32, activation='softmax')#'32' holds for the output size "32"
net = tflearn.regression(net)

# Define model
model = tflearn.DNN(net)
if os.path.isfile('model_save.model'):
	model.load('model_save.model')
# Start training (apply gradient descent algorithm)
for i, (d, l) in enumerate(zip(data, labels)):
    if i >= 20:
        break
    #print(d, l)

model.fit(data, labels, n_epoch=1000, batch_size=16, show_metric=True)
model.save('/home/ziqiangren/ziqiangren/tflearn_sensor/model_save.model')

# Let's create some data for DiCaprio and Winslet
my_test_8 = [39.707819,0.385019,20.199092,0.794156,9.457506,0.145497,0.189150]
my_test_15 = [12.824269,0.360148,9.613503,0.256485,32.222687,1.151379,0.644454]
my_test_19 = [38.670404,0.394162,19.389638,0.773408,-19.383834,0.160869,-0.387677]
my_test_25 = [38.875751,0.319971,23.344817,0.777515,6.669167,0.106691,0.133383]
my_test_31 = [-10.337104,0.579388,-10.426175,-0.206742,-23.319533,0.146307,-0.466391]

# Preprocess data
my_test_8,my_test_15,my_test_19,my_test_25,my_test_31 = preprocess([my_test_8,my_test_15,my_test_19,my_test_25,my_test_31], to_ignore)

'''
my_test=np.zeros([5,8])
i=0
csv_reader = csv.reader(open('birth_features.csv', encoding='utf-8'))
for row in csv_reader:
	my_test[i]=row
	i=i+1

my_test[0],my_test[1],my_test[2],my_test[3],my_test[4] = preprocess([my_test[0],my_test[1],my_test[2],my_test[3],my_test[4]], [6])
'''


# Predict surviving chances (class 1 results)
pred = model.predict([my_test_8,my_test_15,my_test_19,my_test_25,my_test_31])


#print("my_test_1:", pred[0].index(max(pred[0])))
#print("my_test_2:", pred[1].index(max(pred[1])))
#print("my_test_3:", pred[2].index(max(pred[2])))
#print("my_test_4:", pred[3].index(max(pred[3])))
#print("my_test_5:", pred[4].index(max(pred[4])))






