#!/usr/bin/env python 

######################################
#Uracil~Thymine_Converter.py
#Author:
#Alireza Foroozani
#(alireza.foroozani@durham.ac.uk)
#Last edited:
#(19/11/2017)
#

'''

This script converts RNA to DNA by changing all the uracils (U/u)
in the sequences of a FASTA file to thymines (T/t), and vice versa.

Usage:
    
    python Uracil~Thymine_Converter.py \
        -i input.fa \
        -o output.fa \
        -c D

Options:
    
    -i      PATH to location of input fasta file
    -o      PATH to desired location of output fasta file
    -c      Nucleic acid to be converted to:
                for RNA (uracil) to DNA (thymine):
                    -c D
                for DNA to RNA:
                    -c R


You can make Uracil~Thymine_Converter.py into an executable to avoid calling python:

    chmod +x Uracil~Thymine_Converter.py

'''


#Set environment
#################

import os
import subprocess
from optparse import OptionParser
import time


parser=OptionParser()
parser.add_option("-i", "--indir", dest="i")
parser.add_option("-o", "--outdir", dest="o")
parser.add_option("-c", "--conversion", dest="c")
(options, args) = parser.parse_args()


fasta = options.i
outfile = options.o
nuclA = options.c


#Convert nucleic acid
######################

fasta = open(fasta).readlines()

if nuclA=='D' or nuclA=='d':
    with open(outfile, 'w') as output:
        for line in fasta:
            if line[0]=='>': output.write(line)
            else:
                lineList = list(line)
                for n,i in enumerate(lineList):
                    if i=='U':
                        lineList[n]='T'
                    elif i=='u':
                        lineList[n]='t'
                output.write(''.join(lineList))
elif nuclA=='R' or nuclA=='r':
    with open(outfile, 'w') as output:
        for line in fasta:
            if line[0]=='>': output.write(line)
            else:
                lineList = list(line)
                for n,i in enumerate(lineList):
                    if i=='T':
                        lineList[n]='U'
                    elif i=='t':
                        lineList[n]='u'
                output.write(''.join(lineList))











