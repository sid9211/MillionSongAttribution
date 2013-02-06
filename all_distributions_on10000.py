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
cntdanceability = 0

listhotness = []
listyear = []
listloudness = []
listkey = []
listmode = []
listduration = []

# we define the function to apply to all files
def func_to_extract_features(filename):
    """
    This function does 3 simple things:
    - open the song file
    - get artist ID and put it
    - close the file
    """
    global cntnan	
    global cntdanceability
    global listfeatures

    global listhotness
    global listyear
    global listloudness
    global listkey
    global listmode
    global listduration 

    cf = []
    h5 = GETTERS.open_h5_file_read(filename)
    nanfound = 0

    #Get target feature: song hotness
    song_hotness = GETTERS.get_song_hotttnesss(h5)
    if math.isnan(song_hotness):
       nanfound = 1
       cntnan = cntnan + 1
    else:
       cf.append(song_hotness)

    #Get danceablity
#    song_danceability = GETTERS.get_danceability(h5)
    
#    if song_danceability == 0:
#       nanfound = 1
#       cntnan = cntnan + 1
#    else:
#       cf.append(song_danceability)

    #Get song loudness
    song_loudness = GETTERS.get_loudness(h5)
    
    if math.isnan(song_loudness):
       nanfound = 1
       cntnan = cntnan + 1
    else:
       cf.append(song_loudness)

    #Get song energy 
#    song_energy = GETTERS.get_energy(h5)
    
#    if song_energy == 0:
#       nanfound = 1
#       cntnan = cntnan + 1
#    else:
#       cf.append(song_energy)

    #Get key of the song
    song_key = GETTERS.get_key(h5)
    if math.isnan(song_key):
       nanfound = 1
       cntnan = cntnan + 1
    else:
       cf.append(song_key)

    #Get mode of the song
    song_mode = GETTERS.get_mode(h5)
    if math.isnan(song_mode):
       nanfound = 1
       cntnan = cntnan + 1
    elif song_mode == 0:
       nanfound = 1
       cntnan = cntnan + 1
    else:
       cf.append(song_mode)

    #Get duration of the song
    song_duration = GETTERS.get_duration(h5)
    if math.isnan(song_duration):
       nanfound = 1
       cntnan = cntnan + 1
    else:
       cf.append(song_duration)

    #Get Average Pitch Class across all segments
    #Get the pitches (12 pitches histogram for each segment)
    pitches = GETTERS.get_segments_pitches(h5)
    M = np.mat(pitches)
    meanpitches = M.mean(axis=0)
    pitches_arr = np.asarray(meanpitches)
    pitches_list = []
    for i in range(0,12):
	pitches_list.append(pitches_arr[0][i])

    cf.append(pitches_list)

    #Get Average Timbre Class across all segments
    timbres = GETTERS.get_segments_timbre(h5)
    M = np.mat(timbres)
    meantimbres = M.mean(axis=0)
    timbre_arr = np.asarray(meantimbres)
    timbre_list = []
    for i in range(0,12):
	timbre_list.append(timbre_arr[0][i])

    cf.append(timbre_list)

    #Get song year
    song_year = GETTERS.get_year(h5)
    if song_year == 0:
       nanfound = 1
       cntnan = cntnan + 1
    else:
      cf.append(song_year)

    if nanfound == 0:
       strlist = list_to_csv(cf)
       print strlist
       listfeatures.append(strlist)

       listhotness.append(song_hotness)
       listloudness.append(song_loudness)
       listkey.append(song_key)
       listmode.append(song_mode)
       listduration.append(song_duration)
       listyear.append(song_year)

    h5.close()



print 'number of song files:',apply_to_all_files(msd_subset_data_path, func=func_to_extract_features)
print 'Number of songs which dont have hotness is:', cntnan, cntdanceability

plt.figure(1)
plt.hist(listhotness)
plt.xlabel('Hotness range')
plt.ylabel('Number of songs')
plt.title('Histogram of Hotness')

plt.figure(2)
plt.hist(listloudness)
plt.xlabel('Loudness range')
plt.ylabel('Number of songs')
plt.title('Histogram of Loudness')

plt.figure(3)
plt.hist(listkey)
plt.xlabel('Key range')
plt.ylabel('Number of songs')
plt.title('Histogram of Key')

plt.figure(4)
plt.hist(listmode)
plt.xlabel('Mode range')
plt.ylabel('Number of songs')
plt.title('Histogram of Mode')

plt.figure(5)
plt.hist(listduration)
plt.xlabel('Duration range')
plt.ylabel('Number of songs')
plt.title('Histogram of Duration')

plt.figure(6)
plt.hist(listyear)
plt.xlabel('Year range')
plt.ylabel('Number of songs')
plt.title('Histogram of Year')

plt.show()
