#!/usr/bin/env python3

from openmm.app import *
from openmm import *
from openmm.unit import *
from sys import stdout
import os

os.chdir('ante_pdbs')
connect_final="""CONECT    1    8    4    4                                            
CONECT    2   10   14                                                 
CONECT    3   24    7                                                 
CONECT    4    1    1                                                 
CONECT    5   11                                                      
CONECT    6   14   14                                                 
CONECT    7    9   11    8    3                                       
CONECT    8    1    7   18   17                                       
CONECT    9    7   12   12   10                                       
CONECT   10    2    9   13   13                                       
CONECT   11    7   14   19    5                                       
CONECT   12    9    9   20   15                                       
CONECT   13   10   10   16   21                                       
CONECT   14    2    6    6   11                                       
CONECT   15   12   22   16   16                                       
CONECT   16   13   15   15   23                                       
CONECT   17    8                                                      
CONECT   18    8                                                      
CONECT   19   11                                                      
CONECT   20   12                                                      
CONECT   21   13                                                      
CONECT   22   15                                                      
CONECT   23   16                                                      
CONECT   24    3                                                      
MASTER        0    0    0    0    0    0    0    0   24    0   24    0
END
"""

for file in os.listdir():
	print(file)
	with open(file,'a') as f:
		f.writelines(connect_final)
	pdb = PDBFile(file)
	forcefield = ForceField('../base.xml')
	system = forcefield.createSystem(pdb.topology)
	integrator = LangevinMiddleIntegrator(300*kelvin, 1/picosecond, 0.004*picoseconds)
	simulation = Simulation(pdb.topology, system, integrator)
	simulation.context.setPositions(pdb.positions)
	state=simulation.context.getState(getEnergy=True)
	energy = state.getPotentialEnergy()
	print(energy)


