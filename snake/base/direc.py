#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111

"""Definition of enum Direc."""
# 定义方向类型的枚举

from enum import Enum, unique
# 导入枚举类Enum和装饰器unique

# unique装饰器检查不会枚举有相同值的元素
@unique
class Direc(Enum):
    """Directions on the game plane."""
    # 定义各个方向在游戏中的值
    NONE = 0
    LEFT = 1
    UP = 2
    RIGHT = 3
    DOWN = 4

    # staticmethod返回函数的静态方法。该方法不强制要求传递参数
    # 可以不实例化调用：  Direc().opposite() & Direc.opposite()
    # 作用是返回当前方向的相反方向
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
