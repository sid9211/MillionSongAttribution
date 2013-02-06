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
import pickle

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
mydict ={}

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

    #FEATURE 0
    song_hotness = GETTERS.get_song_hotttnesss(h5)
    if math.isnan(song_hotness):
       nanfound = 1
       cntnan = cntnan + 1
    else:
       cf.append(song_hotness)

    #FEATURE 1
    #Get song loudness
    song_loudness = GETTERS.get_loudness(h5)
    
    if math.isnan(song_loudness):
       nanfound = 1
       cntnan = cntnan + 1
    else:
       cf.append(song_loudness)

    #FEATURE 2
    #Get key of the song
    song_key = GETTERS.get_key(h5)
    if math.isnan(song_key):
       nanfound = 1
       cntnan = cntnan + 1
    else:
       cf.append(song_key)

    #FEATURE 3
    #Get duration of the song
    song_duration = GETTERS.get_duration(h5)
    if math.isnan(song_duration):
       nanfound = 1
       cntnan = cntnan + 1
    else:
       cf.append(song_duration)

    #FEATURE 4-15
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

    #FEATURE 16, 27
    #Get Average Timbre Class across all segments
    timbres = GETTERS.get_segments_timbre(h5)
    M = np.mat(timbres)
    meantimbres = M.mean(axis=0)
    timbre_arr = np.asarray(meantimbres)
    timbre_list = []
    for i in range(0,12):
	timbre_list.append(timbre_arr[0][i])

    cf.append(timbre_list)

    #FEATURE 28 
    #Get song year
    song_year = GETTERS.get_year(h5)
    if song_year == 0:
       nanfound = 1
       cntnan = cntnan + 1
    else:
      cf.append(song_year)

    #FEATURE 29 
    #Get song tempo
    song_tempo = GETTERS.get_tempo(h5)
    cf.append(song_tempo)

    #Feature 30
    #Get max loudness for each segment
    max_loudness_arr = GETTERS.get_segments_loudness_max(h5)
    start_loudness_arr = GETTERS.get_segments_loudness_start(h5)
    if nanfound == 0:
       cf.append(max(max_loudness_arr)-min(start_loudness_arr))

    #Feature 31
    artist_familiarity = GETTERS.get_artist_familiarity(h5)
    cf.append(artist_familiarity)

    #Feature 32
    song_title = GETTERS.get_title(h5)
    cf.append(song_title)

    #Featture 33
    artist_name = GETTERS.get_artist_name(h5)
    cf.append(artist_name)

    #Feature 34
    #location = GETTERS.get_artist_location(h5)
    #cf.append(location)

    #Tags
    artist_mbtags = GETTERS.get_artist_mbtags(h5)
    if not artist_mbtags.size:
       genre = "Unknown"
    else:
       artist_mbcount = np.array(GETTERS.get_artist_mbtags_count(h5))
       index_max = artist_mbcount.argmax(axis=0)
       genre = artist_mbtags[index_max]
       if genre == 'espa\xc3\xb1ol':
	  genre = "Unknown"

       cf.append(genre)

    if nanfound == 0:
       strlist = list_to_csv(cf)
       listfeatures.append(strlist)
       mydict.setdefault(genre,[]).append(song_hotness)
    h5.close()



print 'number of song files:',apply_to_all_files(msd_subset_data_path, func=func_to_extract_features)
pickle.dump(mydict, open("genre_hotness.p","wb"))


