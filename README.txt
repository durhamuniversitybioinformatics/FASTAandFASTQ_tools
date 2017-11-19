FASTAandFASTQ_tools

---
AssemblyMetrics.py
   This script calculates numerous metrics of an assembly (FASTA file)
      Requires:
         * Linux or Mac OS
         * biopython
         * numpy
      Usage:
         python path_to/AssemblyMetrics.py <path_to/assembly.fa>
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
