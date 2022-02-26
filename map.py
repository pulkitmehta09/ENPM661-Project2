#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:19:55 2022

@author: pulkit
"""

import numpy as np
import cv2


# map = np.zeros((250,400))


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


def isObstacle(x,y,map):
    flag = False
    if map[y,x] == 1:
        flag = True
    
    return flag
    



