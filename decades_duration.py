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

    mydict = {}

    yearcol = train[:, 27]
    durationcol = train[:, 2]

    mydict[1960]=[]
    mydict[1970]=[]
    mydict[1980]=[]
    mydict[1990]=[]
    mydict[2000]=[]
    mydict[2010]=[]
    decade2010 = 0

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
            decade2010 = decade2010 + 1
	    decade = 2010

        mydict[decade].append(durationcol[i])

    print decade2010
   
    data = [mydict[1960], mydict[1970], mydict[1980], mydict[1990], mydict[2000], mydict[2010]] 
    labels = ['1960', '1970','1980','1990','2000','2010']

    mean60 = np.mean(mydict[1960])
    mean70 = np.mean(mydict[1970])
    mean80 = np.mean(mydict[1980])
    mean90 = np.mean(mydict[1990])
    mean2000 = np.mean(mydict[2000])
    mean2010  = np.mean(mydict[2010])


    plt.hist(data,bins=10, normed=True, label=labels, histtype='bar', cumulative=True)
    plt.legend()
    plt.figure(2)
    plt.plot(labels, [mean60, mean70, mean80, mean90, mean2000, mean2010], "ro")


    plt.show()
   
      

    





if __name__=="__main__":
    main()
