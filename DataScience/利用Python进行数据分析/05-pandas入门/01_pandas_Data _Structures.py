"""
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
介绍： 熟悉pandas数据结构，参考《利用Python进行数据分析》5.1
"""

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

"""
Series
    包含一个值序列和一个数据标签
    一维的数组型对象
"""
# 默认的index是从0开始的计数
print('Example 1:')
obj = pd.Series([4, 7, -5, 3]) 
print(obj)
#0    4
#1    7
#2   -5
#3    3
#dtype: int64

print('Example 2:')
print(obj.values) # [ 4  7 -5  3]
print(obj.index) # RangeIndex(start=0, stop=4, step=1) 类似于range(4)

print('Example 3:')
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
#d    4
#b    7
#a   -5
#c    3
#dtype: int64
print(obj2.index) # Index(['d', 'b', 'a', 'c'], dtype='object')

print('Example 4:')
print(obj2['a']) # -5
obj2['d'] = 6
print(obj2[['c', 'a', 'd']])
#c    3
#a   -5
#d    6
#dtype: int64

# 使用布尔值数组进行过滤
print('Example 5:')
print(obj2[obj2 > 0])
#d    6
#b    7
#c    3
#dtype: int64

# 数组和标量相乘
print('Example 6:')
print(obj2 * 2)
#d    12
#b    14
#a   -10
#c     6
#dtype: int64

# 应用数学函数
print('Example 7:')
print(np.exp(obj2))
#d     403.428793
#b    1096.633158
#a       0.006738
#c      20.085537
#dtype: float64

print('Example 8:')
print('b' in obj2) # True
print('e' in obj2) # False

# 可以使用字典生成一个Series
print('Example 9:')
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)
#Ohio      35000
#Texas     71000
#Oregon    16000
#Utah       5000
#dtype: int64

# 可以指定索引值生成Series
# NaN表示缺失值
print('Example 10:')
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)
#California        NaN
#Ohio          35000.0
#Oregon        16000.0
#Texas         71000.0
#dtype: float64

# 判断是否有缺失值
# 使用pd.isnull或pd.notnull方法进行判别
print('Example 11:')
print(pd.isnull(obj4)) # 等价于obj4.isnull()
#California     True
#Ohio          False
#Oregon        False
#Texas         False
#dtype: bool
print(pd.notnull(obj4)) # 等价于obj4.notnull()
#California    False
#Ohio           True
#Oregon         True
#Texas          True
#dtype: bool

# 自动对齐
print('Example 12:')
print(obj3)
#Ohio      35000
#Texas     71000
#Oregon    16000
#Utah       5000
#dtype: int64
print(obj4)
#California        NaN
#Ohio          35000.0
#Oregon        16000.0
#Texas         71000.0
#dtype: float64
print(obj3 + obj4) # 多个Series在操作时会自动对齐索引相同的元素
#California         NaN
#Ohio           70000.0
#Oregon         32000.0
#Texas         142000.0
#Utah               NaN
#dtype: float64

# Series对象自身和其索引都有name属性
print('Example 13:')
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)
#state
#California        NaN
#Ohio          35000.0
#Oregon        16000.0
#Texas         71000.0
#Name: population, dtype: float64

# Series的索引可以通过按照位置赋值的方式改变
print('Example 14:')
print(obj)
#0    4
#1    7
#2   -5
#3    3
#dtype: int64
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
#Bob      4
#Steve    7
#Jeff    -5
#Ryan     3
#dtype: int64

"""
DataFrame
    表示矩阵的数据表
    包含已经排序的列集合，每一列可以是不同类型的值(数值，字符串，布尔值等)
    有行索引和列索引，相当于一个共享相同索引的Series的字典
    数据被存储为一个以上的二维块
    对数据的修改都是直接在数据上进行处理,如果需要复制，需要使用Series的copy方法
"""

# 利用包含等长的列表或者NumPy数组的字典创建DataFrame
print('Example 15:')
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)
#    state  year  pop
#0    Ohio  2000  1.5
#1    Ohio  2001  1.7
#2    Ohio  2002  3.6
#3  Nevada  2001  2.4
#4  Nevada  2002  2.9
#5  Nevada  2003  3.2

# head方法将选出头部的前5行
print('Example 16:')
print(frame.head())
#    state  year  pop
#0    Ohio  2000  1.5
#1    Ohio  2001  1.7
#2    Ohio  2002  3.6
#3  Nevada  2001  2.4
#4  Nevada  2002  2.9

# DataFrame可以使用columns指定列的顺序　
print('Example 17:')
print(pd.DataFrame(data, columns=["year", "state", "pop"]))
#   year   state  pop
#0  2000    Ohio  1.5
#1  2001    Ohio  1.7
#2  2002    Ohio  3.6
#3  2001  Nevada  2.4
#4  2002  Nevada  2.9
#5  2003  Nevada  3.2

print('Example 18:')
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2) # 当出现缺失值时，也使用NaN进行填补
#       year   state  pop debt
#one    2000    Ohio  1.5  NaN
#two    2001    Ohio  1.7  NaN
#three  2002    Ohio  3.6  NaN
#four   2001  Nevada  2.4  NaN
#five   2002  Nevada  2.9  NaN
#six    2003  Nevada  3.2  NaN
print(frame2.columns)
# Index(['year', 'state', 'pop', 'debt'], dtype='object')

# 可以类似于字典标记或者属性标记的方式检索DataFrame,生成Series
print('Example 19:')
print(frame2['state']) # 对于任意列名均有效
#one        Ohio
#two        Ohio
#three      Ohio
#four     Nevada
#five     Nevada
#six      Nevada
#Name: state, dtype: object
print(frame2.year) # 只在列名是有效的Python变量名时才有效
#one      2000
#two      2001
#three    2002
#four     2001
#five     2002
#six      2003
#Name: year, dtype: int64

# 通过特殊属性loc可以选取行
print('Example 20:')
print(frame2.loc['three'])
#year     2002
#state    Ohio
#pop       3.6
#debt      NaN
#Name: three, dtype: object

# 可以对列进行赋值
print('Example 21:')
frame2['debt'] =16.5 # 赋值为相同的标量
print(frame2)
#       year   state  pop  debt
#one    2000    Ohio  1.5  16.5
#two    2001    Ohio  1.7  16.5
#three  2002    Ohio  3.6  16.5
#four   2001  Nevada  2.4  16.5
#five   2002  Nevada  2.9  16.5
#six    2003  Nevada  3.2  16.5
frame2['debt'] = np.arange(6.) # 赋值为值数组，其长度需要和DataFrame长度相匹配
print(frame2) 
#       year   state  pop  debt
#one    2000    Ohio  1.5   0.0
#two    2001    Ohio  1.7   1.0
#three  2002    Ohio  3.6   2.0
#four   2001  Nevada  2.4   3.0
#five   2002  Nevada  2.9   4.0
#six    2003  Nevada  3.2   5.0

# 可以将Series赋值给一列，Series将按照DataFrame的索引重新排列
# 空缺处将填写缺失值
print('Example 22:')
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five']) 
frame2['debt'] = val
print(frame2)
#       year   state  pop  debt
#one    2000    Ohio  1.5   NaN
#two    2001    Ohio  1.7  -1.2
#three  2002    Ohio  3.6   NaN
#four   2001  Nevada  2.4  -1.5
#five   2002  Nevada  2.9  -1.7
#six    2003  Nevada  3.2   NaN

# 可以通过布尔值进行赋值　
print('Example 23:')
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)
#       year   state  pop  debt  eastern
#one    2000    Ohio  1.5   NaN     True
#two    2001    Ohio  1.7  -1.2     True
#three  2002    Ohio  3.6   NaN     True
#four   2001  Nevada  2.4  -1.5    False
#five   2002  Nevada  2.9  -1.7    False
#six    2003  Nevada  3.2   NaN    False

# del方法可以删除之前新建的列
print('Example 24:')
del frame2['eastern']
print(frame2)
#       year   state  pop  debt
#one    2000    Ohio  1.5   NaN
#two    2001    Ohio  1.7  -1.2
#three  2002    Ohio  3.6   NaN
#four   2001  Nevada  2.4  -1.5
#five   2002  Nevada  2.9  -1.7
#six    2003  Nevada  3.2   NaN

# 对于包含字典的嵌套字典，外层字典的键将作为列，内层字典的键将作为行索引
print('Example 25:')
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)
#      Nevada  Ohio
#2000     NaN   1.5
#2001     2.4   1.7
#2002     2.9   3.6

# 可以使用.T对DataFrame进行转置
# 转置相当于将原来的DataFrame行列互换
print('Example 26:')
print(frame3.T)
#        2000  2001  2002
#Nevada   NaN   2.4   2.9
#Ohio     1.5   1.7   3.6

# 如果显式指明索引，内部键将不会被排序
# 索引若没有对应值，则将用NaN填充　
print('Example 27:')
frame4 = pd.DataFrame(pop, index=[2001, 2002, 2003])
print(frame4)
#      Nevada  Ohio
#2001     2.4   1.7
#2002     2.9   3.6
#2003     NaN   NaN

# 如果DataFrame的索引和列拥有name属性，则name属性将被显示
print('Example 28:')
frame3.index.name = 'year'; frame3.columns.name = 'state'
print(frame3)
#state  Nevada  Ohio
#year               
#2000      NaN   1.5
#2001      2.4   1.7
#2002      2.9   3.6

# DataFrame的values属性会将包含在DataFrame中的数据以二维ndarray形式返回
print('Example 29:')
print(frame3.values)
#[[nan 1.5]
# [2.4 1.7]
# [2.9 3.6]]

print('Example 30:')
print(frame2.values)
#[[2000 'Ohio' 1.5 nan]
# [2001 'Ohio' 1.7 -1.2]
# [2002 'Ohio' 3.6 nan]
# [2001 'Nevada' 2.4 -1.5]
# [2002 'Nevada' 2.9 -1.7]
# [2003 'Nevada' 3.2 nan]]

"""
索引对象
    索引对象是用于存储轴标签和其他元数据(轴名或者标签)
    索引对象是不可变的
"""
print('Example 31:')
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)
# Index(['a', 'b', 'c'], dtype='object')
# 无法对Index进行赋值，因为索引标签不可变

print('Example 32:')
labels = pd.Index(np.arange(3))
print(labels)
# Int64Index([0, 1, 2], dtype='int64')

print('Example 33:')
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)
#0    1.5
#1   -2.5
#2    0.0
#dtype: float64
print(obj2.index is labels) # True

print('Example 34:')
print(frame3)
#state  Nevada  Ohio
#year               
#2000      NaN   1.5
#2001      2.4   1.7
#2002      2.9   3.6
print(frame3.columns)
# Index(['Nevada', 'Ohio'], dtype='object', name='state')
print('Ohio' in frame3.columns) # True
print(2003 in frame3.index) # False

# 索引对象可以包含重复标签
print('Example 35:')
dup_labels = pd.Index(['foo', 'foo', 'bar', 'bar'])
print(dup_labels)
# Index(['foo', 'foo', 'bar', 'bar'], dtype='object')


