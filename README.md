# Antibody-Nucleic-Acid-Antigen-Superpose

Superimpose multiple Antibody-antigen structure whose antigens are nucleic acids

This is a project done by Nicholas Gao and Hrutvik Bhavsar.

The intended workflow of this pipeline is:

   1)Download a tsv from the Structural Antibody Database (http://opig.stats.ox.ac.uk/webapps/newsabdab/sabdab/) that contains only antibodies bound to nucleic acid antigens. Or use tsv file already in this git repo.
   
   2)Use Nucleic_Acid_DeleteBadPDBs.py and Nucleic_Acid_Exception_List.tsv to delete bad lines from your .tsv.
   
   3)Use Nucleic_Acid_UniquePDBs.py to get a unique list of PDB codes. Use list of unique PDB codes with batch_download.sh to download PDB files to same directory as python scripts.
   
   4)Use Nucleic_Acid_Standardization.py to create a .pml. Use .pml in PyMol on downloaded PDBs to: a) standardize chain names b) ensure only one antibody-antigen complex per PDB c) 
   delete antigen atoms not near to antibody d) remove antibody constant domains
   
   5)Use Nucleic_Acid_Color_And_Alignment.py to create a .pml. Use .pml in PyMOL on downloaded PDBs to: a) superimpose all structures b) color all structures to delineate antibody heavy  
   chain, antibody light chain, antigen c) hide all other atoms not in b)
