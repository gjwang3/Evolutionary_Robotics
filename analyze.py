#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:47:08 2023

@author: guanjinwang
"""

import numpy as np
import matplotlib.pyplot as plt

# with open('./data/backLegSensorValues.npy', 'wb') as f:
#     np.load(f)
######################################################   plot sensor data ####################################  
# backLegSensorValues = np.load('./data/backLegSensorValues.npy')
# frontLegSensorValues = np.load('./data/frontLegSensorValues.npy')

# print(backLegSensorValues)
# print(frontLegSensorValues)

# line_down, = plt.plot(backLegSensorValues, linewidth = 10, label='backLegSensor')
# line_up, = plt.plot(frontLegSensorValues,label='frontLegSensor') 

# #plt.legend()
# plt.legend(handles=[line_down, line_up])
# plt.show()

########################################################################################################### 


backLegMotorValues = np.load('./data/backLegMotorValues.npy')
frontLegMotorValues = np.load('./data/frontLegMotorValues.npy')



line_down, = plt.plot(backLegMotorValues, linewidth = 10, label='backLegMotor')
line_up, = plt.plot(frontLegMotorValues,label='frontLegMotor') 

#plt.legend()
plt.legend(handles=[line_down, line_up])
plt.show()