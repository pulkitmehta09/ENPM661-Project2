#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:09:06 2022

ENPM 661
Project 1

@author: Pulkit Mehta
UID: 117551693
"""

class Node:
    def __init__(self, pos, cost, parent):
        self.pos = pos                      # Position of the node
        self.x = pos[0]                     # x-coordinate of the node
        self.y = pos[1]                     # y-coordinate of the node
        self.cost = cost                    # Total cost to reach the node 
        self.parent = parent                # Parent of the node
