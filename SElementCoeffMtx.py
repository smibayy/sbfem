# -*- coding: utf-8 -*-
'''
@author: Yang Yang
@contact: yanghhu@foxmail.com
@created on: 2020/4/19 21:12
'''
import numpy as np
from EleCoeff2NodeEle import *
from input import *
def SElementCoeffMtx(node, conn, E, V):
    '''
    :param node:
    :param conn:
    :param E:
    :param V:
    :return:
    '''
    nd = 2 * len(node)
    E0 = np.zeros((nd, nd))
    E1 = np.zeros((nd, nd))
    E2 = np.zeros((nd, nd))
    M0 = np.zeros((nd, nd))

    ele = []
    dof = []
    for ie in range(len(conn)):
        ele.append(node[conn[ie][0]-1])
        ele.append(node[conn[ie][1]-1])
        dof.append(2 * conn[ie][0] - 1)
        dof.append(2 * conn[ie][0])
        dof.append(2 * conn[ie][1] - 1)
        dof.append(2 * conn[ie][1])
        ee0, ee1, ee2 = EleCoeff2NodeEle(ele, E, V)
        # assembly E0, E1, E2
        for i in range(len(ee0)):
            for j in range(len(ee0)):
                E0[dof[i]-1][dof[j]-1] += ee0[i,j]

        for i in range(len(ee1)):
            for j in range(len(ee1)):
                E1[dof[i]-1][dof[j]-1] += ee1[i,j]

        for i in range(len(ee2)):
            for j in range(len(ee2)):
                E2[dof[i]-1][dof[j]-1] += ee2[i,j]
        ele = []
        dof = []

    return E0, E1, E2

if __name__ == '__main__':
    node, ele = inputData("test.sbinp")
    E = 10.
    v = 0.
    E0, E1, E2 = SElementCoeffMtx(node, ele, E, v)
    Pf = 1./np.sqrt(np.diag(E0))
    P = np.diag(Pf)
    E0 = np.dot(np.dot(P,E0),P)
    E1 = np.dot(np.dot(P,E1),P)
    E2 = np.dot(np.dot(P,E2),P)
    s1 = -np.dot(np.linalg.inv(E0), E1.T)
    s2 = np.linalg.inv(E0)
    s3 = E2 - np.dot(np.dot(E1,np.linalg.inv(E0)),E1.T)
    s4 = np.dot(E1, np.linalg.inv(E0))
    Zp = np.bmat([[s1, s2],[s3, s4]])
    # print (Zp)
    eignvalue, featurevector = np.linalg.eig(Zp)
    # print (eignvalue)
    a = np.diag(eignvalue)
    print(a)







