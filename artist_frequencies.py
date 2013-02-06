import numpy as np
import pylab as pl
import matplotlib
import matplotlib.pyplot as plt
import pickle
def main():
    index = 0
    X = []
    Y = []
    total = 0
    mydict = pickle.load(open("artist_hotness.p","rb"))
    for key in mydict:
	print key , len(mydict[key])
        X.append(index)
        index = index + 1
        Y.append(len(mydict[key]))
	total = total + len(mydict[key])

    print total
    plt.plot(X, Y, 'ro')
    plt.hist(Y)
    plt.show()

if __name__=="__main__":
    main()
