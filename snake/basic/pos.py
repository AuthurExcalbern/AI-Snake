#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111

"""Definition of class Pos(Position)."""
# 定义在地图中的位置类

from snake.basic.direc import Direc

class Pos:
    """
    Integer coordinate in 2D plane.
    
    The origin of the coordinate system is at the top-left corner,
    with x-axis extends downward and y-axis extends rightward.
    """
    # 2D地图，左上角为原点，xy轴向下和右延伸
    
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
    
    # __str__ : Use to convert values into a form suitable for human reading
    # 转换为可以让人类读的格式
    def __str__(self):
        return 'Pos(%d, %d)' % (self._x, self._y)
    #转换为可以让机器读的格式
    # __repr__ : Translate into the form that the interpreter reads
    __repr__ = __str__
    
    
    # Operation
    # 位置类的各种操作：计算位置
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self._x == other.x and self._y == other.y
        return NotImplemented
    
    def __pos__(self):
        return Pos(self._x, self._y)
    
    def __neg__(self):
        return Pos(-self._x, -self._y)
    
    def __and__(self, other):
        if isinstance(self, other.__class__):
            return Pos(self._x + other.x, self._y + other.y)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(self, other.__class__):
            return self + (-other)
        return NotImplemented
    
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    
    @staticmethod
    def manhattan_dist(p1, p2):
        return abs(p1.x - p2.x) + abs(p1.y - p2.y)
    
    def direc_to(self, adj_pos):
        """Return the direction of an sdjacent Pos relative to self."""
        # 返回从self位置走向adj_pos位置的方向
        if self._x == adj_pos.x:
            diff = self._y - adj_pos.y
            if diff == 1:
                return Direc.LEFT
            elif diff == -1:
                return Direc.RIGHT
        elif self._y == adj_pos.y:
            diff = self._x = adj_pos.x
            if diff == 1:
                return Direc.UP
            elif diff == -1:
                return Direc.DOWN
        return Direc.NONE
    
    def adj(self, direc):
        """Return the adjacent Pos in a given direction."""
        # 返回走向direc方向后的一个点
        if direc == Direc.LEFT:
            return Pos(self._x, self._y - 1)
        elif direc == Direc.RIGHT:
            return Pos(self._x, self._y + 1)
        elif direc == Direc.UP:
            return Pos(self._x + 1, self._y)
        elif direc == Direc.DOWN:
            return Pos(self._x - 1, self._y)
        else:
            return None
    
    def all_adj(self):
        """Return a list of all the adjacent Pos."""
        # 返回一个列表：包含走向所有方向后的点
        adjs = []
        for direc in Direc:
            if direc != Direc.NONE:
                adjs.append(self.adj(direc))
        return adjs
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, val):
        self.__x = val
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, val):
        self.__y = val
