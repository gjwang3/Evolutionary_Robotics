# run this code in terminal; otherwise some functions do not work in Spyder

#test if phybullet is installed
import pybullet as p
import time

#creat an object 
physicsClient = p.connect(p.GUI)
# disable the sidebars on the pybullet simulation/speed up simulation
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# tells pybullet to read in the world described in box.sdf.
p.loadSDF("box.sdf")

for i in range(1000):
  p.stepSimulation()
#sleeping our code by 1/60th of a second during each pass through the loop
  time.sleep(1/60)
  print(i)
  
p.disconnect()



