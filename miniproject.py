#to run: python3 miniproject.py P11413.faa PDB5ukw_nomutant.faa

"""
Program: miniproject
File: 	 miniproject.py

Version: V1.0
Date: 26.10.2021
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
V1.0 	26.10.21 	Original 	By: BAM
"""

#*************************************************************************
# Import libraries

import sys

#*************************************************************************
def read_file(filename):
	"""Read input files without first row, delete breaks and return as 
	uppercase string

	Input: 	filename 		--- FASTA format sequence file 
	Return: file_edited 	--- string with uppercase amino acid sequence 

	26.10.21 	Original 	By: BAM

	>>> read_file("test.faa")
	'HELLOWORLD'
	>>> read_file("test2.faa")
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

if __name__ == "__main__":
   import doctest
   doctest.testmod()


#*************************************************************************
def compare_seqs (pdb_file, sprot_file):
	"""Compare 2 sequences to identity whether the PDB sequence in the 
	pdb_file is contained within the swiss prot sequence in the sprot_file

	Input: 	pdb_file 	--- FASTA file of PDB amino acid sequence
			sprot_file	--- FASTA file of Swiss Prot amino acid sequence
	Return: Boolean 	--- True if the PDB sequence is in the Swiss prot 
							sequence, otherwise False.

	26.10.21 	Original 	By: BAM

	>>> compare_seqs("test1.faa", "test.faa")
	True
	>>> compare_seqs("test.faa", "test2.faa")
	False	
	>>> 

	"""

	#(read and edit the two sequence files to make pdbseq and sprotseq 
	#(contain the sequence as a string only)
	sprotseq = read_file(sprot_file)
	pdbseq = read_file(pdb_file)
	#return True if pdbseq is contained within sprotseq
	return True if pdbseq in sprotseq else False

if __name__ == "__main__":
   import doctest
   doctest.testmod()


#*************************************************************************
def define_lengths (pdb_file, sprot_file):
	"""Identify the shorter and longer sequence between the amino acid 
	sequence in the PDB and Swiss Prot files

	Input: 	pdb_file 	--- FASTA file of PDB amino acid sequence
			sprot_file	--- FASTA file of Swiss Prot amino acid sequence
	Return: long_seq 	--- amino acid sequence of the longer sequence 
			short_seq 	--- amino acid sequence of the shorter sequence 
	

	26.10.21 	Original 	By: BAM

	>>> define_lengths ("test.faa", "test2.faa")
	('AAHETTOWORLDZZ', 'HELLOWORLD')
	>>> define_lengths ("test2.faa", "test.faa")
	('AAHETTOWORLDZZ', 'HELLOWORLD')
	>>> 

	"""

	#read and edit files to make string of only amino acid sequences
	pdbseq = read_file(pdb_file)
	sprotseq = read_file(sprot_file)
	#check which sequence is longer
	
	if len(pdbseq) < len(sprotseq):
		long_seq = sprotseq
		short_seq = pdbseq
	elif len(pdbseq) == len(sprotseq):
		long_seq = sprotseq
		short_seq = pdbseq
	else:
		short_seq = sprotseq
		long_seq = pdbseq
	#return tuple that includes the long_seq and short_seq
	return long_seq, short_seq

if __name__ == "__main__":
   import doctest
   doctest.testmod()


#*************************************************************************
def get_matches (sprotseq, pdbseq, offset): 
	"""Returns number of amino acid matches between two input sequences 
	with the longer sequence at defined offset

	Input: 	sprotseq 			--- string of amino acid sequence from PDB file 
			pdbseq				--- string of amino acid sequence from Swiss Prot file 
			offset 				--- integer by which the longer and shorter 
									sequence are offset for comparison 
	Return: number_of_matches 	--- integer, number of matches between two sequences
	

	26.10.21 	Original 	By: BAM

	>>> get_matches ("test2.faa", "test.faa", 1)
	0
	>>> get_matches ("test2.faa", "test.faa", 2)
	8
	>>> get_matches ("test2.faa", "test.faa", 3)
	0
	>>> 
	"""

	#use the define_lengths function to read and edit files and identify the shorter and longer sequence
	(long_seq, short_seq) = define_lengths (sprotseq, pdbseq) 	
	#check matches for all positions along shorter sequence
	position = range(len(short_seq))
	number_of_matches = 0
	
	for x in position:
		#check if letters being compared are within the length of the sequence
		#match of letter in short sequence and the letter in the longer sequence at an offset
		if ((x + offset < len(long_seq)) and (long_seq[x + offset] == short_seq[x])):
			#increase number of matches for each match of S position to L position+offset
			number_of_matches = number_of_matches + 1 		
	return number_of_matches

if __name__ == "__main__":
   import doctest
   doctest.testmod()


#*************************************************************************
def check_all_offsets (sprotseq, pdbseq):
	"""Returns a tuple of total matches between two sequences and the 
	offset value that results in this best match number

	Input: 	sprotseq 				--- string of amino acid sequence from PDB file 
			pdbseq					--- string of amino acid sequence from Swiss Prot file 
	Return: best_number_of_matches 	--- number of matches between two sequences
			best_offset 			--- offset value that gives the most matches (best alignment of sequences)
	

	26.10.21 	Original 	By: BAM

	>>> check_all_offsets ("test2.faa", "test.faa")
	(8, 2)
	>>> check_all_offsets ("test1.faa", "test.faa")
	(5, 0)
	>>> 
	"""

	#use define_lengths to get short and long sequence between two sequences
	(long_seq, short_seq) = define_lengths (sprotseq, pdbseq)
	best_number_of_matches = 0
	#possible offsets include all integers in range from 0 to the difference in length of the sequences
	offsets = range(len(long_seq) - len(short_seq))
	
	for x in offsets:
		#get number_of_matches using get_matches function and all possible offsets
		number_of_matches = get_matches (sprotseq, pdbseq, x)
		if number_of_matches > best_number_of_matches:
			#if the number of matches for this offset is better than for previous matches it becomes best_number_of_matches
			best_number_of_matches = number_of_matches
			best_offset = x
	return best_number_of_matches, best_offset

if __name__ == "__main__":
   import doctest
   doctest.testmod()


#*************************************************************************
def show_mismatches (sprotseq, pdbseq):
	"""Print positions of all mismatches in the best alignment between 
	sequences sprotseq and pdbseq, with respect to positions in longer and 
	shorter sequence (position 1 is the fisrt amino acid in the sequence)

	Input: 	sprotseq 				--- string of amino acid sequence from PDB file 
			pdbseq					--- string of amino acid sequence from Swiss Prot file 

	26.10.21 	Original 	By: BAM

	>>> show_mismatches ("test2.faa", "test.faa")
	Mismatch at short sequence position
	3
	with long sequence position
	5
	Mismatch at short sequence position
	4
	with long sequence position
	6
	>>> show_mismatches ("test2.faa", "test1.faa")
	Mismatch at short sequence position
	3
	with long sequence position
	5
	Mismatch at short sequence position
	4
	with long sequence position
	6
	>>> 
	"""

	#use check_all_offsets to get best number of matches and best offset to use for this alignment
	(best_number_of_matches, best_offset) = check_all_offsets (sprotseq, pdbseq)
	#use define_lengths to get the two sequences
	(long_seq, short_seq) = define_lengths (sprotseq, pdbseq)
	#check all positions along the short sequence
	position = range(len(short_seq))
	
	for x in position:
		#check the positions being checked are in the sequence
		#if the letter is not the same 
		if ((x + best_offset < len(long_seq)) and (long_seq[x + best_offset] != short_seq[x])):
			#print the mismatches relative to short and long sequence position
			print ("Mismatch at short sequence position") 
			#1st position is the first letter (not like python with position 0 being first)
			print (x + 1)
			print ("with long sequence position")
			print (x + best_offset + 1) 

if __name__ == "__main__":
   import doctest
   doctest.testmod()


#*************************************************************************

#file1 = sys.argv[1]
#file2 = sys.argv[2]




