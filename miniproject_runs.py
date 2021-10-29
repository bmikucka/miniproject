#to run: python3 miniproject.py P11413.faa PDB5ukw_nomutant.faa
"""
Program:  miniproject_read
File:     miniproject_readpy

Version: V1.0
Date: 29.10.2021
Function: Identify differences, and if there are any, between protein 
sequences in FASTA format files (from SwissProt and PDB)

Author: Barbara A. Mikucka

--------------------------------------------------------------------------
Description:
The program takes 2 protein sequence FASTA format files and returns whether 
the shorter (PDB sequence) is contained in the longer (SwissProt sequence). 
If the sequences are different the program identifies the mismatches.

--------------------------------------------------------------------------
Usage:
======
miniproject file1 file2 

--------------------------------------------------------------------------
Revision history:
=================
V1.0  29.10.21    Original    By: BAM
"""

#*************************************************************************
# Import libraries

import sys

from miniproject import (read_file, if_sequences_match, define_lengths, 
   get_matches, check_all_offsets, show_mismatches)


#*************************************************************************

#get files from command line
#[0] is this file
#1 and 2 - FASTA sequence files
sprot_file = sys.argv[1]
pdb_file = sys.argv[2]

if len(sys.argv) == 3:
   #check if the sequences match
   if if_sequences_match (sprot_file, pdb_file):
      print ("No mutations have been identified")
      #DOES NOT WORK
   else:
      #if mutations present prints the differences
      show_mismatches (sprot_file, pdb_file)
    #THIS PART WORKS
elif len(sys.argv) == 4:
   #4th optional character - the residue of interest
   residue_check = sys.argv[3]
   mutations =
   for x in mutations:
      if residue_check == x:
         print ("The residue of interest is mutated in the sequence provided.")
      else:
         print ("The residue of interest is NOT mutated in the sequence provided.")





   

