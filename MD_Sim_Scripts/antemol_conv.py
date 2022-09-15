#!/usr/bin/env python3

import os as os
from openbabel import openbabel

os.chdir('./mol2_corrected')
allfilelist=os.listdir()
obconv=openbabel.OBConversion()
obconv.SetInAndOutFormats("mol2", "pdb")
mol= openbabel.OBMol()
for directory in allfilelist:
	print('directory ' + directory)
	os.chdir('./'+directory)
	files=os.listdir()
	print('FILES:')
	print(files)
	for file in files:
		fileroot=file.replace('correct.mol2', 'final')
		if 'ante_out' in file:
			print('ante_out ' + file)
			obconv.ReadFile(mol,file)
			obconv.WriteFile(mol,fileroot+'.pdb')
	os.chdir('..')
	
