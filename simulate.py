# run this code in terminal; otherwise some functions do not work in Spyder

#test if phybullet is installed
import pybullet as p
import time # sleep
import pybullet_data # add floor

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

# tells pybullet to read in the world described in box.sdf.
p.loadSDF("boxes.sdf")

for i in range(1000):
  p.stepSimulation()
#sleeping our code by 1/60th of a second during each pass through the loop
  time.sleep(1/60)
  print(i)
  
p.disconnect()



