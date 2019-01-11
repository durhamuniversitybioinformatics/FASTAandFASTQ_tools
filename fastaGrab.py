#!/usr/bin/env python

######################################
#fastaGrab.py
#Author:
#Ali Foroozani
#(alireza.foroozani@durham.ac.uk)
#Last edited:
#(Feb 2016)
#

'''
This script extracts wanted sequences from a FASTA file by contig name.

The input must be a file containing a list of contig names:
        e.g.
                ATCG00040.1
                ATCG00130.1
                ATCG00170.1

Requires:
        * biopython

Usage:
        python fastaGrab.py -s <sequences_file.fa> -w <wanted_sequences.txt> -o <output_file.fa>
'''


#Import modules and set variables
##################################

from optparse import OptionParser
from Bio import SeqIO

parser=OptionParser()
parser.add_option("-s", "--sequences", dest="s")
parser.add_option("-w", "--wanted", dest="w")
parser.add_option("-o", "--output", dest="o")
(options, args) = parser.parse_args()

fasta_file = options.s
wanted_file = options.w
result_file = options.o


#Parse the wanted.txt file for headers
#######################################

wanted = set()
with open(wanted_file) as f:
    for line in f:
        line = line.strip()
        if line !="":
            wanted.add(line)

#Extract wanted seqs from .fa and write to new file
####################################################

fasta_sequences = SeqIO.parse(open(fasta_file), 'fasta')
with open(result_file, "w") as f:
    for seq in fasta_sequences:
        if seq.id in wanted:
            SeqIO.write(seq, f, "fasta")







