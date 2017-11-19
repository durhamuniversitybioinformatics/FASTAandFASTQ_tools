FASTAandFASTQ_tools

---
AssemblyMetrics.py
   This script calculates numerous metrics of an assembly (FASTA file)
      Requires:
         * biopython
         * numpy
      Usage:
         python path_to/AssemblyMetrics.py <path_to/assembly.fa>
---
fastaGrab.py
   This script extracts wanted sequences from a FASTA file using a list of contig names.
      Requires:
         *biopython
      Usage:
         python fastGrab.py \
            -s sequences_file.fa \
            -w wanted_sequences_list.txt \
            -o output_file.fa
---
Uracil~Thymine_Converter.py
     This script converts all uracil (U/u) bases to thymines (T/t), or vice versa, for a FASTA file.
       Usage:
         python Uracil~Thymine_Converter.py \
            -i input.fa \
            -o output.fa \
            -c D                       # 'D' for RNA-->DNA, 'R' for DNA-->RNA
---


-------------------------------------------------------------------------------------------
System Requirements

To install python modules (e.g. biopython/numpy):
   By far the easiest way, if you have sudo privileges, is to use pip: 
      e.g.  sudo pip install biopython
   Otherwise, contact a system administrator to install into a loadable python module:
      e.g.  module load python/2.7.9
