#to run: python3 miniproject.py P11413.faa PDB5ukw_nomutant.faa
import sys

sprotseq = sys.argv[1]
pdbseq = sys.argv[2]

#reading the files and deleting breaks
def read_file(filename):
	"""Read input files without first row and delete breaks"""
	with open(filename) as file:
		rows = file.readlines()[1:] 		#read all but first line
		combined = ''.join(rows) 		#make into string
		combined = combined.replace('\n', '') 		#get rid of breaks
		return combined 

print("does read_file work?" + (read_file("test.faa")))
#print((read_file(pdbseq)))


def edit_file(file):
	"""reads the file and makes all characters upper case"""
	file = read_file(file)
	file = file.upper() 		#all uppercase
	return file

print((edit_file("test.faa")))


#reading the two files and changing them to compare
def compare_seqs (sprotseq, pdbseq):
	"""Compare 2 sequences to identity whether the PDB sequence pdbseq is the same as the swiss prot sequence sprotseq"""
	sprotseq = edit_file(sprotseq)
	pdbseq = edit_file(pdbseq)
	#return True if pdbseq in sprotseq else False
	return True if pdbseq in sprotseq else False


#print("The sequences are the same") if pdbseq in sprotseq else print ("The sequences are different")


#test compare_seq function
print ("test comparison:")
print(compare_seqs ("test.faa", "test2.faa"))

print ("Swiss Prot and PDB sequences are the same:")
print(compare_seqs(sprotseq, pdbseq))

#print(edit_file(pdbseq))


best_offset = 0		#best offset position
best_number_of_matches = 0 		# how well the best offset scores

def define_lengths (pdbseq, sprotseq):
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

#test define_lenghts
print(define_lengths(edit_file("test.faa"), edit_file("test2.faa")))

def get_matches (L, S, offset): 
	"""Returns number_of_matches between L and S at a certain offset"""
	position = range(len(S)) #for all the positions in shorter sequence
	print (position)
	number_of_matches = 0
	for x in position:
		if ((x + offset < len(L)) and (L[x + offset] == S[x])):
			number_of_matches = number_of_matches + 1 #increase number of matches for each match of S position to L position+offset
	return number_of_matches

#test get_matches
print(get_matches(edit_file("test.faa"), edit_file("test2.faa"), 0))

#offsets to check - len(L) - len(S)
#offsets = len(L) - len(S) 

#if number_of_matches > best_number_of_matches:
	#best_number_of_matches = number_of_matches

#if compare_seqs (sprotseq, pdbseq) == True:
	#define_lengths (pdbseq, sprotseq)
	#get_matches (L, S, )









#compare characters in sequences 
#def differences (seq1, seq2):
	#"""Prints the number of differences across two strings seq1 and seq 2"""
	#count = sum(1 for a, b in zip(seq1, seq2) if a != b)
	#return print(count)

#slide sequence  - put differences into it, print differences in the smallest number of differences








