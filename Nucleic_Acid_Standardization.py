import csv
import os

#read TSV into python
print("Files present with the .tsv extension:")
print("*************************")
for file in os.listdir():
    if file[-4:] == ".tsv":
        print(file)
print("*************************")

UserTSV = input('Enter the name of the TSV file you would like to be read: ')
tsv_file = open(UserTSV)
read_tsv = list(csv.reader(tsv_file, delimiter="\t"))

#this deletes any existing .pml files in the directory, opens a new empty .pml
for file in os.listdir():
    if ".pml" in file:
        os.remove(file)
f = open("Nucleic_Acid_Standardization.pml", "a")

#this runs through the .tsv, uses info in .tsv to appropriately populate the .pml
for i, line in enumerate(read_tsv):
    pdb = read_tsv[i][0]
    prevpdb = read_tsv[i-1][0]
    heavychain = read_tsv[i][1]
    lightchain = read_tsv[i][2]
    antigen = read_tsv[i][4]
    if i == 0: #exception command for first line
        continue
    if i == 1: #exception commands for second line
        print("load "+pdb+".pdb.gz", file=f)
        print("alter (chain "+heavychain+"), chain='y'", file=f)
        print("alter (chain "+lightchain+"), chain='z'", file=f)
        print("alter (chain "+antigen+"), chain='f'", file=f)
    elif pdb == prevpdb: #if prev entry is same pdb, delete duplicate antibody/antigen chains
        print("remove c. "+heavychain+" or c. "+lightchain+"", file=f)
        if len(antigen) == 1:
            print("remove c. "+antigen[0], file=f)
        if len(antigen) == 5:
            print("remove c. "+antigen[0]+" or c. "+antigen[4], file=f)
        if len(antigen) == 9:
            print("remove c. "+antigen[0]+" or c. "+antigen[4]+" or c. "+antigen[8], file=f)
        if len(antigen) == 17:
            print("remove c. "+antigen[0]+" or c. "+antigen[4]+" or c. "+antigen[8]+" or c. "+antigen[12]+" or c. "+antigen[16], file=f)
    elif pdb != prevpdb: #if prev entry is not same pdb => delete extraneous atoms, close out current entry, start chain renaming of next entry
        #print("remove c. y and not i. 1-114", file=f)
        #print("remove c. z and not i. 1-107", file=f)
        #print("sele c. f within 20 of c. y or c. z", file=f)
        #print("remove c. f and not sele", file=f)
        print("remove (chain C)", file=f)
        print("remove (chain D)", file=f)
        print("save "+prevpdb+"-proc.pdb, "+prevpdb, file=f)
        print("delete "+prevpdb, file=f)
        print("load "+pdb+".pdb.gz", file=f)
        print("alter (chain "+heavychain+"), chain='y'", file=f)
        print("alter (chain "+lightchain+"), chain='z'", file=f)
        if len(antigen) == 1:
            print("alter (chain "+antigen[0]+"), chain='f'", file=f)
        if len(antigen) == 5:
            print("alter (chain "+antigen[0]+" or chain "+antigen[4]+"), chain='f'", file=f)
        if len(antigen) == 9:
            print("alter (chain "+antigen[0]+" or chain "+antigen[4]+" or chain "+antigen[8]+"), chain='f'", file=f)
        if len(antigen) == 17:
            print("alter (chain "+antigen[0]+" or chain "+antigen[4]+" or chain "+antigen[8]+" or chain "+antigen[12]+" or chain "+antigen[16]+"), chain = 'f'", file=f)
    if i == len(read_tsv) - 1: #exception commands for last line
        print("remove (chain A)", file=f)
        print("remove (chain B)", file=f)
        print("remove (chain D)", file=f)
        print("remove (chain C)", file=f)
        #print("remove c. y and not i. 1-114", file=f)
        #print("remove c. z and not i. 1-107", file=f)
        #print("sele c. f within 20 of c. y or c. z", file=f)
        #print("remove c. f and not sele", file=f)
        print("save "+pdb+"-proc.pdb, "+ pdb, file=f)
        print("delete "+pdb, file=f)

f.close()
