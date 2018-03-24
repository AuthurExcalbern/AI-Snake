#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111

"""Definition of class Point."""
# 定义点的值

from enum import Enum, unique

# Custom Class
# @unique can help us check the guarantee that there is no repeat value
# 装饰器检查不会出现两个相同的赋值
class PointType(Enum):
    """Type of the points on the game map."""
    # 定义游戏地图中点的值（类型）
    
    EMPTY = 0
    WALL = 1
    FOOD = 2
    
    HEAD_L = 100
    HEAD_U = 101
    HEAD_R = 102
    HEAD_D = 103
    
    BODY_LU = 104
    BODY_UR = 105
    BODY_RD = 106
    BODY_DL = 107
    
    BODY_HOR = 108
    BODY_VER = 109



class Point:
    """Point on the game map."""
    # 定义地图中的点类
    
    # type is a private variable.
    def __init__(self):
        self._type = PointType.EMPTY
    
    # get velue
    @property
    def type(self):
        return self._type
    
    # set velue
    @type.setter
    def type(self, val):
        self.__type = val
