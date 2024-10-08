#This script takes the first column of Structural Antibody Database .tsv and returns a unique list of pdbs within.
#Make sure the TSVList variable is correctly specified to the name of the .tsv file
#The output of this script is a file named uniquepdbs.txt
#The PDB list in uniquepdbs.txt should be used to batch download from here (https://www.rcsb.org/pdb/download/download.do)

#reads TSV into python
import os
for file in os.listdir():
    if file[-4:] == ".tsv":
        print(file)
UserTSV = input('Enter the name of the TSV file you would like to be read: ')
TSVList = open(UserTSV)


#things to be filled later by script
unique = set()
f = open("uniquepdbs.txt", "a")


#add pdbs from TSV into python set
for line in TSVList:
    a = line.split()
    if a[0] == "pdb": #skip the header
        continue
    unique.add(a[0])

    
#write out unique PDBs to a text file
f.write(",".join(unique))
