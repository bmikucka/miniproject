import sys

sprotseq = sys.argv[1]
pdbseq = sys.argv[2]

#reading the files and deleting breaks
def read_file(filename):
	"""Read input files"""
	with open(filename) as file:
		file = file.read().replace('\n', '') 
		return file 

print("Read file function works if testfile:" + (read_file("test.faa")))


def edit_file(file):
	"""reads the file, deletes breaks and makes all characters upper case. deletes first 7 characters"""
	file = read_file(file)
	file = file.upper()
	file = file[7:]
	return file

print("Edit file function works if TESTFILE:" + (edit_file("test.faa")))


#reading the two files and changing them to compare
#still need to remove the identifier bits off the pdb chain to be able to compare them
def compare_seqs (sprotseq, pdbseq):
	"""Compare 2 sequences to identity whether the PDB sequence pdbseq is the same as the swiss prot sequence sprotseq"""
	sprotseq = edit_file(sprotseq)
	pdbseq = edit_file(pdbseq)
	#return True if pdbseq in sprotseq else False
	return (print("The sequences are the same") if pdbseq in sprotseq else print ("The sequences are different"))

#test compare_seq function
print ("compare seqs works if true:")
print((compare_seqs ("test.faa", "test2.faa")))

print(compare_seqs (sprotseq, pdbseq))

#print(edit_file(pdbseq))



