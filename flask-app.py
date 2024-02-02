#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from datascience import * 
from flask import Flask, render_template, request


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
    return render_template('upload_form.html')  # Create an HTML file for the form

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_sanger_file = request.files['sanger_file']
    uploaded_eblocks_file = request.files['eblocks_file']

    try:
        sanger = Table.read_table(uploaded_sanger_file)
        eblocks = Table.read_table(uploaded_eblocks_file)
    except FileNotFoundError:
        return "File not found."

    output = match_sanger_to_eblocks(sanger, eblocks)
    csv_file_path = "matched.csv"
    output.to_csv(csv_file_path)

    return render_template('result.html', result=output.to_html())  # Create an HTML file for the result

if __name__ == '__main__':
    app.run(debug=True)

