# -*- coding: utf-8 -*-
'''
@author: Yang Yang
@contact: yanghhu@foxmail.com
@created on: 2020/4/21 20:33
'''
def inputData(file):
    '''
    :param file: the input file of sbfem
    :return:  node, element
    '''
    stemp =[]
    fo = open(file,"r")
    # read node
    dummy = fo.readline()
    nodeNumber = fo.readline()
    for i in range(int(nodeNumber)):
        line = fo.readline()
        temp1 = line.strip('\n')
        temp2 = line.split(',')
        stemp.append(temp2[1:])
    node = [list(map(float,i)) for i in stemp]
    stemp = []

    # read element
    dummy = fo.readline()
    elementNumber = fo.readline()
    for i in range(int(elementNumber)):
        line = fo.readline()
        temp1 = line.strip('\n')
        temp2 = line.split(',')
        stemp.append(temp2[1:])
    element = [list(map(int,i)) for i in stemp]

    return node, element

if __name__ == '__main__':
    node, element = inputData("test.sbinp")
    print (node)
    print (element)
