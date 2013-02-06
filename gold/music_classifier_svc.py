import csv_io
import numpy as np
from sklearn import cross_validation
from sklearn import grid_search
from sklearn import svm
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.metrics import metrics
def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("./filtered_classes_musiconly.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )
    train_scaled = preprocessing.scale(train)
    clf  = SVC(kernel='rbf', C=1000, gamma=0.001)
    scores = cross_validation.cross_val_score(clf, train_scaled, target, metrics.classification_report, cv=10)
    print scores
    #cores = cross_validation.cross_val_score(clf, train_scaled, target, cv=10)
    #print "Accuracy: %0.2f, (+/- %0.2f)" % (scores.mean(), scores.std()/2)	
if __name__=="__main__":
    main()



     
