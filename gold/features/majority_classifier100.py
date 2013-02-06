import csv_io
import numpy as np
from Histogram import * 
from sklearn.metrics import metrics
from sklearn import cross_validation
import operator
def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("./best.csv")
    o_target = np.array( [x[0] for x in data] )
    o_train = np.array( [x[1:] for x in data] )

    for i in range(0, 100):
        #Split the data randomly into 80% training and 20% test
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(o_train,o_target, test_size = 0.20)
        #Compute the most frequent class in the training set
        H = histogram(y_train)
        mc = max(H.iteritems(), key=operator.itemgetter(1))[0]
        y_predict = np.empty(len(y_test))
        y_predict[:] = mc
        #print metrics.classification_report(y_test, y_predict)
        print i, str(metrics.zero_one_score(y_test, y_predict)) 
if __name__=="__main__":
    main()



     
