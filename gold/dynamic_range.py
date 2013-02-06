"""
Tutorial for the Million Song Dataset

by Thierry Bertin-Mahieux (2011) Columbia University
   tb2332@columbia.edu
   Copyright 2011 T. Bertin-Mahieux, All Rights Reserved

This tutorial will walk you through a quick experiment
using the Million Song Dataset (MSD). We will actually be working
on the 10K songs subset for speed issues, but the code should
transpose seamlessly.

In this tutorial, we do simple metadata analysis. We look at
which artist has the most songs by iterating over the whole
dataset and using an SQLite database.

You need to have the MSD code downloaded from GITHUB.
See the MSD website for details:
http://labrosa.ee.columbia.edu/millionsong/

If you have any questions regarding the dataset or this tutorial,
please first take a look at the website. Send us an email
if you haven't found the answer.

Note: this tutorial is developed using Python 2.6
      on an Ubuntu machine. PDF created using 'pyreport'.
"""

# usual imports
import os
import sys
import time
import glob
import datetime
import sqlite3
import numpy as np # get it at: http://numpy.scipy.org/
import math
import pickle

from csv_io import *
from ListtoCSV import *
import  matplotlib.pyplot as plt
import echonest.audio as audio
from pyechonest import config
config.ECHO_NEST_API_KEY = "RQXNEZNEIJWY6YM35"
from pyechonest import song
from scipy.stats import *


# path to the Million Song Dataset subset (uncompressed)
# CHANGE IT TO YOUR LOCAL CONFIGURATION
msd_subset_path='/home/vivek/CompBio/data/MSD/MillionSongSubset/'
msd_subset_data_path=os.path.join(msd_subset_path,'data')
msd_subset_addf_path=os.path.join(msd_subset_path,'AdditionalFiles')
assert os.path.isdir(msd_subset_path),'wrong path' # sanity check

# path to the Million Song Dataset code
# CHANGE IT TO YOUR LOCAL CONFIGURATION
msd_code_path='/home/vivek/CompBio/data/MSD/'
assert os.path.isdir(msd_code_path),'wrong path' # sanity check
# we add some paths to python so we can import MSD code
# Ubuntu: you can change the environment variable PYTHONPATH
# in your .bashrc file so you do not have to type these lines
sys.path.append( os.path.join(msd_code_path,'PythonSrc') )

# imports specific to the MSD
import hdf5_getters as GETTERS

# we define this very useful function to iterate the files
def apply_to_all_files(basedir,func=lambda x: x,ext='.h5'):
    """
    From a base directory, go through all subdirectories,
    find all files with the given extension, apply the
    given function 'func' to all of them.
    If no 'func' is passed, we do nothing except counting.
    INPUT
       basedir  - base directory of the dataset
       func     - function to apply to all filenames
       ext      - extension, .h5 by default
    RETURN
       number of files
    """
    cnt = 0
    # iterate over all files in all subdirectories
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        # count files
        cnt += len(files)
        # apply function to all files
        for f in files :
            func(f)       
    return cnt

# we can now easily count the number of files in the dataset
print 'number of song files:',apply_to_all_files(msd_subset_data_path)
listfeatures = []
listtitle =['Immigrant Song']
cntnan = 0
# we define the function to apply to all files
def func_to_extract_features(filename):
    """
    This function does 3 simple things:
    - open the song file
    - get artist ID and put it
    - close the file
    """
    global cntnan	
    global listfeatures

    cf = []
    h5 = GETTERS.open_h5_file_read(filename)
    title = GETTERS.get_title(h5)
    if title not in listtitle:
       h5.close()
       return
    else:
      

    h5.close()



print 'number of song files:',apply_to_all_files(msd_subset_data_path, func=func_to_extract_features)
print len(listtitle)
pickle.dump(listtitle, open("gold_title.p","wb"))

