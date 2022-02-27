#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:05:36 2022

@author: pulkit
"""

from functionsv1 import *

import numpy as np

map = create_map()
start_node = getStartNode(map)
goal_node = getGoalNode(map)

visited, node_objects, path = Djikstra(start_node, goal_node, map)

Animate(node_objects, path, map)

# cv2.imshow('Djikstra', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()