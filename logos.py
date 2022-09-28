import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.ion()
import logomaker as lm
from Bio import AlignIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", dest="reads", required=True, type=str, help="reads file")
parser.add_argument("-o", dest="out", required=True, type=str, help="output files")
args = parser.parse_args()

with open(args.reads, "r") as f:
    lines = f.readlines()

#print(''.join(lines[:20]))

seqs = [seq.strip().upper() for seq in lines if ('#' not in seq) and ('>') not in seq]
print('There are %d sequences, all of length %d'%(len(seqs), len(seqs[0])))


ww_counts_df = lm.alignment_to_matrix(sequences=seqs, to_type='counts', characters_to_ignore='.-X')
logo=lm.Logo(ww_counts_df)

plt.savefig('David_la_mas_perra.pdf')
plt.show()
