#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:52:42 2023

@author: guanjinwang
"""
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
from sensor import SENSOR
from motor import MOTOR

from pyrosim.neuralNetwork import NEURAL_NETWORK

s = 2  # num of sensor instance
m = 2  # num of motor instance


class ROBOT:
    # constructor
    def __init__(self):
        self.sensors = dict()  # hashmap
        self.motors = dict()
        # reads body.urdf into an object called robotId, return an integer
        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        for self.linkName in pyrosim.linkNamesToIndices:
            # print(self.linkName)# BackLeg Torso FrontLeg, key of hashmap
            # print((pyrosim.linkNamesToIndices))
            self.sensors[self.linkName] = SENSOR(self.linkName)
            # print(self.sensors[self.linkName].values)

    def Sense(self, ith_timestep):
        for linkName1 in pyrosim.linkNamesToIndices:
            self.sensors[linkName1].values[ith_timestep] = self.sensors[linkName1].Get_Value(
                linkName1)
            # print(self.sensors[linkName1].values[ith_timestep])

    def Prepare_To_Act(self):

        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseoffset
        self.maxForce = c.maxForce
        motorID = 0
        for self.jointName in pyrosim.jointNamesToIndices:
            #print(self.jointName)  # key of hashmap
            #print((pyrosim.jointNamesToIndices))

            self.motors[self.jointName] = MOTOR(self.jointName, self.amplitude[motorID], self.frequency[motorID], self.offset[motorID], self.maxForce[motorID])
            #print(self.motors[self.jointName].values)
            motorID += 1

    def Act(self, ith_timestep):
    # def Act(self):   

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                self.jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                # print(neuronName)
                #print(self.jointName) # print new and check
                
                self.motors[self.jointName].Set_Value(ith_timestep,desiredAngle )
                

                #self.motors[self.jointName].motorValues[ith_timestep] #

    def Think(self):
        self.nn.Update()
        self.nn.Print()
