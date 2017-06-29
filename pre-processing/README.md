Our pre-processing method includes mainly sensor acceleration data segmentation and features extraction. Since the datasets(train sets and test sets) are still under construction and maintenance, they are not showed here. However, you can add your own datasets into the path and change the program parameters to make sure they are suitable for your own datasets.

The order of program execution is: (Python 3.5.2 |Anaconda custom (64-bit))

python train_datasets_segmetation.py
python train_datasets_get_features.py
python train_datasets_simplification.py
python test_datasets_segmetation.py
python test_datasets_get_features.py
