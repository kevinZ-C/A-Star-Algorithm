# a_star.py

import sys
import time

import numpy as np

from matplotlib.patches import Rectangle

import point
import random_map

class AStar:
    def __init__(self, map, start_x=0, start_y=0, end_x=0, end_y=0):
        self.map = map
        self.open_set = []  # 待遍历节点
        self.close_set = [] # 已遍历节点
        self.start_point = [start_x, start_y]
        # print(self.start_point)
        self.end_point = [end_x, end_y]

    def BaseCost(self, p):
        x_dis = abs(p.x - self.start_point[0])
        y_dis = abs(p.y - self.start_point[1])
        # Distance to start point
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def HeuristicCost(self, p):
        x_dis = abs(p.x - self.end_point[0])
        y_dis = abs(p.y - self.end_point[1])
        # Distance to end point
        return x_dis + y_dis + (np.sqrt(2) - 2) * min(x_dis, y_dis)

    def TotalCost(self, p):
        return self.BaseCost(p) + self.HeuristicCost(p)

    def IsValidPoint(self, x, y):
        if x < 0 or y < 0:
            return False
        if x >= self.map.size or y >= self.map.size:
            return False
        return not self.map.IsObstacle(x, y)

    # 判断是否在某个节点列表中
    def IsInPointList(self, p, point_list):
        for point in point_list:
            if point.x == p.x and point.y == p.y:
                return True
        return False

    # 判断是否在待遍历列表中
    def IsInOpenList(self, p):
        return self.IsInPointList(p, self.open_set)

    # 判断是否在已遍历列表中
    def IsInCloseList(self, p):
        return self.IsInPointList(p, self.close_set)

    def IsStartPoint(self, p):
        return p.x == self.start_point[0] and p.y == self.start_point[1]

    def IsEndPoint(self, p):
        return p.x == self.end_point[0] and p.y == self.end_point[1]

    def SaveImage(self, plt):
        millis = int(round(time.time() * 1000))
        filename = './Results/' + str(millis) + '.png'
        plt.savefig(filename)

    def ProcessPoint(self, x, y, parent):
        if not self.IsValidPoint(x, y):
            return # Do nothing for invalid point
        p = point.Point(x, y)
        if self.IsInCloseList(p):
            return # Do nothing for visited point
        print('Process Point [', p.x, ',', p.y, ']', ', cost: ', p.cost)
        if not self.IsInOpenList(p):
            p.parent = parent
            p.cost = self.TotalCost(p)
            self.open_set.append(p)

    def SelectPointInOpenList(self):
        index = 0
        selected_index = -1
        min_cost = sys.maxsize
        for p in self.open_set:
            cost = self.TotalCost(p)
            if cost < min_cost:
                min_cost = cost
                selected_index = index
            index += 1
        return selected_index

    def BuildPath(self, p, ax, plt, start_time):
        path = []
        while True:
            path.insert(0, p) # Insert first
            if self.IsStartPoint(p):
                break
            else:
                p = p.parent
        for p in path:
            rec = Rectangle((p.x, p.y), 1, 1, color='g')
            ax.add_patch(rec)
            plt.draw()

        self.SaveImage(plt)
        end_time = time.time()
        print('===== Algorithm finish in', int(end_time-start_time), ' seconds')

    def RunAndSaveImage(self, ax, plt, start_x, start_y):
        start_time = time.time()

        start_point = point.Point(start_x, start_y)
        start_point.cost = 0
        self.open_set.append(start_point)

        while True:
            index = self.SelectPointInOpenList()
            if index < 0:
                print('No path found, algorithm failed!!!')
                self.SaveImage(plt)
                return

            p = self.open_set[index]
            rec = Rectangle((p.x, p.y), 1, 1, color='c')
            ax.add_patch(rec)

            if self.IsEndPoint(p):
                self.SaveImage(plt)
                return self.BuildPath(p, ax, plt, start_time)

            del self.open_set[index]
            self.close_set.append(p)

            # Process all neighbors
            x = p.x
            y = p.y
            # self.ProcessPoint(x-1, y+1, p)
            self.ProcessPoint(x-1, y, p)
            # self.ProcessPoint(x-1, y-1, p)
            self.ProcessPoint(x, y-1, p)
            # self.ProcessPoint(x+1, y-1, p)
            self.ProcessPoint(x+1, y, p)
            # self.ProcessPoint(x+1, y+1, p)
            self.ProcessPoint(x, y+1, p)
            # 假设机器人只有四自由度



