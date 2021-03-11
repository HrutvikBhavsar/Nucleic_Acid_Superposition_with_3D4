# Antibody-Nucleic-Acid-Antigen-Superpose

Superimpose multiple Antibody-antigen structure whose antigens are nucleic acids

This is a project done by Nicholas Gao and Hrutvik Bhavsar.

The intended workflow of this pipeline is:

   0) Copy all the files in this directory to a new folder.

   1)Download a tsv from the Structural Antibody Database (http://opig.stats.ox.ac.uk/webapps/newsabdab/sabdab/search/, Search structures by attribute) that contains only antibodies bound to nucleic acid antigens. Or use 20210311_0849863_summary.tsv which was downloaded on 11Mar2021.
   
   2)Run Nucleic_Acid_DeleteBadPDBs.py, give the script the desired .tsv from step 1 and Nucleic_Acid_Exception_List.txt. A new .tsv (Nucleic_Acids-BadPDBsRemoved.tsv) will be generated that excludes lines described by the Exception List.
   
   3)Run Nucleic_Acid_UniquePDBs.py, give the script Nucleic_Acids-BadPDBsRemoved.tsv. A unique list of PDB codes (uniquepdbs.txt) will be generated.. Use uniquepdbs.txt with batch_download.sh to download PDB files to same directory as python scripts (command './batch_download.sh -f uniquepdbs.txt -p')
   
   4)Run Nucleic_Acid_Standardization.py, give the script Nucleic_Acids-BadPDBsRemoved.tsv. Nucleic_Acid_Standardization.pml will be created. Use Nucleic_Acid_Standardization.pml in PyMol on downloaded PDBs to: a) standardize chain names b) ensure only one antibody-antigen complex per PDB
   
   5)Run Nucleic_Acid_Color_And_Alignment.py, give the script Nucleic_Acids-BadPDBsRemoved.tsv. Nucleic_Acid_Color_And_Align.pml will be created. Use Nucleic_Acid_Color_And_Align.pml in PyMOL to: a) align all structures on the variable heavy domain b) color all structures to delineate antibody heavy chain, antibody light chain, antigen c) hide all other atoms not in b)
