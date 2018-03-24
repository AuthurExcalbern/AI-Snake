#!/usr/bin/env python3
# -*-coding: utf-8 -*-
# pylint: disable=C0103,C0111

"""Definition of enum Direc(Direction)."""
#定义有关方向的类

from enum import Enum, unique

# Custom Class
# @unique can help us check the guarantee that there is no repeat value
# 装饰器检查不会枚举有相同值的元素
@unique
class Direc(Enum):
    """Directions on the game."""
    #定义各个方向在游戏中的值
    NONE = 0
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4
    
    # The static method of returning the function.
    # Direc().opposite() & Direc.opposite()
    # 定义静态方法，功能是转换到当前方向的相反方向
    @staticmethod
    def opposite(direc):
        """Return the opposite direction."""
        if direc == Direc.LEFT:
            return Direc.RIGHT
        elif direc == Direc.RIGHT:
            return Direc.LEFT
        elif direc == Direc.UP:
            return Direc.DOWN
        elif direc == Direc.DOWN:
            return Direc.UP
        else:
            return Direc.NONE
