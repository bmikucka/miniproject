#to run: python3 miniproject.py P11413.faa PDB5ukw_nonmutant.faa
import sys

sprotseq = sys.argv[1]
pdbseq = sys.argv[2]

#reading the files and deleting breaks
def read_file(filename):
	"""Read input files"""
	with open(filename) as file:
		rows = file.readlines()[1:]
		combined = ''.join(rows)
		combined = combined.replace('\n', '') 
		return combined 

print("does read_file work?" + (read_file("test.faa")))
print((read_file(pdbseq)))


def edit_file(file):
	"""reads the file, deletes breaks and makes all characters upper case. deletes first 7 characters"""
	file = read_file(file)
	file = file.upper()
	return file

print((edit_file("test.faa")))


#reading the two files and changing them to compare
def compare_seqs (sprotseq, pdbseq):
	"""Compare 2 sequences to identity whether the PDB sequence pdbseq is the same as the swiss prot sequence sprotseq"""
	sprotseq = edit_file(sprotseq)
	pdbseq = edit_file(pdbseq)
	#return True if pdbseq in sprotseq else False
	return print("The sequences are the same") if pdbseq in sprotseq else print ("The sequences are different")

	


#test compare_seq function
print ("test comparison:")
print((compare_seqs ("test.faa", "test2.faa")))

print(compare_seqs(sprotseq, pdbseq))

#print(edit_file(pdbseq))

#compare characters in sequences 
def differences (seq1, seq2):
	"""Prints the number of differences across two strings seq1 and seq 2"""
	count = sum(1 for a, b in zip(seq1, seq2) if a != b)
	return print(count)

#slide sequence  - put differences into it, print differences in the smallest number of differences








