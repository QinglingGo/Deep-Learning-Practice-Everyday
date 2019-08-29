"""
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.37
介绍： numpy的axis用法详解
参考： https://blog.csdn.net/sky_kkk/article/details/79725646
"""

import numpy as np

"""
一维数组:axis=0
二维数组:axis=0,1
N维数组:axis=0,1,N-1

axis=0对应最外层[]
axis=1对应第二外层[]
aixs=N-1对应第N-1外层(最内层)[]
"""

"""
axis = 0表示对最外层[]里的最大单位块做块与块之间的运算,同时移除最外层[]
"""
a = np.array([1,2,3])
print(a.sum(axis=0)) 
# 6
# 因为只有一层[]，所以直接对最大单位块1,2,3进行运算
# 运算结果是[6],去掉最外层[]后，输出结果是6

a = np.array([[1,2],[3,4]])
print(a.sum(axis=0)) 
# [4 6]
# 有2层[],最外层[]中的最大单位块为[1,2],[3,4]
# [1,2]+[3,4]=[4,6]
# 运算结果是[[4 6]],去掉最外层[]后，输出结果是[4 6]

a = np.array([[[1,2],[3,4]],[[11,12],[13,14]]])
print(a.sum(axis=0)) 
# [[12 14]
# [16 18]]
# 有三层[]，最外层[]中的最大单位块为[[1,2],[3,4]],[[11,12],[13,14]]
# [[1,2],[3,4]]+[[11,12],[13,14]]=[[12,14],[16,18]]
# 去掉最外层[]的输出结果是[[12 14][16 18]]

"""
axis = 1表示对第二外层[]里的最大单位块做块与块之间的运算,同时移除第二外层[]
"""
a = np.array([1,2,3])
#print(a.sum(axis=1))
# numpy.AxisError: axis 1 is out of bounds for array of dimension 1
# 因为只有一层[]，axis只能为0,所以会报错

a = np.array([[1,2],[3,4]])  
print(a.sum(axis = 1))
# [3 7]
# 有两层[],第二外层[]的最大单位块有两组，分别为1,2和3,4
# 分别对两组进行运算，第一个单位块的结果:1+2=3;第二个单位块的结果:3+4=7
# 运算结果为[[3][7]]，但移除第二外层[]后，输出结果为[3 7]

a = np.array([[[1,2],[3,4]],[[11,12],[13,14]]])
print(a.sum(axis=1))
# [[ 4  6]
# [24 26]]
# 有三层[],第二外层[]的最大单位块有2组：[1,2],[3,4]和[11,12],[13,14]
# 分别进行运算,[1,2]+[3,4]=[4,6];[11,12]+[13,14]=[24,26]
# 运算结果为[[[4 6][24 26]]],移除第二层[]后，输出结果为[[4 6][24 26]]