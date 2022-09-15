#!/usr/bin/env python3

import os as os
from openbabel import openbabel

connectivity="""
END """
#makes list of TorsionDrive files
allfilelist=os.listdir()
gid_files=[]
filetype='gid'
for file in allfilelist:
	if filetype in file :
		gid_files.append(file)
print('filelist',gid_files)

os.mkdir('optimized_tdrive_xyz')
os.mkdir('pdb_files')

# extracts optimised structure from TorsionDrive xyz file
for file in gid_files:
	num=str(len(os.listdir(file)))
	fullxyz=str(file+'/'+ num +'/tdrive.xyz')
	xyzdata=[]
	with open(fullxyz) as f:
		numatoms=f.readline()
		xyzdata.append(numatoms)
		xyzdata.append('\n')
		for line in (f.readlines()[-int(numatoms):]):
			xyzdata.append(line)
	finalxyz=open('optimized_tdrive_xyz/'+ file +'.xyz', 'w')
	for line in xyzdata:
		finalxyz.write(line)
		
#converts xyz file to pbd
obconv=openbabel.OBConversion()
obconv.SetInAndOutFormats("xyz", "pdb")
mol= openbabel.OBMol()
for file in gid_files:
	obconv.ReadFile(mol,'optimized_tdrive_xyz/'+file+'.xyz')
	obconv.WriteFile(mol,'pdb_files/' + file + '.pdb')
	
#corrects connectivity
	with open('pdb_files/'+file+'.pdb') as f1:
		positions=f1.readlines()[:26]
	with open('pdb_files/'+file+'_correct.pdb','w') as f2:
		f2.writelines(positions)
		f2.writelines(connectivity)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
