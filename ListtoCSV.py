from csv_io import *
from collections import *

def list_to_csv(L):
	strlist = str(L).translate(None, '[]')
	return strlist
