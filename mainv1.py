#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:05:36 2022

@author: pulkit
"""

from functionsv1 import *

import numpy as np

map = create_map()

print("""
This program uses Djikstra's method for searching a path from user defined start and goal location in a given map.
The user needs to provide the coordinates of the start and goal node according to the format given below:
For example: For a node with x and y-coordinates as 100 and 200, 
Input: 100,200
(Note: Only comma seperated values are allowed)
	""")

start_node = getStartNode(map)
goal_node = getGoalNode(map)

visited, node_objects, path = Djikstra(start_node, goal_node, map)

Animate(node_objects, path, map)

# cv2.imshow('Djikstra', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()