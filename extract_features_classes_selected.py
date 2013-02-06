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

from csv_io import *
from ListtoCSV import *
import  matplotlib.pyplot as plt

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
    nanfound = 0

    #Get target feature: song hotness

    #FEATURE 0
    song_hotness = GETTERS.get_song_hotttnesss(h5)
    if math.isnan(song_hotness):
       nanfound = 1
       cntnan = cntnan + 1
    else:
       if song_hotness <= 0.2:
          song_hotness_class = 0
       elif song_hotness <= 0.4:
          song_hotness_class = 1
       elif song_hotness <= 0.6:
          song_hotness_class = 2
       elif song_hotness <= 0.8:
          song_hotness_class = 3
       else:
          song_hotness_class = 4

       cf.append(song_hotness_class)

    #FEATURE 1
    #Get song loudness
    song_loudness = GETTERS.get_loudness(h5)
    
    if math.isnan(song_loudness):
       nanfound = 1
       cntnan = cntnan + 1
    else:
       cf.append(song_loudness)

    #FEATURE 2 
    #Get song year
    song_year = GETTERS.get_year(h5)
    if song_year == 0:
       nanfound = 1
       cntnan = cntnan + 1
    else:
      cf.append(song_year)

    #FEATURE 3
    #Get song tempo
    song_tempo = GETTERS.get_tempo(h5)
    cf.append(song_tempo)

    #Feature 4 
    #Artist familarity
    artist_familiarity = GETTERS.get_artist_familiarity(h5)
    cf.append(artist_familiarity)

    #Feature 5 
    artist_hotness = GETTERS.get_artist_hotttnesss(h5)
    if math.isnan(artist_hotness):
       nanfound = 1
       cntnan = cntnan + 1
    else:
       cf.append(artist_hotness)

    if nanfound == 0:
       strlist = list_to_csv(cf)
       listfeatures.append(strlist)

    h5.close()



print 'number of song files:',apply_to_all_files(msd_subset_data_path, func=func_to_extract_features)
filename = 'hotness_features_classes_selected.csv'
write_delimited_file(filename, listfeatures)
