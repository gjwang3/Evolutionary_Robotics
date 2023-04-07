import math

import pyrosim.pyrosim as pyrosim
# tell pyrosim the name of the file for storing information
pyrosim.Start_SDF("boxes.sdf")
# stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf
HEIGHT = []
for i in range(10):
    
    HEIGHT.append(1*math.pow(0.9, i))
    length, width, height = 1*math.pow(0.9, i), 1*math.pow(0.9, i), HEIGHT[i]
    x, y, z = 0, 0, sum(HEIGHT) - HEIGHT[i]/2
    pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height ]) 
    
# tells pyrosim to close the sdf file
pyrosim.End()