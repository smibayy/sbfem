# -*- coding: utf-8 -*-
'''
@author: Yang Yang
@contact: yanghhu@foxmail.com
@created on: 2020/4/21 13:00
'''
import numpy as np
def SElementSlnEigenMethod(E0, E1, E2, M0):
    nd = len(E0)
    id = np.linspace(1, nd, nd)

    # Preconditioning
    Pf = 1./np.sqrt(np.diag(E0))
    P = np.diag(Pf)
    E0 = np.dot(np.dot(P,E0),P)
    E1 = np.dot(np.dot(P,E1),P)
    E2 = np.dot(np.dot(P,E2),P)

    # Construct Zp
    s1 = -np.dot(np.linalg.inv(E0), E1.T)
    s2 = np.linalg.inv(E0)
    s3 = E2 - np.dot(np.dot(E1,np.linalg.inv(E0)),E1.T)
    s4 = np.dot(E1, np.linalg.inv(E0))
    Zp = np.bmat([[s1, s2],[s3, s4]])

    # eigenvalues and eigenvectors of Zp
    eignvalue, featurevector = np.linalg.eig(Zp)
#TODO: T continue




if __name__ == '__main__':
    pass
