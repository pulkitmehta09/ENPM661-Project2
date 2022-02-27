#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 00:42:42 2022

@author: pulkit
"""

from functions import *
import numpy as np
import cv2


map_img, map = create_map()

def Djikstra(start_node, goal_node):
    
    
    map_img, map = create_map()

    OpenList = PriorityQueue()
    open_set = set()
    
    ClosedList = []
    closed_set = set()
    
    
    start_node.append(0)            # 2 - index of node
    start_node.append(-1)           # 3 - parent node
    start_node.append(0)            # 4 - costtocome
    start_node.append(0)            # 5 - total cost
    OpenList.put((start_node[5],start_node))
    open_set.add(tuple(start_node[:2]))
    
    isgoal = False
    success = False
    count = 0
    
    moves = ['N','NE','E','SE','S','SW','W','NW']

    while not(OpenList.empty() and isgoal):
        node = OpenList.get()
        node = node[1][:]
        open_set.remove(tuple(node[:2]))
        ClosedList.append(node)
        closed_set.add(tuple(node[:2]))
        if node[:2] == goal_node or count == 100000:
            path = []
            parent_index = node[3]
            while (parent_index != -1):
                n = ClosedList[parent_index]
                path.append((n[0],n[1]))
                parent_index = n[3]
            
            path = list(reversed(path))
            path.append((goal_node[0],goal_node[1]))
            
            return closed_set, path
            
        
        for direction in moves:
            new_node, cost = ActionMove(node, direction)
            if not ((tuple(new_node[:2]) in closed_set) and isObstacle(new_node[:2],map) and isnotValid(new_node[:2])):
                if not (tuple(new_node[:2]) in open_set):
                    new_node[3] = node[2]
                    new_node[4] = node[4] + cost
                    new_node[5] = new_node[4]
                    OpenList.put((new_node[5],new_node))
                    open_set.add(tuple(new_node[:2]))
                else:
                    if(new_node[5] > node[4] + cost):
                        new_node[3] = node[2]
                        new_node[4] = node[4] + cost
                        new_node[5] = new_node[4]
                        
        count+=1                    
        




start_node = getStartNode()
goal_node = getGoalNode()

close = Djikstra(start_node,goal_node)

# map_img = cv2.flip(map_img,0)
cv2.namedWindow("map", cv2.WINDOW_NORMAL)
cv2.imshow('map', map_img)
cv2.waitKey(0)
cv2.destroyAllWindows()