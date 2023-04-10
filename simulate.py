# run this code in terminal; otherwise some functions do not work in Spyder

#test if phybullet is installed
import pybullet as p
import time # sleep
import pybullet_data # add floor
import pyrosim.pyrosim as pyrosim
import numpy as np

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
# reads body.urdf into an object called robotId
robotId = p.loadURDF("body.urdf")
# tells pybullet to read in the world described in box.sdf.
p.loadSDF("world.sdf")
# additional setting up for simulating sensors
pyrosim.Prepare_To_Simulate(robotId)
# has the same length as the number of iterations of your for loop
backLegSensorValues = np.zeros(100)
frontLegSensorValues = np.zeros(100)
#exit()


for i in range(100):
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
#sleeping our code by 1/60th of a second during each pass through the loop
  time.sleep(1/60)
  print(i)
  
p.disconnect()


print(backLegSensorValues)
# git is usually used to manage software, not data
np.save('./data/backLegSensorValues',backLegSensorValues)
print(frontLegSensorValues)
np.save('./data/frontLegSensorValues',frontLegSensorValues)