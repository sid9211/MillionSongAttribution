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

    keycol = train[:, 1]
    hotnesscol = target

    mydict[0]=[]
    mydict[1]=[]
    mydict[2]=[]
    mydict[3]=[]
    mydict[4]=[]
    mydict[5]= []

    mydict[6]=[]
    mydict[7]=[]
    mydict[8]=[]
    mydict[9]=[]
    mydict[10]=[]
    mydict[11]=[]
  
    data = []

    for i in range(0,len(keycol)) :
        key = keycol[i]
        mydict[key].append(hotnesscol[i])

    for i in range(0,12):
	data.append(mydict[i])

    labels = ['C','C#', 'D','D#','E','F','F#','G','G#','A','A#','B']
    plt.hist(data, normed=True, label=labels) 
    plt.legend()
    plt.show()
   
      

    





if __name__=="__main__":
    main()
