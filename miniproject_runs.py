


sprot_file = sys.argv[1]
pdb_file = sys.argv[2]


if if_sequences_match (sprot_file, pdb_file) == False:
   show_mismatches (sprot_file, pdb_file)

   

if if_sequences_match ("test.faa", "test1.faa") == False:
   show_mismatches ("test.faa", "test1.faa")

if_sequences_match (sprot_file, pdb_file)
if_sequences_match ("test.faa", "test1.faa")