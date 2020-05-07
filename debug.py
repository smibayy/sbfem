# -*- coding: utf-8 -*-
'''
@author: Yang Yang
@contact: yanghhu@foxmail.com
@created on: 2020/5/7 14:10
'''
def outputData(data,fileName):
    fo=open(fileName,"w")
    for i in range(len(data)):
        for j in range(len(data[0])):
            fo.write(str("%.3f"%data[i][j]))
            fo.write("\t")
        fo.write("\n")
    fo.close()

def outputData1(data,fileName):
    fo=open(fileName,"w")
    for i in range(len(data)):
        for j in range(len(data[0])):
            fo.write(str("%.3f"%data[i]))
            fo.write("\t")
        fo.write("\n")
    fo.close()
