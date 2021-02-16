#this script removes lines that correspond to "bad" PDBs in the .tsv, writes good PDB lines to new .tsv


import os

for file in os.listdir():
    if file[-4:] == ".tsv":
        print(file)
        
UserTSV=input('Enter the name of the TSV file you would like to be read: ')
tsv_file = open(UserTSV, "r")

for file in os.listdir():
    if "Exception" in file:
        print(file)
UserExceptions=input('Enter the name of the List of Exceptions PDBs you would like to be read: ')
ExceptionList = open(UserExceptions, "r")

#things to be filled later in script
BadPDBs=[]
#if "500Lines-BadPDBsRemoved.tsv" in os.listdir():
    #os.remove("500Lines-BadPDBsRemoved.tsv")
f = open("Nucleic_Acids-BadPDBsRemoved.tsv", "a")

#build list of bad PDBs
for line in ExceptionList:
    a = line.split()
    BadPDBs.append(a[0])

#remove bad PDB lines from tsv, write to new file
for line in tsv_file:
    a = line.split()
    if a[0] in BadPDBs:
        continue
    f.write(line)
