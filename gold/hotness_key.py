import csv_io
import numpy as np
import pylab as pl
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde



def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("./filtered_classes.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )

    hotness_col = target
    print "Length of target", len(hotness_col)
    col = train[:, 1]

    mydict = {}
    mydict[0] = []
    mydict[1] = []
    for i in range(0, len(hotness_col)):
        key = hotness_col[i]
	val = col[i]
	mydict[key].append(val) 
   
    mylabels = ['Flops','Hits']
    print len(mydict[0]), len(mydict[1])
    plt.hist([mydict[0], mydict[1]], label=mylabels, normed=True) 
    plt.legend(loc='upper left')
    plt.show()

if __name__=="__main__":
    main()
