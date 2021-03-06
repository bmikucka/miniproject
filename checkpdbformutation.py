#to run: python3 checkpdbformutation.py test/P11413.faa test/PDB5ukw_nomutant.faa
"""
Program:  checkpdbformuation
File:     checkpdbformutation.py

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
checkpdbformutation file1 file2 

--------------------------------------------------------------------------
Revision history:
=================
V1.0  29.10.21    Original    By: BAM
"""

#*************************************************************************
# Import libraries

import sys

from checkpdbformutation_lib import (read_file, fasta_files_match, identify_short_sequence, 
   get_number_of_matches, check_all_offsets, show_mismatches, get_mutations)


#*************************************************************************

#get files from command line
#[0] is this file
#1 and 2 - FASTA sequence files
sprot_file = sys.argv[1]
pdb_file = sys.argv[2]


#if no specific residue to check
if len(sys.argv) >= 3:
   #check if the sequences match
   if fasta_files_match (pdb_file, sprot_file):
      print ("No mutations have been identified")

   else:
      #if mutations present prints the differences
      show_mismatches (sprot_file, pdb_file)

      #if have a specific residue to check
      if len(sys.argv) == 4:
         mutated_residue = int(sys.argv[3])
         #get list of mutated residues relative to Swiss Prot (longer) sequence
         mutations = get_mutations (sprot_file, pdb_file)
      
         #check if the residue of interest is mutated
         if (mutated_residue in mutations):
            print ("The residue of interest is mutated in the sequence provided.")
         elif (mutated_residue not in mutations): 
            print ("The residue of interest is NOT mutated in the sequence provided.")


            



         


