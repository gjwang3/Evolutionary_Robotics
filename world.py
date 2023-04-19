#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:52:21 2023

@author: guanjinwang
"""
import pybullet as p

class WORLD:
   
    # constructor
    def __init__(self):

        # add floor
        self.planeId = p.loadURDF("plane.urdf")

        # tells pybullet to read in the world described in box.sdf.
        self.worldId = p.loadSDF("world.sdf")
        