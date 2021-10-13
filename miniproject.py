import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

print ('first argument was:' + file1)
print ("second file was:" + file2)

def read_file(filename):
	"""Read input files and return without first line"""
	with open(filename) as file:
		return file.readlines().upper() [1:]

def no_breaks(file):
	"""Gets rid of the rows in the file"""
	return file.strip


def compare_seqs (sprotseq, pdbseq):
	"""Compare 2 sequences to identity whether the PDB sequence pdbseq is the same as the swiss prot sequence sprotseq"""
	read_file(sprotseq)
	no_breaks(sprotseq)
	read_file(pdbseq)
	no_breaks(pdbseq)
	print(pdbseq, sprotseq)
	return True if pdbseq in sprotseq else False


compare_seqs(sprotseq, pdbseq_nonmut)

