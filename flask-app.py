#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from datascience import * 
from flask import Flask


# In[10]:


app = Flask(__name__)

def match_sanger_to_eblocks(sanger_sequences, eblock_sequences):
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
    pass

@app.route('/')
def index():
    return render_template('index.html')  # Create an HTML file for the form

@app.route('/process', methods=['POST'])
def process():
    file_path1 = request.form['file_path1']
    file_path2 = request.form['file_path2']

    try:
        sanger = Table.read_table(file_path1)
        eblocks = Table.read_table(file_path2)
    except FileNotFoundError:
        return "File not found. Please check the file paths."

    output = match_sanger_to_eblocks(sanger, eblocks)
    csv_file_path = "matched.csv"
    output.to_csv(csv_file_path)

    return render_template('result.html', result=output.to_html())  # Create an HTML file for the result

if __name__ == '__main__':
    app.run(debug=True)

