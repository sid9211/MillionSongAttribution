import csv_io
import numpy as np
from sklearn import cross_validation
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn import preprocessing
from sklearn.metrics import metrics
def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("./hotness_features_classes_selected.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )
    train_scaled = preprocessing.scale(train)

    #print str(train_scaled)
    #Preprocessing
    # 1. Standardize all features to 0,1
    # 2. Create a SVM Classifier

    clf = LinearSVC()
#   scores = cross_validation.cross_val_score(clf, train_scaled, target, metrics.precision_recall_fscore_support, cv = 5)
#    scores = cross_validation.cross_val_score(clf, train_scaled, target, metrics.classification_report, cv=10)
#    print '%s' % scores
    scores = cross_validation.cross_val_score(clf, train_scaled, target, cv=10)
    print "Accuracy: %0.2f, (+/- %0.2f)" % (scores.mean(), scores.std()/2)
if __name__=="__main__":
    main()



     
