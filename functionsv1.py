#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 18:04:49 2022

@author: pulkit
"""

import math
import numpy as np
import cv2
from queue import PriorityQueue
import time

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
                
    return map

def isObstacle(node,map):
    flag = False
    if map[node[1],node[0]] == 1:
        flag = True
    return flag
    

def isnotValid(node):
    flag = True
    if (node[1] >= 0 and node[0] >= 0 and node[1] < 250 and node[0] < 400):
        flag = False
    
    return flag


def getStartNode(map):
    """
    Get the start node from user.

    Returns
    -------
    start_node : Array
        Coordinates of start node.

    """
    flag = False
    while not flag:
        start_node = [int(item) for item in input("Enter the start node:").split(',')]
        if (len(start_node) == 2 and (0 <= start_node[0] <= 400) and (0 <= start_node[1] <= 250)):
            if not isObstacle(start_node,map):
                flag = True
            else:   
                print("Start node collides with obstacle")
        else:
            print("Enter a valid start node")
            flag = False
        
    return start_node


def getGoalNode(map):
    """
    Get the goal node from user.

    Returns
    -------
    goal_node : Array
        Coordinates of goal node.

    """
    flag = False
    while not flag:
        goal_node = [int(item) for item in input("Enter the goal node:").split(',')]
        if (len(goal_node) == 2 and (0 <= goal_node[0] <= 400) and (0 <= goal_node[1] <= 250)):
            if not isObstacle(goal_node,map):
                flag = True
            else:
                print("Goal node collides with obstacle")
        else:
            print("Enter a valid goal node")
            flag = False
        
    return goal_node


class Node:
    def __init__(self, pos, cost, parent):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.cost = cost
        self.parent = parent

def explore(node,map):
    x = node.x
    y = node.y

    moves = [(x, y + 1),(x + 1, y),(x, y -1),(x - 1, y),(x + 1, y + 1),(x + 1, y - 1),(x - 1, y - 1),(x - 1, y + 1)]
    valid_paths = []
    for pos, move in enumerate(moves):
        if not (move[0] >= 400 or move[0] < 0 or move[1] >= 250 or move[1] < 0):
            if map[move[1]][move[0]] == 0:
                cost = 1.4 if pos > 3 else 1
                valid_paths.append([move,cost])

    return valid_paths


def Djikstra(start_node, goal_node, map):

    q = PriorityQueue()
    visited = set([])
    node_objects = {}
    distance = {}

    for i in range(0, map.shape[1]):
        for j in range(0, map.shape[0]):
            distance[str([i,j])] = 999999
    
    distance[str(start_node)] = 0
    visited.add(str(start_node))
    node = Node(start_node,0,None)
    node_objects[str(node.pos)] = node
    q.put([node.cost, node.pos])
    reached = False

    img_show = np.dstack([map.copy() * 0, map.copy() * 0, map.copy() * 255])

    while not q.empty():
        node_temp = q.get()
        node = node_objects[str(node_temp[1])]
        if node_temp[1][0] == goal_node[0] and node_temp[1][1] == goal_node[1]:
            print("Goal Reached!!!")
            node_objects[str(goal_node)] = Node(goal_node,node_temp[0], node)
            reached = True
            break

        for next_node, cost in explore(node,map):

            if str(next_node) in visited:
                cost_temp = cost + distance[str(node.pos)]
                if cost_temp < distance[str(next_node)]:
                    distance[str(next_node)] = cost_temp
                    node_objects[str(next_node)].parent = node

            else:
                visited.add(str(next_node))
                img_show[next_node[1], next_node[0], :] = np.array([0,255,0])
                absolute_cost = cost + distance[str(node.pos)]
                distance[str(next_node)] = absolute_cost
                new_node = Node(next_node, absolute_cost, node_objects[str(node.pos)])
                node_objects[str(next_node)] = new_node
                q.put([absolute_cost, new_node.pos])

    
    goal = node_objects[str(goal_node)]
    parent_node = goal.parent
    while parent_node:
        img_show[parent_node.pos[1], parent_node.pos[0],:] = np.array([255,0,0])
        parent_node = parent_node.parent
    cv2.imshow('img', img_show)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


