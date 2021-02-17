import os

print("Files present with the .tsv extension:")
print("*************************")
for file in os.listdir():
    if file[-4:] == ".tsv":
        print(file)
print("*************************")

userinput = input('Enter the name of the TSV file you would like to be read:')
TSVfile = open(userinput)

#empty things filled later by script
unique = set()
f = open("Nucleic_Acid_Color_And_Align.pml", "a")

#Eliminates duplicate PDBs
for row in TSVfile:
    a = row.split()
    if a[0] =="pdb":
        continue
    unique.add(a[0])


#Load PDBs into PyMol and color appropriately
for PDB in unique:
    f.write("load "+PDB+"-proc.PDB"+"\n")

f.write("color red, (chain y)"+"\n")
f.write("color blue, (chain z)"+"\n")
f.write("color green, (chain f)"+"\n")
f.write("color warmpink, c. y and resi 1-114"+"\n")
f.write("color lightblue, c. z and resi 1-107"+"\n")

#Align all PDBs against the same reference. Align on the heavy chain variable domain
for PDB in unique:
    f.write("align "+PDB+"-proc and c. y and resi 1-114, "+a[0]+"-proc and c. y and resi 1-114"+"\n")

#Hide everything, then show antibody and antigen as ribbon
f.write("hide all"+"\n")
f.write("show ribbon, chain 'y'"+"\n")
f.write("show ribbon, chain 'z'"+"\n")
f.write("show ribbon, chain 'f'"+"\n")
