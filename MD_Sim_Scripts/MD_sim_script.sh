#!/bin/bash

python TD_conv.py
echo 'TD_conv done'

mkdir pdb_corrected
cd pdb_files

for file in *_correct.pdb
do 
mv $file ../pdb_corrected
done
echo 'files to pdb_corrected done'

cd ../pdb_corrected
for file in *
do
echo $file
mkdir ante_$file
mv $file ante_$file/
cd ante_$file/
antechamber -at gaff2 -c bcc -s 0 -nc -1 -i $file -fi pdb -o ante_out_$file -fo pdb
cd ..
done
echo 'antechamber done'

cd ..
mkdir ante_pdbs
cd pdb_corrected
for file in *
do
cd $file
for pdb in ante_out*
do 
echo $pdb
mv $pdb ../../ante_pdbs
done
cd ..
done
echo 'antemol move done'

cd ..
python MD_sim.py

echo 'MD Sim complete'
