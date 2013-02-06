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

    hotness_col = target
    artisthotnesscol = train[:, 31]

    mydict = {}
    artisthotness_classes = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    for fclass in artisthotness_classes:
        mydict[fclass]=[]

    print len(target)
    for i in range(0, len(target)):
	key = artisthotnesscol[i]
	if (key < 0.2):
	    keyclass = 0.0
        elif (key < 0.4):
            keyclass = 0.2
	elif (key < 0.6):
	    keyclass = 0.4
	elif (key < 0.8):
	    keyclass = 0.6
	else:
	    keyclass = 0.8

	value = hotness_col[i]
	mydict[keyclass].append(value)
        
        if keyclass == 0.0 and value > 0.6:
	   print "Song" , i 

    print len(mydict[0.0]) + len(mydict[0.2]) + len(mydict[0.4]) + len(mydict[0.6]) + len(mydict[0.8])
    plt.hist(mydict[0.6])
    plt.show()
	    

if __name__=="__main__":
    main()
