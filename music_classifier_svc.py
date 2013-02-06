import csv_io
import numpy as np
from sklearn import cross_validation
from sklearn import svm
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.metrics import metrics
def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("./hotness_features_classes_selected.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )
    train_scaled = preprocessing.scale(train)
    c =  pow(2,-5)
    for index in range(0, 32):
         g = pow(2,-15)
         for jindex in range(0, 18):
                print c, g
         	clf = SVC(C=c, gamma=g)
         	scores = cross_validation.cross_val_score(clf, train_scaled, target, cv=10)
         	print "Accuracy: %0.2f, (+/- %0.2f)" % (scores.mean(), scores.std()/2)	
		g = 2.0 * g
         c = 2.0 * c
if __name__=="__main__":
    main()



     
