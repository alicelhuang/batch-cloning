#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from datascience import * 


# In[18]:


# The 'match_sanger_to_eblocks' function takes two arguments -
#     sanger_sequences: a TABLE with column "Sanger Sequences" + any other columns with useful info (MiniPrep Number, Date)
#     eblock_sequences: a TABLE with columns "Name" and "Eblock Sequences".
# It returns a new table with all the information from the original Sanger Sequencing table and adds a new column,
# "Eblock Matches," which lists the name of the Eblock that each sequencing result matches.

### NOTE: Make sure that the columns are labeled exactly as described above!

# Get file paths from the user
file_path1 = input("Enter the path for the Sanger Sequences CSV file: ")
file_path2 = input("Enter the path for the Eblock Sequences CSV file: ")

try:
    sanger = Table.read_table(file_path1)
    eblocks = Table.read_table(file_path2)
except FileNotFoundError:
    print("File not found. Please check the file paths.")
    exit()

def match_sanger_to_eblocks (sanger_sequences, eblock_sequences):
    num_eblocks = eblock_sequences.num_rows
    num_sangers = sanger_sequences.num_rows
  
    all_matches = make_array()
    for sanger in np.arange(num_sangers):
        matches = str()
        for eblock in np.arange(num_eblocks):
            if eblocks.column('Eblock Sequence').item(eblock).lower() in sanger_sequences.column('Sanger Sequence').item(sanger).lower():
                matches = matches + eblocks.column('Name').item(eblock)
            else:
                continue

        all_matches = np.append(all_matches, matches)

    matched_table = sanger_sequences.with_column('Eblock Matches', all_matches)
    return matched_table

output = match_sanger_to_eblocks(sanger, eblocks)
output.show()


# In[ ]:


# Specify the file path
csv_file_path = "EJ-matched-01.csv"

# Writing DataFrame to CSV file using pandas
output.to_csv(csv_file_path)


# In[ ]:




