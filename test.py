# -*- coding: utf-8 -*-
'''
@author: Yang Yang
@contact: yanghhu@foxmail.com
@created on: 2020/4/17 21:12
'''
import numpy as np

node = [[-1, -1], [1, -1]]
E = 10.
v = 0.

x1, y1, = node[0][0], node[0][1]
x2, y2, = node[1][0], node[1][1]
dx = x2 - x1
dy = y2 - y1
mean_x = (x1 + x2) / 2.
mean_y = (y1 + y2) / 2.
a = (x1 * y2 - x2 * y1)

if a < 1.e-10:
    print ('Negative area (EleCoeff2NodeEle')

C1 = 0.5 * np.mat([[dy, 0.],[0., -dx],[-dx, dy]])
C2 = 0.5 * np.mat([[-mean_y, 0.],[0., mean_x],[mean_x, -mean_y]])

D = (E/(1-v*v)) * np.mat([[1.,v,0.],[v,1.,0.],[0.,0.,(1-v)/2.]])
Q0 = (1. / a) * (C1.T * D * C1)
Q1 = (1. / a) * (C2.T * D * C1)
Q2 = (1. / a) * (C2.T * D * C2)
E0 = (2. / 3.) * np.bmat([[2. * Q0, Q0], [Q0, 2. * Q0]])
E1 = np.bmat([[-Q1, -Q1], [Q1, Q1]]) - 1. / 3. * np.bmat([[Q0, -Q0], [-Q0, Q0]])
E2 = np.bmat([[Q2, -Q2], [-Q2, Q2]]) + 1. / 3. * np.bmat([[Q0, -Q0], [-Q0, Q0]])
print(E0)

