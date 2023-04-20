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
  
    def __init__(self,jointName, amplitude,frequency,phaseoffset,maxForce):

        # self.motorValues = np.zeros(c.numIteration)
        
        #self.values = []
        self.motorValues = amplitude * np.sin(frequency* np.linspace(0, 2*math.pi, c.numIteration) + phaseoffset)
        self.maxForce = maxForce

    def Set_Value(self,ith_timestep,desiredAngle):
        
        self.motorValues[ith_timestep] = desiredAngle
        #return self.motorValues
       

