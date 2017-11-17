#!/usr/bin/env python

##############################################
# AssemblyMetrics.py
# Author:
# Ali Foroozani 
# (alireza.foroozani@durham.dur.ac.uk)
# Last edited:
# (26/4/2016)
#

'''
This script prints out the following metrics for a FASTA file to standard output:
    * total length (Mbp)
    * number of contigs
    * N50
    * smallest contig length (bp)
    * longest contig length (bp)
    * average contig length (bp)
    * median contig length (bp)
    
Requires:
    * biopython
    * numpy
    * Linux or Mac OS
    
Usage:

   python path_to/AssemblyMetrics.py <assembly.fa>
    

This script can be made into an executable so python doesn't need to be called:
 
   chmod +x AssemblyMetrics.py
    
'''


#Import modules and set argv
#############################

import sys
from Bio import SeqIO
import numpy

FASTA=sys.argv[1]

print("\nCalculating assembly metrics for %s...\n" % (FASTA.split("/")[-1]))


#Parse the .fa file
####################

assemblyFA=SeqIO.parse(open(FASTA), 'fasta')

seqs=[]
for seq in assemblyFA:
    seqs.append(len(seq))


#Calculate metrics
###################

#length
totLength = sum(seqs)/1000000.0

#no. contigs
noContigs = len(seqs)

#smallest contig
minLength = min(seqs)

#longest contig
maxLength = max(seqs)

#average contig length
avgLength = numpy.average(seqs)
avgLength = numpy.around(avgLength, decimals=2)

#median contig length
medLength = int(numpy.median(seqs))

#N50
len50 = sum(seqs)/2

seqsSort = sorted(seqs)

accumulator=[]
x=0
for seq in seqsSort:
    accumulator.append(seq)
    x = sum(accumulator)
    if x >= len50:
        N50=seq
        break
    else: continue


#Report metrics
################

print("total length of assembly:    %s Mbp" % (totLength))
print("number of contigs:           %s\n" % (noContigs))
print("smallest contig length:      %s bp" % (minLength))
print("longest contig length:       %s bp" % (maxLength))
print("average contig length:       %s bp" % (avgLength))
print("median contig length:        %s bp\n" % (medLength))
print("assembly N50:                %s\n\n" % (N50))
print("\n")


