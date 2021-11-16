
"""
Program: checkpdbformutation_lib
File:    checkpdbformutation_lib.py

Version: V1.0
Date: 26.10.2021
Function:   Library: functions used for checkpdbformutation which identifies 
            differences, and if there are any, between protein sequences in 
            FASTA format files (from SwissProt and PDB)

Author: Barbara A. Mikucka

--------------------------------------------------------------------------
Description:
The program takes 2 protein sequence FASTA format files and returns whether 
the shorter (PDB sequence) is contained in the longer (SwissProt sequence). 
If the sequences are different the program identifies the mismatches.

--------------------------------------------------------------------------
Usage:
======
checkpdbmutation pdb_file sprot_file test.faa test1.faa test2.faa

--------------------------------------------------------------------------
Revision history:
=================
V1.0  26.10.21    Original    By: BAM
"""

#*************************************************************************
# Import libraries

import sys

#*************************************************************************
def read_file(filename):
   """Read input files without first row, delete breaks and return as 
   uppercase string

   Input:   filename    --- FASTA format sequence file 
   Return: file_edited  --- string with uppercase amino acid sequence 

   26.10.21    Original    By: BAM

   >>> read_file("test/test.faa")
   'HELLOWORLD'
   >>> read_file("test/test2.faa")
   'AAHETTOWORLDZZ'
   >>>

   """
   with open(filename) as file:
      #read all but first line
      rows = file.readlines()[1:]   
      #make into string
      file_edited = ''.join(rows) 
      #get rid of breaks
      file_edited = file_edited.replace('\n', '') 
      #make all letters uppercase
      file_edited = file_edited.upper()   
      return file_edited 


#*************************************************************************
def fasta_files_match (pdb_file, sprot_file):
   """Compare 2 sequences to identity whether the PDB sequence in the 
   pdb_file is contained within the swiss prot sequence in the sprot_file

   Input:   pdb_file    --- FASTA file of PDB amino acid sequence
            sprot_file  --- FASTA file of Swiss Prot amino acid sequence
   Return:  Boolean     --- True if the PDB sequence is in the Swiss prot 
                     sequence, otherwise False.

   26.10.21    Original    By: BAM

   >>> fasta_files_match ("test/test1.faa", "test/test.faa")
   No mutations identified in PDB sequence
   True
   >>> fasta_files_match ("test/test.faa", "test/test2.faa")
   False
   >>> 

   """

   #read and edit the two sequence files to make pdbseq and sprotseq 
   #(contain the sequence as a string only)
   sprotseq = read_file(sprot_file)
   pdbseq = read_file(pdb_file)
   #return True if pdbseq is contained within sprotseq
   if pdbseq in sprotseq:
      return True
   else: 
      return False


#*************************************************************************
def identify_short_sequence (pdb_file, sprot_file):
   """Identify the shorter and longer sequence between the amino acid 
   sequence in the PDB and Swiss Prot files

   Input:   pdb_file    --- FASTA file of PDB amino acid sequence
         sprot_file  --- FASTA file of Swiss Prot amino acid sequence
   Return: long_seq  --- amino acid sequence of the longer sequence 
         short_seq   --- amino acid sequence of the shorter sequence 
   

   26.10.21    Original    By: BAM

   >>> identify_short_sequence ("test/test.faa", "test/test2.faa")
   ('AAHETTOWORLDZZ', 'HELLOWORLD', 1)
   >>> identify_short_sequence ("test/test2.faa", "test/test.faa")
   ('AAHETTOWORLDZZ', 'HELLOWORLD', 0)
   >>> 

   """

   #read and edit files to make string of only amino acid sequences
   pdbseq = read_file(pdb_file)
   sprotseq = read_file(sprot_file)
   #check which sequence is longer
   
   if len(pdbseq) < len(sprotseq):
      long_seq = sprotseq
      short_seq = pdbseq
      a = 1
      #'a' is used to later correclty identify the shorter and longer sequences
      #as either PDB or Swiss Prot sequences.
   elif len(pdbseq) == len(sprotseq):
      long_seq = sprotseq
      short_seq = pdbseq
      a = 0
   else:
      short_seq = sprotseq
      long_seq = pdbseq
      a = 0
   #return tuple that includes the long_seq and short_seq
   return long_seq, short_seq, a



#*************************************************************************
def get_number_of_matches (sprot_file, pdb_file, offset): 
   """Returns number of amino acid matches between two input sequences 
   with the longer sequence at defined offset

   Input:   pdb_file          --- FASTA file of PDB amino acid sequence
            sprot_file        --- FASTA file of Swiss Prot amino acid sequence
            offset            --- integer by which the longer and shorter 
                                  sequence are offset for comparison 
   Return:  number_of_matches --- integer, number of matches between two sequences
   

   26.10.21    Original    By: BAM

   >>> get_number_of_matches ("test/test2.faa", "test/test.faa", 1)
   0
   >>> get_number_of_matches ("test/test2.faa", "test/test.faa", 2)
   8
   >>> get_number_of_matches ("test/test2.faa", "test/test.faa", 3)
   0
   >>> 
   """

   #use the identify_short_sequence function to read and edit files and 
   #identify the shorter and longer sequence
   (long_seq, short_seq, a) = identify_short_sequence(sprot_file, pdb_file)  
   #check matches for all positions along shorter sequence
   positions = range(len(short_seq))
   number_of_matches = 0
   
   for x in positions:
      #check if letters being compared are within the length of the sequence
      #match of letter in short sequence and the letter in the longer sequence at an offset
      if ((x + offset < len(long_seq)) and 
         (long_seq[x + offset] == short_seq[x])):
         #increase number of matches for each match of S position to L position+offset
         number_of_matches = number_of_matches + 1       
   return number_of_matches


#*************************************************************************
def check_all_offsets (sprot_file, pdb_file):
   """Returns a tuple of total matches between two sequences and the 
   offset value that results in this best match number

   Input:   pdb_file                --- FASTA file of PDB amino acid sequence
            sprot_file              --- FASTA file of Swiss Prot amino acid sequence
   Return:  best_number_of_matches  --- number of matches between two sequences
            best_offset             --- offset value that gives the most matches 
                                       (best alignment of sequences)
      

   26.10.21    Original    By: BAM

   >>> check_all_offsets ("test/test2.faa", "test/test.faa")
   (8, 2)
   >>> check_all_offsets ("test/test1.faa", "test/test.faa")
   (5, 0)
   >>> 
   """

   #use identify_short_sequence to get short and long sequence between two sequences
   (long_seq, short_seq, a) = identify_short_sequence (sprot_file, pdb_file)
   best_number_of_matches = 0
   #possible offsets include all integers in range from 0 to the difference in length of the sequences
   offsets = range(len(long_seq) - len(short_seq))
   
   for x in offsets:
      #get number_of_matches using get_number_of_matches function and all possible offsets
      number_of_matches = get_number_of_matches (sprot_file, pdb_file, x)
      if number_of_matches > best_number_of_matches:
         #if the number of matches for this offset is better than 
         #for previous matches it becomes best_number_of_matches
         best_number_of_matches = number_of_matches
         best_offset = x
   return best_number_of_matches, best_offset


#*************************************************************************
def show_mismatches (sprot_file, pdb_file):
   """Print positions of all mismatches in the best alignment between 
   sequences sprotseq and pdbseq, with respect to positions in longer and 
   shorter sequence (position 1 is the fisrt amino acid in the sequence)

   Input:   pdb_file    --- FASTA file of PDB amino acid sequence
         sprot_file  --- FASTA file of Swiss Prot amino acid sequence

   26.10.21    Original    By: BAM

   >>> show_mismatches ("test/test2.faa", "test/test.faa")
   Mismatch at Swiss Prot position
   3
   L
   with PDB sequence position
   5
   T
   Mismatch at Swiss Prot position
   4
   L
   with PDB sequence position
   6
   T
   >>>
   >>> show_mismatches ("test/test2.faa", "test/test1.faa")
   Mismatch at Swiss Prot position
   3
   L
   with PDB sequence position
   5
   T
   Mismatch at Swiss Prot position
   4
   L
   with PDB sequence position
   6
   T
   >>> 

   """

   #use check_all_offsets to get best number of matches and best offset to use for this alignment
   (best_number_of_matches, best_offset) = check_all_offsets (sprot_file, pdb_file)
   #use identify)short_sequence to get the two sequences
   (long_seq, short_seq, a) = identify_short_sequence (sprot_file, pdb_file)
   #check all positions along the short sequence
   positions = range(len(short_seq))
   
   for x in positions:
      #check the positions being checked are in the sequence
      #if the letter is not the same 
      if ((x + best_offset < len(long_seq)) and
      (long_seq[x + best_offset] != short_seq[x])):
         #print the mismatches relative to short and long sequence position
         if a == 1:
            #for if the PDB sequence is the shorter sequence
            print ("Mismatch at PDB sequence position") 
            #1st position is the first letter (not like python with position 0 being first)
            print (x + 1) 
            print(short_seq[x])
            print ("with Swiss Prot sequence position")
            print (x + best_offset + 1) 
            print(long_seq[(x + best_offset)])
         elif a == 0: 
            #For if the Swiss Prot sequence is the shorter sequence
            print ("Mismatch at Swiss Prot position") 
            #1st position is the first letter (not like python with position 0 being first)
            print (x + 1) 
            print (short_seq[x])
            print ("with PDB sequence position")
            print (x + best_offset + 1) 
            print (long_seq[(x + best_offset)])




#*************************************************************************
def get_mutations (sprot_file, pdb_file):
   """Returns a list of all mismatches between the sequence in the Swiss Prot 
   file and PDB file, relative to the longer (Swiss Prot) sequence.

   Input:   pdb_file        --- FASTA file of PDB amino acid sequence
            sprot_file      --- FASTA file of Swiss Prot amino acid sequence
   Return:  all_mutations   --- list of residues mismatched between Swiss Prot 
                                 and PDB sequences relative to longer sequence
           
      

   02.11.21    Original    By: BAM

   >>> get_mutations ("test/test2.faa", "test/test.faa")
   [5, 6]
   >>> get_mutations ("test/test1.faa", "test/test.faa")
   []
   >>>
   """

   #use check_all_offsets to get best number of matches and best offset to use for this alignment
   (best_number_of_matches, best_offset) = check_all_offsets (sprot_file, pdb_file)
   #use identify_short_sequence to get the two sequences
   (long_seq, short_seq, a) = identify_short_sequence (sprot_file, pdb_file)
   #check all positions along the short sequence
   positions = range(len(short_seq))
   
   #make a list of mutations
   mutations = []

   for x in positions:
      #check the positions being checked are in the sequence
      #if the letter is not the same 
      if ((x + best_offset < len(long_seq)) and
      (long_seq[x + best_offset] != short_seq[x])):
         #add the positions that match this to a list
         mutations.append(x + 1 + best_offset)

   return mutations


   #*************************************************************************

if __name__ == "__main__":
   import doctest
   doctest.testmod()


