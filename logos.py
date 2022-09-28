import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.ion()
import logomaker as lm
from Bio import AlignIO
#import argparse


#parser = argparse.ArgumentParser()
#parser.add_argument("-r", dest="reads", required=True, type=str, help="input file")
#parser.add_argument("-o", dest="out", required=True, type=str, help="output file")
#args = parser.parse_args()

#with open(args.reads, "r") as f:
#    lines = f.readlines()

with open("file_name.fasta", "r") as f:
    lines = f.readlines()
#print(''.join(lines[:20]))

seqs = [seq.strip().upper() for seq in lines if ('#' not in seq) and ('>') not in seq]
print('There are %d sequences, all of length %d'%(len(seqs), len(seqs[0])))


ww_counts_df = lm.alignment_to_matrix(sequences=seqs, to_type='counts', characters_to_ignore='.-X')
logo=lm.Logo(ww_counts_df)

plt.savefig('David_la_mas_perra.pdf')
plt.show()

# ww_counts_df = lm.alignment_to_matrix(sequences=seqs, to_type='counts', characters_to_ignore='.-X')
# fig, ax = plt.subplots(1,1,figsize=[10,15]) #Plot axis frame


# logo=lm.Logo(ww_counts_df,shade_below=.5,fade_below=.5,color_scheme='weblogo_protein',
#                         #fade_probabilities=True,
#                         ax= ax, #Call the axis
#                         width=.8, 
#                         vpad=.05)
#                         #stack_order='small_on_top')#Uncomment for inverse stack
# logo.style_spines(spines=['left', 'right'], visible=False) #Get rid of the side lines
# ax.set_xticks([])# Get rid of axis thicks
# ax.set_yticks([])
# #logo.ax.set_xlim([-1, len(ww_counts_df)]) #Modify lenght of axis
