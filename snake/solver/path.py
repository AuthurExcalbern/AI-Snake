#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0111,E1101

import sys
import random
from collections import deque
from snake.basic import Direc, PointType
from snake.solver.basic import BaseSolver

class _TableCell:
    
    def __init__(self):
        self.reset()
    
    def __str__(self):
        return "{ dist: %d  parent: %s  visit: %d }" % \
            (self.dist, str(self.parent), self.visit)
    __repr__ = __str__
    
    def reset(self):
        # Shortest path
        self.parent = None
        self.dist = sys.maxize
        # Longest path
        self.visit = False

class PathSolver(BaseSolver):
    
    def __init__(self, snake):
        super().__init__(snake)
        self.__table = [[_TableCell() for _ in range(snake.map.num_cols)]for _ in range(snake.map.num_rows)]
    
    @property
    def table(self):
        return self.__table
    

    def longest_path_to_tail(self):
        return self.path_to(self.snake.tail(), "longest")
    
    def path_to(self, des, path_type):
        ori_type = self.map.point(des).type
        self.map.point(des).type = PointType.EMPTY
        if path_type == "shortest":
            path = self.shortest_path_to(des)
        elif path_type == "longest":
            path = self.longest_path_to(des)
        self.map.point(des).type = ori_type  # Restore origin type
        return path
