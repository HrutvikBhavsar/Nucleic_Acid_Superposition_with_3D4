# Antibody-Nucleic-Acid-Antigen-Superpose

Superimpose multiple Antibody-antigen structure that contain nucleic acids

This is a project done by Nicholas Gao and Hrutvik Bhavsar.

The intended workflow of this pipeline is:

   1)Use Nucleic_Acid_tsv_maker.py to make a tsv file that only includes PDBs whose antigen type are nucleic acids. Use this Nucleic_Acid_Only tsv in the following steps.
   2)Use Nucleic_Acid_DeleteBadPDBs.py and Nucleic_Acid_Exception_List.tsv to delete bad lines from your .tsv.
   3)Use Nucleic_Acid_UniquePDBs.py to get a list of PDB codes to download from https://www.rcsb.org/pdb/download/download.do. Put downloaded PDBs in same directory as python scripts.
   4)Use Nucleic_Acid_Standardization.py to create a .pml. Use .pml in PyMol on downloaded PDBs to: a) standardize chain names b) ensure only one antibody-antigen complex per PDB c) 
   delete antigen atoms not near to antibody d) remove antibody constant domains
   5)Use Nucleic_Acid_Color_And_Alignment.py to create a .pml. Use .pml in PyMOL on downloaded PDBs to: a) superimpose all structures b) color all structures to delineate antibody heavy  
   chain, antibody light chain, antigen c) hide all other atoms not in b)
