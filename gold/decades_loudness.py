import csv_io
import numpy as np
import pylab as pl
import matplotlib
import matplotlib.pyplot as plt

def main():
    #read in  data, parse into training and target sets
    data = csv_io.read_data("./filtered_classes.csv")
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )

    mydict = {}

    yearcol = train[:, 9]
    energycol = train[:, 13]

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

        mydict[decade].append(energycol[i])

    mean60 = np.median(mydict[1960])
    mean70 = np.median(mydict[1970])
    mean80 = np.median(mydict[1980])
    mean90 = np.median(mydict[1990])
    mean2000 = np.median(mydict[2000])
    mean2010  = np.median(mydict[2010])
   
    print mean60, mean70, mean80, mean90, mean2000, mean2010
    print len(mydict[1960]),len(mydict[1970]), len(mydict[1980]), len(mydict[1990]), len(mydict[2000]), len(mydict[2010])
    
    data = [mydict[1960], mydict[1970], mydict[1980], mydict[1990], mydict[2000], mydict[2010]]
    labels = ['1960', '1970', '1980', '1990', '2000','2010']
    plt.hist(data, bins=20, normed=True, label=labels)
    
#    plt.hist(mydict[1960],bins=50, normed=True, label='1960',histtype='stepfilled', cumulative=True)
#    plt.hist(mydict[1980],bins=50, normed=True, label='1980', histtype='stepfilled', cumulative=True)
#    plt.hist(mydict[2010],bins=50 ,normed=True, label='2010', histtype='stepfilled', cumulative=True)
    plt.legend(loc='upper left')
    plt.figure(2)
    plt.plot(labels, [mean60, mean70, mean80, mean90, mean2000, mean2010])
    plt.show()
   
      

    





if __name__=="__main__":
    main()
