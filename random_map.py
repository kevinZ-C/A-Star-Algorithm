# random_map.py

import numpy as np

import point


class IdealMap:
    def __init__(self, size=20):
        self.size = size
        self.obstacle = 25
        self.GenerateObstacle()

    def GenerateObstacle(self):
        self.obstacle_point = []
        grid_size = self.size // 5  # 将地图划分为5*5个大方格

        # 生成25个大方格的中心点
        grid_centers = [(i * grid_size + grid_size // 2, j * grid_size + grid_size // 2)
                        for i in range(5) for j in range(5)]

        # 在25个大方格中随机选取10个生成障碍
        selected_centers = np.random.choice(range(25), size=self.obstacle, replace=False)
        for center_index in selected_centers:
            x, y = grid_centers[center_index]
            for dx in range(-1, 1):  # 生成2*2的障碍
                for dy in range(-1, 1):
                    self.obstacle_point.append(point.Point(x + dx, y + dy))

    def IsObstacle(self, i, j):
        for p in self.obstacle_point:
            if i == p.x and j == p.y:
                return True
        return False
