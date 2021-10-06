sprotseq="/Users/basia/Desktop/mini_project/P11413.faa"
#pdbseq="/Users/basia/Desktop/mini_project/PDB5ukw_mutant.faa"
pdbseq_nonmut="/Users/basia/Desktop/mini_project/PDB5ukw_nomutant.faa"

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

