
import pyrosim.pyrosim as pyrosim
# tell pyrosim the name of the file for storing information
pyrosim.Start_SDF("box.sdf")
# stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf.
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
# tells pyrosim to close the sdf file
pyrosim.End()