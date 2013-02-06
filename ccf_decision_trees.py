from sklearn import tree 
import csv_io
import numpy as np
from sklearn import cross_validation
from sklearn import preprocessing 

def main():
    #read in  data, parse into training and target sets
    train = csv_io.read_data("./hotness_features_classes.csv")
    target = np.array( [x[0] for x in train] )
    train = np.array( [x[1:] for x in train] )
    train_scaled = preprocessing.scale(train)
    clf = tree.DecisionTreeClassifier(random_state = 0)
    scores = cross_validation.cross_val_score(clf, train_scaled, target,None, cv=10)
    print "Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()/2)
if __name__=="__main__":
    main()

