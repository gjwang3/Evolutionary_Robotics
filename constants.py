#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:30:30 2023

@author: guanjinwang
"""
import numpy as np
import math

numIteration = 1000
# # has the same length as the number of iterations of your for loop
# backLegSensorValues = np.zeros(numIteration)
# frontLegSensorValues = np.zeros(numIteration)
# scale = math.pi/4
# targetAngles = scale * np.sin(np.linspace(0, 2*math.pi, numIteration))# -scale ro scale

amplitude =[math.pi/4, math.pi/4]
frequency = [10,10]
phaseoffset = [0,math.pi/4]
maxForce = [25, 25]



# amplitudeBackLeg = math.pi/4
# frequencyBackLeg = 10
# phaseoffsetBackLeg = 0
# backLegMotorValues = amplitudeBackLeg * np.sin(frequencyBackLeg * np.linspace(0, 2*math.pi, numIteration) + phaseoffsetBackLeg)# -scale ro scale
# amplitudeFrontLeg = math.pi/4
# frequencyFrontLeg = 10
# phaseoffsetFrontLeg = math.pi/4 #0
# frontLegMotorValues = targetAngles = amplitudeFrontLeg * np.sin(frequencyFrontLeg * np.linspace(0, 2*math.pi, numIteration) + phaseoffsetFrontLeg)# -scale ro scale
# maxForceBackLeg = 25
# maxForceFrontLeg = 25
