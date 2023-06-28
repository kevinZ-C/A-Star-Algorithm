# main.py

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

import random_map
import a_star

plt.figure(figsize=(5, 5))

map = random_map.IdealMap()

ax = plt.gca()
ax.set_xlim([0, map.size])
ax.set_ylim([0, map.size])

for i in range(map.size):
    for j in range(map.size):
        if map.IsObstacle(i,j):
            rec = Rectangle((i, j), width=1, height=1, color='gray')
            ax.add_patch(rec)
        else:
            rec = Rectangle((i, j), width=1, height=1, edgecolor='gray', facecolor='w')
            ax.add_patch(rec)

# 起点上色
# rec = Rectangle((0, 0), width = 1, height = 1, facecolor='b')
# ax.add_patch(rec)

# 终点标红
# rec = Rectangle((map.size-1, map.size-1), width = 1, height = 1, facecolor='r')
# ax.add_patch(rec)

# plt.axis('equal')
# plt.axis('off')
# plt.tight_layout()
#plt.show()

start_x = int(input("输入起点的横坐标："))
start_y = int(input("输入起点的纵坐标："))
rec = Rectangle((start_x, start_y), width = 1, height = 1, facecolor='b')
ax.add_patch(rec)

end_x = int(input("输入终点的横坐标："))
end_y = int(input("输入终点的纵坐标："))
rec = Rectangle((end_x, end_y), width = 1, height = 1, facecolor='r')
ax.add_patch(rec)

plt.axis('equal')
plt.axis('off')
plt.tight_layout()

a_star = a_star.AStar(map, start_x, start_y, end_x, end_y)
a_star.RunAndSaveImage(ax, plt, start_x, start_y)

