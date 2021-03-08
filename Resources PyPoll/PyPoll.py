import os 
import csv 
import collections
from collections import Counter 

voters_candidates = []
votes_per_candidate = []

election_data_csv_path = os.path.join("Resources","election_data.csv")

#next step needs to be like pybank, open csv to read
with open(election_data_csv_path, newline="") as csvfile: 
