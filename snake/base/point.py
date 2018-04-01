#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111

"""Definition of class Point."""
# 定义点类型的枚举

from enum import Enum, unique


@unique
class PointType(Enum):
    """Type of the points on the game map."""
    # 定义在游戏地图的各个值在地图里的含义，即为点的类型
    EMPTY = 0# 空
    WALL = 1# 墙
    FOOD = 2# 食物
    HEAD_L = 100# 头的方向
    HEAD_U = 101
    HEAD_R = 102
    HEAD_D = 103
    BODY_LU = 104# 身体的方向
    BODY_UR = 105
    BODY_RD = 106
    BODY_DL = 107
    BODY_HOR = 108
    BODY_VER = 109

# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
class Point:
    """Point on the game map."""
    # 定义在地图中的点
    def __init__(self):#游戏中的点初始都为空
        self._type = PointType.EMPTY#protected 类型的变量

    @property#用于得到点类型
    def type(self):
        return self._type

    @type.setter#用于设置点类型
    def type(self, val):
        self._type = val
