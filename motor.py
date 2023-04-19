#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:29:08 2023

@author: guanjinwang
"""
import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import math

class MOTOR:
    # constructor
  
    def __init__(self,jointName):

        self.motorValues = np.zeros(c.numIteration)
        
        #self.values = []

    def Set_Value(self,jointName,amplitude,frequency,phaseoffset,maxForce):
        self.motorValues = amplitude * np.sin(frequency* np.linspace(0, 2*math.pi, c.numIteration) + phaseoffset)
        self.maxForce = maxForce
       

    # def Get_Value(self,linkName1):
    #     # add a touch sensor to the leg , touch sensors only work in non-root links
    #     return pyrosim.Get_Touch_Sensor_Value_For_Link(linkName1)