#!/usr/bin/env python 

###############################
#renameFASTAheaders.py
#Reza Foroozani
#(alireza.foroozani@durham.ac.uk)
#Last edited:
#(11/12/2017)
#


'''
This script renames the sequence headers in a FASTA file to a user defined string,
and appends a sequence/contig number to the header with leading zeros.

        i.e.        Headers in the input file...
        
                >ATCG00500.1 pacid=19637947 polypeptide=ATCG00500.1 locus=ATCG00500 ID=ATCG00500.1.TAIR10 annot-version=TAIR10
                ATGGAAAAATCGTGGTTCAATTTTATGTTTTCTAAGGGAGAATTGGAATACAGAGGTGAGCTAAGTAAAGCAATGGATAG
                TTTTGCTCCTGGTGAAAAGACTACTATAAGTCAAGACCGTTTTATATATGATATGGATAAAAACTTTTATGGTTGGGATG
                ...


                    ...can be changed to the following in the output file using the header_string 'AthalianaCDS_sequence':
                                            
                >AthalianaCDS_sequence000001
                ATGGAAAAATCGTGGTTCAATTTTATGTTTTCTAAGGGAGAATTGGAATACAGAGGTGAGCTAAGTAAAGCAATGGATAG
                TTTTGCTCCTGGTGAAAAGACTACTATAAGTCAAGACCGTTTTATATATGATATGGATAAAAACTTTTATGGTTGGGATG
                ...
                
                
Usage:
        python renameFASTAheaders.py \
            -i <input_FASTA_file.fa> \
            -o <outfile_.fa> \
            -s <header_string>
                
                
'''

#Set env
#########

import os
from optparse import OptionParser
import time


parser=OptionParser()
parser.add_option("-i", "--infile", dest="i")
parser.add_option("-o", "--outfile", dest="o")
parser.add_option("-s", "--string", dest="s")
(options, args) = parser.parse_args()

infile=options.i
outfile=options.o
headerPrefix=options.s


def Update(str):
    Time=time.strftime("%d/%m/%Y %H:%M")
    str+='%s'
    print(str % (Time))


#Rename headers
################

infile=open(infile).readlines()

with open(outfile, 'w') as output:
    N=0
    for line in infile:
        if line[0]=='>':
            N+=1
    N=len(str(N))
    n=1
    for line in infile:
        if line[0]=='>':
            newHeader='>%s%s\n' % (headerPrefix, str(n).zfill(N))
            n+=1
            output.write(newHeader)
        else:
            output.write(line)




