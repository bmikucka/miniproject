import sys

sprotseq = sys.argv[1]
pdbseq = sys.argv[2]

#reading the files here and uppercase so can be compared
def read_file(filename):
	"""Read input files and return as uppercase"""
	with open(filename) as file:
		return file.readlines().upper() [1:]

#making sure the breaks dont interfere with comaprison
def no_breaks(file):
	"""Gets rid of the rows in the file"""
	return file.strip

#reading the two files and changing them to compare
#still need to remove the identifier bits off the pdb chain to be able to compare them
def compare_seqs (sprotseq, pdbseq):
	"""Compare 2 sequences to identity whether the PDB sequence pdbseq is the same as the swiss prot sequence sprotseq"""
	read_file(sprotseq)
	no_breaks(sprotseq)
	read_file(pdbseq)
	no_breaks(pdbseq)
	return True if pdbseq in sprotseq else False

#nothing comes back - no true or false.

