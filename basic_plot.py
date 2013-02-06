import csv_io
import numpy as np
import pylab as pl
import matplotlib
import matplotlib.pyplot as plt

def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("./hotness_features.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )
    fig = plt.figure()
   
    xcol = train[:, 30]
    ycol = train[:, 31]
    print np.corrcoef(xcol, ycol)
    plt.plot(xcol, ycol)
    plt.show()

if __name__=="__main__":
    main()
