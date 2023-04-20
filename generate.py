import math

import pyrosim.pyrosim as pyrosim
# it generates links and joints and sends them to a urdf file, broadly-used file format in the robotics community
# generate neurons and synapses and send them to a nndf file, nndf files, specific to pyrosim, in-house python robotics simulator, neural network-controlled robot


##################################### working pyramid######################################################################
# tell pyrosim the name of the file for storing information
# pyrosim.Start_SDF("boxes.sdf")
# # stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf
# HEIGHT = []
# for i in range(10):
    
#     HEIGHT.append(1*math.pow(0.9, i))
#     length, width, height = 1*math.pow(0.9, i), 1*math.pow(0.9, i), HEIGHT[i]
#     x, y, z = 0, 0, sum(HEIGHT) - HEIGHT[i]/2
#     pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height ]) 
# pyrosim.End()
##########################################################################################################################


###############################working two blocks w/o link###############################################################
# def Create_World():
#     # tell pyrosim the name of the file for storing information
#     pyrosim.Start_SDF("world.sdf")
#     # stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf
#     lengthWorld, widthWorld, heightWorld = 1, 1, 1
#     xWorld, yWorld, zWorld = 0, 0, 0.5
#     pyrosim.Send_Cube(name="Box", pos=[xWorld, yWorld, zWorld] , size=[lengthWorld, widthWorld, heightWorld]) 
#     # tells pyrosim to close the sdf file
#     pyrosim.End()

# def Create_Robot():
#     pyrosim.Start_URDF("body.urdf")
#     lengthRobot, widthRobot, heightRobot = 1, 1, 1
#     xRobot, yRobot, zRobot = 1, 0, 1.5
#     pyrosim.Send_Cube(name="Torso", pos=[xRobot, yRobot, zRobot ] , size=[lengthRobot, widthRobot, heightRobot]) 
#     pyrosim.End()
##########################################################################################################################


###############################error: URDF file with multiple root links found: Torso Leg#################################
################################URDF files must describe a robot in a tree data structure################################
# def Create_Robot():
#     pyrosim.Start_URDF("body.urdf")
#     lengthWorld, widthWorld, heightWorld = 1, 1, 1
#     xWorld, yWorld, zWorld = 0, 0, 0.5
#     pyrosim.Send_Cube(name="Torso", pos=[xWorld, yWorld, zWorld] , size=[lengthWorld, widthWorld, heightWorld]) 
#     lengthRobot, widthRobot, heightRobot = 1, 1, 1
#     xRobot, yRobot, zRobot = 1, 0, 1.5
#     pyrosim.Send_Cube(name="Leg", pos=[xRobot, yRobot, zRobot ] , size=[lengthRobot, widthRobot, heightRobot]) 
#     pyrosim.End()
#########################################################################################################################


################################use all absolute position wrong##########################################################
# def Create_Robot():
#     pyrosim.Start_URDF("body.urdf")
#     lengthWorld, widthWorld, heightWorld = 1, 1, 1
#     xWorld, yWorld, zWorld = 0, 0, 0.5
#     pyrosim.Send_Cube(name="Torso", pos=[xWorld, yWorld, zWorld] , size=[lengthWorld, widthWorld, heightWorld]) 
    
#     pyrosim.Send_Joint( name = "Torso_Leg" , parent= "Torso" , child = "Leg" , type = "revolute", position = [0.5,0,1])
    
#     lengthRobot, widthRobot, heightRobot = 1, 1, 1
#     xRobot, yRobot, zRobot = 1, 0, 1.5
#     pyrosim.Send_Cube(name="Leg", pos=[xRobot, yRobot, zRobot ] , size=[lengthRobot, widthRobot, heightRobot]) 
#     pyrosim.End()
#########################################################################################################################
#SDF specify environments, only links, no joints,disconnected objects, all link coordinates in SDF files are absolute.
def Create_World():
    # tell pyrosim the name of the file for storing information
    pyrosim.Start_SDF("world.sdf")
    # stores a box with initial position x=0, y=0, z=0.5, and length, width and height all equal to 1 meter, in box.sdf
    lengthWorld, widthWorld, heightWorld = 1, 1, 1
    xWorld, yWorld, zWorld = -1, -1, 0.5
    pyrosim.Send_Cube(name="Box", pos=[xWorld, yWorld, zWorld] , size=[lengthWorld, widthWorld, heightWorld]) 
    # tells pyrosim to close the sdf file
    pyrosim.End()
################################1st link/joint absolute, others (relative to upstream joint)##############################
# def Create_Robot():
#     pyrosim.Start_URDF("body.urdf")
#     lengthWorld, widthWorld, heightWorld = 1, 1, 1
#     xWorld, yWorld, zWorld = 0, 0, 0.5
#     pyrosim.Send_Cube(name="Link0", pos=[xWorld, yWorld, zWorld] , size=[lengthWorld, widthWorld, heightWorld]) 
    
#     pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
    
#     lengthRobot, widthRobot, heightRobot = 1, 1, 1
#     xRobot, yRobot, zRobot = 0, 0, .5
#     pyrosim.Send_Cube(name="Link1", pos=[xRobot, yRobot, zRobot ] , size=[lengthRobot, widthRobot, heightRobot]) 
#     pyrosim.End()
#########################################################################################################################


################################A three-link, two-joint robot#########################################################
#def Create_Robot():
def Generate_Body():
    pyrosim.Start_URDF("body.urdf")
    # Torso is root link (1st)
    lengthRobot, widthRobot, heightRobot = 1, 1, 1
    xRobot, yRobot, zRobot = 1.5, 0, 1.5
    pyrosim.Send_Cube(name="Torso", pos=[xRobot, yRobot, zRobot ] , size=[lengthRobot, widthRobot, heightRobot]) 
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
    
    lengthWorld, widthWorld, heightWorld = 1, 1, 1
    xWorld, yWorld, zWorld = -0.5, 0, -0.5
    pyrosim.Send_Cube(name="BackLeg", pos=[xWorld, yWorld, zWorld] , size=[lengthWorld, widthWorld, heightWorld]) 
   
    
    # as it is connected with root link, use absolute 
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
    
    lengthRobot, widthRobot, heightRobot = 1, 1, 1
    xRobot, yRobot, zRobot = 0.5, 0, -.5
    pyrosim.Send_Cube(name="FrontLeg", pos=[xRobot, yRobot, zRobot ] , size=[lengthRobot, widthRobot, heightRobot]) 
    pyrosim.End()
#########################################################################################################################


########################################################Brain ########################################################
#def Create_Robot():
def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    # neurons receive values from sensors; 
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    
    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
    pyrosim.End()
#########################################################################################################################




#call
Create_World()
#Create_Robot()
Generate_Body()
Generate_Brain()