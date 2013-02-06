import csv_io
import numpy as np
from sklearn.decomposition import PCA
import pylab as pl
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn import svm
from sklearn.svm import LinearSVC
from sklearn import cross_validation

def plot_2D(data, target, target_names):
	colors = cycle('rgbcmykw')
	target_ids = [0,1]
	print str(target_ids)
	pl.figure(2)
	for i, c, label in zip(target_ids, colors, target_names):
		pl.scatter(data[target == i, 0], data[target == i, 1],
		c=c, label=label)
	pl.title('2D PCA Projection of the data set')
	pl.legend()
	pl.show()

def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("filtered_classes.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )

    pca = PCA(whiten=True).fit(train)
    print str(pca.components_)
    print str(pca.explained_variance_ratio_)
    print str(pca.explained_variance_ratio_.sum())

    plt.figure(1)
    plt.plot(pca.explained_variance_ratio_)

    X_pca = pca.transform(train)
    print str(len(X_pca));


    target_names = ["Flops", "Hits" ]
    plot_2D(X_pca, target, target_names)   

if __name__=="__main__":
    main()
