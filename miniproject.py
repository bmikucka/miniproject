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

file1 = sys.argv[1]
file2 = sys.argv[2]

#reading the files and deleting breaks
def read_file(filename):
	"""Read input files without first row and delete breaks"""
	with open(filename) as file:
		rows = file.readlines()[1:] 		#read all but first line
		combined = ''.join(rows) 		#make into string
		combined = combined.replace('\n', '') 		#get rid of breaks
		return combined 

#*************************************************************************



def edit_file(file):
	"""reads the file and makes all characters upper case"""
	file = read_file(file)
	file = file.upper() 		#all uppercase
	return file


#*************************************************************************

#reading the two files and changing them to compare
def compare_seqs (sprotseq, pdbseq):
	"""Compare 2 sequences to identity whether the PDB sequence pdbseq is the same as the swiss prot sequence sprotseq"""
	sprotseq = edit_file(sprotseq)
	pdbseq = edit_file(pdbseq)
	#return True if pdbseq in sprotseq else False
	return True if pdbseq in sprotseq else False


#*************************************************************************

def define_lengths (pdbseq, sprotseq):
	pdbseq = edit_file(pdbseq)
	sprotseq = edit_file(sprotseq)
	if len(pdbseq) < len(sprotseq):
		L = sprotseq
		S = pdbseq
	elif len(pdbseq) == len(sprotseq):
		L = sprotseq
		S = pdbseq
	else:
		S = sprotseq
		L = pdbseq
	return L, S


#*************************************************************************

def get_matches (sprotseq, pdbseq, offset): 
	"""Returns number_of_matches between L and S at a certain offset"""
	(L, S) = define_lengths (sprotseq, pdbseq) 		
	position = range(len(S))		 #for all the positions in shorter sequence
	number_of_matches = 0
	for x in position:
		if ((x + offset < len(L)) and (L[x + offset] == S[x])):
			number_of_matches = number_of_matches + 1 		#increase number of matches for each match of S position to L position+offset
	return number_of_matches

#*************************************************************************

#offsets to check
def check_all_offsets (sprotseq, pdbseq):
	(L, S) = define_lengths (sprotseq, pdbseq)
	best_number_of_matches = 0
	offsets = range(len(L) - len(S))
	for x in offsets:
		number_of_matches = get_matches (sprotseq, pdbseq, x)
		if number_of_matches > best_number_of_matches:
			best_number_of_matches = number_of_matches
			best_offset = x
	return best_number_of_matches, best_offset


#*************************************************************************

def show_mismatches (sprotseq, pdbseq):
	(best_number_of_matches, best_offset) = check_all_offsets (sprotseq, pdbseq)
	(L, S) = define_lengths (sprotseq, pdbseq) 	
	position = range(len(S))
	for x in position:
		if ((x + best_offset < len(L)) and (L[x + best_offset] != S[x])):
			print ("Mismatch at short sequence position") #1st position is the first letter (not like python with position 0 being first)
			print (x + 1)
			print ("with long sequence position")
			print (x + best_offset + 1) 

#*************************************************************************

print("does read_file work?" + (read_file("test.faa")))
#print((read_file(pdbseq)))

print((edit_file("test.faa")))

#print("The sequences are the same") if pdbseq in sprotseq else print ("The sequences are different")


#test compare_seq function
print ("test comparison:")
print(compare_seqs ("test.faa", "test2.faa"))

print ("Swiss Prot and PDB sequences are the same:")
print(compare_seqs(sprotseq, pdbseq))

#print(edit_file(pdbseq))

#print(check_all_offsets ("test.faa", "test2.faa"))

#show_mismatches ("test.faa", "test2.faa")



