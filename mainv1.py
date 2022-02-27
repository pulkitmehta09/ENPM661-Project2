#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:05:36 2022

@author: pulkit
"""

from functionsv1 import *


map = create_map()
start_node = getStartNode(map)
goal_node = getGoalNode(map)

Djikstra(start_node, goal_node, map)

