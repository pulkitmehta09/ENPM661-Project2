#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 01:35:13 2022

@author: pulkit
"""

import numpy as np
import cv2
from queue import PriorityQueue

def getStartNode():
    flag = False
    while not flag:
        start_node = [int(item) for item in input("Enter the start node:").split(',')]
        if (len(start_node) == 2 and (0 <= start_node[0] <= 400) and (0 <= start_node[1] <= 250)):
            flag = True
        else:
            print("Enter a valid start node")
            flag = False
        
    return start_node


def getGoalNode():
    flag = False
    while not flag:
        goal_node = [int(item) for item in input("Enter the goal node:").split(',')]
        if (len(goal_node) == 2 and (0 <= goal_node[0] <= 400) and (0 <= goal_node[1] <= 250)):
            flag = True
        else:
            print("Enter a valid start node")
            flag = False
        
    return goal_node

# def Actions():
#     move = [[1,0,1],[-1,0,1],[0,1,1],[0,-1,1],[1,1,1.4],[-1,1,1.4],[1,-1,1.4],[-1,-1,1.4]]

#     return move                

def ActionMove(node,direction):
    if direction == 'N':
        new_node = node
        new_node[1] = node[1] + 1
        new_node[2] = node[2] + 1
        cost = 1
    elif direction == 'NE':
        new_node = node
        new_node[1] = node[1] + 1
        new_node[0] = node[0] + 1
        new_node[2] = node[2] + 1
        cost = 1.4
    elif direction == 'E':
        new_node = node
        new_node[0] = node[0] + 1
        new_node[2] = node[2] + 1
        cost = 1
    elif direction == 'SE':
        new_node = node
        new_node[1] = node[1] - 1
        new_node[0] = node[0] + 1
        new_node[2] = node[2] + 1
        cost = 1.4
    elif direction == 'S':
        new_node = node
        new_node[1] = node[1] - 1
        new_node[2] = node[2] + 1
        cost = 1
    elif direction == 'SW':
        new_node = node
        new_node[1] = node[1] - 1
        new_node[0] = node[0] - 1
        new_node[2] = node[2] + 1
        cost = 1.4
    elif direction == 'W':
        new_node = node
        new_node[0] = node[0] - 1
        new_node[2] = node[2] + 1
        cost = 1
    elif direction == 'NW':
        new_node = node
        new_node[1] = node[1] + 1
        new_node[0] = node[0] - 1
        new_node[2] = node[2] + 1
        cost = 1.4
    else:
        new_node = node
        cost = 0

    return new_node, cost


def line(p1,p2,x,y):
    f = ((p2[1] - p1[1]) * (x - p1[0])) / ( p2[0] - p1[0]) + p1[1] - y
    
    return f

def circle(center,r,x,y):
    c = (x - center[0])**2 + (y - center[1])**2 - r**2
    
    return c


def create_map():
    map = np.zeros((250,400))
    for i in range(map.shape[1]):
        for j in range(map.shape[0]):
            if (circle((300,65),40,i,j) < 0):
                map[j,i] = 1
            if (line((36,65),(115,40),i,j) < 0 and line((36,65),(105,150),i,j) > 0 and line((80,70),(105,150),i,j) < 0):
                map[j,i] = 1
            if (i > 165 and i < 235 and line((165,129.79),(200,109.59),i,j) < 0 and line((200,109.59),(235,129.79),i,j) < 0 and line((165,170.20),(200,190.41),i,j) > 0 and line((200,190.41),(235,170.20),i,j) > 0):
                map[j,i] = 1
            if (line((80,70),(105,150),i,j) > 0 and line((36,65),(115,40),i,j) < 0 and line((80,70),(115,40),i,j) > 0):
                map[j,i] = 1
                
    img = np.zeros((250,400,3))
    img[:,:,0] = 0
    img[:,:,1] = 0
    img[:,:,2] = map
    
    return img,map


def isObstacle(node,map):
    flag = False
    if map[node[1],node[0]] == 1:
        flag = True
    return flag
    

def isnotValid(node):
    flag = True
    if (node[1] > 0 and node[0] > 0 and node[1] < 250 and node[0] < 400):
        flag = False
    
    return flag