#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:05:36 2022

ENPM 661
Project 1

@author: Pulkit Mehta
UID: 117551693
"""

from functions import *

map = create_map()

initialize()

start_node = getStartNode(map)
goal_node = getGoalNode(map)

nodes = Dijkstra(start_node, goal_node, map)
node_objects, path = GeneratePath(nodes, goal_node)

Animate(node_objects, path, map)

