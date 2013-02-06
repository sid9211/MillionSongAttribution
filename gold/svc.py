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
    data = csv_io.read_data("./filtered_classes.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )
    train_scaled = preprocessing.scale(train)

    X_train, X_test, y_train, y_test = cross_validation.train_test_split(train_scaled, target, test_size = 0.8)
    clf  = SVC(kernel='linear', C=0.005).fit(X_train, y_train)
    print clf.score(X_test, y_test)
if __name__=="__main__":
    main()



     
