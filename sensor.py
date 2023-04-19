#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 12:28:41 2023

@author: guanjinwang
"""
import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:
    # constructor
    def __init__(self,linkname):

        self.values = np.zeros(c.numIteration)
        #self.values = []


    def Get_Value(self,linkName):
        # add a touch sensor to the leg , touch sensors only work in non-root links
        return pyrosim.Get_Touch_Sensor_Value_For_Link(linkName)