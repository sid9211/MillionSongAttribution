import csv_io
from scipy.stats import mode
import numpy as np
import pylab as pl
import matplotlib
import matplotlib.pyplot as plt

def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("./hotness_features.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )

    mydict = {}

    yearcol = train[:, 27]
    keycol = train[:, 1]

    mydict[1960]=[]
    mydict[1970]=[]
    mydict[1980]=[]
    mydict[1990]=[]
    mydict[2000]=[]
    mydict[2010]=[]

    for i in range(0,len(yearcol)) :
        year = yearcol[i]
        if ((year >= 1960) and (year < 1970)):
            decade = 1960
        elif ((year >= 1970) and (year < 1980)):
            decade = 1970
        elif ((year >=1980) and (year < 1990)):
            decade = 1980
	elif ((year >= 1990) and (year < 2000)):
	    decade = 1990
        elif ((year >= 2000) and (year < 2010)):
	    decade = 2000
	else:
	    decade = 2010

        mydict[decade].append(keycol[i])

    print len(mydict[1970])
    
    data = [mydict[1960], mydict[1970], mydict[1980], mydict[1990], mydict[2000], mydict[2010]] 
    labels = ['1960', '1970','1980','1990','2000','2010']

    key1960 = mode(mydict[1960])
    key1970 = mode(mydict[1970])
    key1980 = mode(mydict[1980])
    key1990 = mode(mydict[1990])
    key2000 = mode(mydict[2000])
    key2010 = mode(mydict[2010])
    print key1960[0], key1970[0],key1980[0], key1990[0], key2000[0], key2010[0]

    plt.hist(data,bins=12, normed=True, label=labels, histtype='bar')
    plt.legend()
    plt.show()

if __name__=="__main__":
    main()
