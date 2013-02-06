import csv_io
import numpy as np
from sklearn import cross_validation
from sklearn import svm
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.metrics import metrics
from sklearn.feature_selection import RFECV
def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("./hotness_features_classes.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )
    train_scaled = preprocessing.scale(train)
    clf = SVC(kernel='linear')
    selector = RFECV(clf, step=1, cv=10)
    selector = selector.fit(train_scaled, target)
    print selector.support_
if __name__=="__main__":
    main()



     
