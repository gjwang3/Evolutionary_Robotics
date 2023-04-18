# run this code in terminal; otherwise some functions do not work in Spyder

#test if phybullet is installed
import pybullet as p
import time # sleep
import pybullet_data # add floor
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random

#creat an object 
physicsClient = p.connect(p.GUI)
# add floor
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# disable the sidebars on the pybullet simulation/speed up simulation
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# add gravity
p.setGravity(0,0,-9.8)
# add floor
planeId = p.loadURDF("plane.urdf")
# reads body.urdf into an object called robotId, return an integer
robotId = p.loadURDF("body.urdf")
# tells pybullet to read in the world described in box.sdf.
p.loadSDF("world.sdf")
# additional setting up for simulating sensors
pyrosim.Prepare_To_Simulate(robotId)

numIteration = 1000
# has the same length as the number of iterations of your for loop
backLegSensorValues = np.zeros(numIteration)
frontLegSensorValues = np.zeros(numIteration)
# scale = math.pi/4
# targetAngles = scale * np.sin(np.linspace(0, 2*math.pi, numIteration))# -scale ro scale
amplitudeBackLeg = math.pi/4
frequencyBackLeg = 10
phaseOffsetBackLeg = 0
backLegMotorValues = amplitudeBackLeg * np.sin(frequencyBackLeg * np.linspace(0, 2*math.pi, numIteration) + phaseOffsetBackLeg)# -scale ro scale
amplitudeFrontLeg = math.pi/4
frequencyFrontLeg = 10
phaseOffsetFrontLeg = math.pi/4 #0
frontLegMotorValues = targetAngles = amplitudeFrontLeg * np.sin(frequencyFrontLeg * np.linspace(0, 2*math.pi, numIteration) + phaseOffsetFrontLeg)# -scale ro scale
#exit()


for i in range(numIteration):
#    
  p.stepSimulation()
# add a touch sensor to the back leg , touch sensors only work in non-root links
  backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  #print(backLegTouch)
  backLegSensorValues[i] = backLegTouch
 # add a touch sensor to the front leg , touch sensors only work in non-root links
  frontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
  #print(frontLegTouch)
  frontLegSensorValues[i] = frontLegTouch 
  
# add a motor to backLeg
  pyrosim.Set_Motor_For_Joint(
# what robot the motor should be attached
  bodyIndex = robotId,
# what joint the motor should be attached to
#  jointName = "Torso_BackLeg", 
  jointName = b'Torso_BackLeg', #if above does not work
# how the motor will attempt to control the motion
  controlMode = p.POSITION_CONTROL, # or velocity control

# stand on the toe
# targetPosition =  math.pi/4.0,
# targetPosition =  math.pi*random.random() - math.pi/2.0, #-pi/2 to pi/2, random is 0 to 1
# walk    
  targetPosition = backLegMotorValues[i],
  
  maxForce = 25)  # how strong the motors are, 500 fly in the air
  
 
  
# add a motor to frontLeg
  pyrosim.Set_Motor_For_Joint(
# what robot the motor should be attached
  bodyIndex = robotId,
# what joint the motor should be attached to
#  jointName = "Torso_BackLeg", 
  jointName = b'Torso_FrontLeg', #if above does not work
# how the motor will attempt to control the motion
  controlMode = p.POSITION_CONTROL, # or velocity control

# stand on the toe
# targetPosition =  -math.pi/4.0,
# targetPosition =  math.pi*random.random() - math.pi/2.0,
# walk  
  targetPosition = frontLegMotorValues[i],
  maxForce = 25)  
  
#sleeping our code by 1/60th of a second during each pass through the loop
  time.sleep(1/240)
  print(i)
  
p.disconnect()


print(backLegSensorValues)
# git is usually used to manage software, not data
np.save('./data/backLegSensorValues',backLegSensorValues)
print(frontLegSensorValues)
np.save('./data/frontLegSensorValues',frontLegSensorValues)

np.save('./data/backLegMotorValues',backLegMotorValues)
np.save('./data/frontLegMotorValues',frontLegMotorValues)
