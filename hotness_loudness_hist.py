import csv_io
import numpy as np
import pylab as pl
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde



def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("./hotness_features.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )

    hotness_col = target
    loudness_col = train[:, 0]

    mydict = {}
    loudness_classes = [-40,-35,-30,-25,-20,-15,-10,-5]
    for fclass in loudness_classes:
        mydict[fclass]=[]

    print len(target)
    for i in range(0, len(target)):
	key = loudness_col[i]
	if (key < -35):
	    keyclass = -40
        elif (key < -30):
            keyclass = -35 
	elif (key < -25):
	    keyclass = -30 
	elif (key < -20):
	    keyclass = -25
	elif (key < -15):
	    keyclass = -20
	elif (key < -10):
	    keyclass = -15
	elif (key < -5):
	    keyclass = -10
        else:
	    keyclass = -5 

	value = hotness_col[i]
	mydict[keyclass].append(value)

    print len(mydict[-40] + mydict[-35]) + len(mydict[-30]) + len(mydict[-25]) + len(mydict[-20]) + len(mydict[-15]) + len(mydict[-10]) + len(mydict[-5])

    samp = mydict[-30]
    my_pdf = gaussian_kde(samp)
    x = np.linspace(0,1.0,100)
    plt.plot(x, my_pdf(x), 'r')
    pdf, bins, patches = plt.hist(samp, normed=True)
    print bins 
    print np.sum(pdf * np.diff(bins))
    plt.grid()
    plt.show()

if __name__=="__main__":
    main()
