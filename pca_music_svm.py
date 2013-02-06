import csv_io
import numpy as np
from sklearn.decomposition import PCA
import pylab as pl
from itertools import cycle
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn import cross_validation
def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("./hotness_features_classes.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )

    pca = PCA(n_components=2, whiten=True).fit(train)
    print str(pca.explained_variance_ratio_)
    print str(pca.explained_variance_ratio_.sum())

    X_pca = pca.transform(train)
    print str(len(X_pca));
    clf = LinearSVC(dual=False, penalty='l2')
    scores = cross_validation.cross_val_score(clf, X_pca, target, cv = 10)

    print "Accuracy: %0.2f , (+/- %0.2f)" % (scores.mean(), scores.std()/2)

if __name__=="__main__":
    main()
