#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:50:32 2023

@author: guanjinwang
"""
# run this code in terminal; otherwise some functions do not work in Spyder
    
#test if phybullet is installed
import pybullet as p
import time # sleep
import pybullet_data # add floor
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c

from world import WORLD
from robot import ROBOT


class SIMULATION:
    # constructor
    def __init__(self):
        # use “self” to access the attributes and methods of the class 
        #creat an object 
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # disable the sidebars on the pybullet simulation/speed up simulation
        #p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
        # add gravity
        p.setGravity(0,0,-9.8)
        # creates a new SIMULATION attribute, and that attribute will hold an instance of the WORLD class
        self.world = WORLD()
        self.robot = ROBOT()
        # additional setting up for simulating sensors
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        # get link name
        self.robot.Prepare_To_Sense()
        # get joint name
        self.robot.Prepare_To_Act()        
        
        # # #exit()
    def Run(self):
        for i in range(c.numIteration):   
            p.stepSimulation()
            # every simulation time step order: 1 sensor neurons 2 hidden neurons 3 motor neurons.
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            for jointNameEach in pyrosim.jointNamesToIndices:
                # print(jointNameEach) #debug
                # add a motor
                pyrosim.Set_Motor_For_Joint(
                # what robot the motor should be attached
                bodyIndex = self.robot.robotId,
                # what joint the motor should be attached to
                #  jointName = "jointNameEach", 
                # jointName = b'jointNameEach', #if above does not work
                jointName = jointNameEach,

                # how the motor will attempt to control the motion
                controlMode = p.POSITION_CONTROL, # or velocity control
                # walk    
                targetPosition = self.robot.motors[jointNameEach].motorValues[i],
  
                maxForce = self.robot.motors[jointNameEach].maxForce)  # how strong the motors are, 500 fly in the air
           
  
            #sleeping our code by 1/60th of a second during each pass through the loop
            time.sleep(1/240)
            # print(i)
 
         # save sensor data
    def Save_Values(self):  
        j = 0
        for legNameSensor in pyrosim.linkNamesToIndices:
            #print(self.robot.sensors[legNameSensor].values)
            j+=1
            np.save('./data/legNameSensor' +str(j),self.robot.sensors[legNameSensor].values)
        k =0
        for legNameMotor in pyrosim.jointNamesToIndices:
            #print(self.robot.motors[legNameMotor].motorValues)
            k+=1
            np.save('./data/legNameMotor' +str(k),self.robot.motors[legNameMotor].motorValues)
            
    # destructor
    def __del__(self):

        p.disconnect()
        




# # git is usually used to manage software, not data


# np.save('./data/backLegMotorValues',c.backLegMotorValues)
# np.save('./data/frontLegMotorValues',c.frontLegMotorValues)
