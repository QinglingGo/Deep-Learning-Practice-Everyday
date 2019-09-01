# Deep Learning Practice Everyday

本项目是对于机器学习和深度学习自学知识的总结，会持续更新。

其中 ***[Issues](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/issues)*** 板块将更新一些学习笔记和总结的内容。

|分类|标签|
|:--: |:--: |
|领域|[Data Science](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/labels/Data%20Science)<br>[Deep Learning](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/labels/Deep%20Learning)<br>[Machine Learning](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/labels/Machine%20Learning)<br>[Math](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/labels/Math)|
|工具|[Numpy](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/labels/NumPy)<br>[sklearn](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/labels/sklearn)|
|类别|[Summary](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/labels/Summary)|
|书籍|[Book-Statistical Learning Method](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/labels/Book-Statistical%20Learning%20Method)|

## 1 机器学习

### 1.1 《机器学习实战》

机器学习算法，主要参考《机器学习实战》。

其他参考资料：

[Jack Cui的博客](https://github.com/Jack-Cherish/Machine-Learning)

[ApacheAI的讲解【强烈推荐】](https://github.com/apachecn/AiLearning#1%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0---%E5%9F%BA%E7%A1%80)

|章节|内容|
| :--: |:--: |
|[kNN](https://github.com/apachecn/AiLearning/blob/master/docs/ml/2.k-%E8%BF%91%E9%82%BB%E7%AE%97%E6%B3%95.md)|[【简单kNN】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Machine%20Learning/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%AE%9E%E6%88%98/01-KNN/01-%E7%AE%80%E5%8D%95kNN)<br>[【约会网站数据分析】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Machine%20Learning/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%AE%9E%E6%88%98/01-KNN/02-%E7%BA%A6%E4%BC%9A%E7%BD%91%E7%AB%99%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90)<br>[【手写数字识别】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Machine%20Learning/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%AE%9E%E6%88%98/01-KNN/03-%E6%89%8B%E5%86%99%E6%95%B0%E5%AD%97%E8%AF%86%E5%88%AB)|
|[Decision Tree](https://github.com/apachecn/AiLearning/blob/master/docs/ml/3.%E5%86%B3%E7%AD%96%E6%A0%91.md)|[【贷款发放】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Machine%20Learning/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E5%AE%9E%E6%88%98/02-Decision%20Tree/01-%E8%B4%B7%E6%AC%BE%E5%8F%91%E6%94%BE)【190708：补全基本代码，待进一步理解原理，待学习决策树可视化】|

### 1.2 《统计学习方法》

参考李航2012版本《统计学习方法》，作为《机器学习实战》的理论补充。

|章节|内容|
| :--: |:--: |
|第1章－统计学习方法概论|[【笔记】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/issues/7)<br>[【代码】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Machine%20Learning/%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95/01-%E7%BB%9F%E8%AE%A1%E5%AD%A6%E4%B9%A0%E6%96%B9%E6%B3%95%E6%A6%82%E8%AE%BA)|

## 2 深度学习

### 2.1 [《python深度学习》](https://github.com/fchollet/deep-learning-with-python-notebooks)

keras开发者编写，介绍利用keras进行深度学习模型构建和训练。

|项目|内容|
| :--: |:--: |
|[MNIST](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/python%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/01-MNIST)|MNIST是手写数字数据集，每张图是28×28的灰度图;使用模型对手写数字数据集进行分类|
|[IMDB](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/python%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/02-IMDB)|IMDB来自电影数据库，是影评数据集;使用模型对影评数据集进行情感分类|
|[路透社新闻分类](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/python%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/03-%E8%B7%AF%E9%80%8F%E7%A4%BE%E6%96%B0%E9%97%BB%E5%88%86%E7%B1%BB)| Reuters数据集是新闻的多分类文本数据集，有46个主题;使用模型对新闻主题进行分类|
|[波士顿房价预测](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/python%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/04-%E6%B3%A2%E5%A3%AB%E9%A1%BF%E6%88%BF%E4%BB%B7%E9%A2%84%E6%B5%8B)|波士顿房价预测数据包含404个训练样本，102个测试样本;使用模型对波士顿房价进行预测|
|[猫狗图像分类](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/python%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/05-%E7%8C%AB%E7%8B%97%E5%9B%BE%E5%83%8F%E5%88%86%E7%B1%BB)|猫狗数据集是kaggle竞赛的数据集，包含25000张图片，其中每一类各有12500张图片;使用模型对猫狗类别进行分类|
|[Jena温度预测](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/python%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/06-Jena%E6%B8%A9%E5%BA%A6%E9%A2%84%E6%B5%8B)|Jena气象数据是每10分钟记录与气象有关的14个不同的量值。使用模型对Jena地区的温度进行预测|
|[LSTM文本生成](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/python%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/07-LSTM%E6%96%87%E6%9C%AC%E7%94%9F%E6%88%90)|学习尼采的作品，生成具有尼采风格的文字|
|[DeepDream](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/python%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/08-DeepDream)|利用ImageNet上的预训练网络，实现DeepDream效果。|
|[可视化CNN](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/python%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0/09-%E5%8F%AF%E8%A7%86%E5%8C%96CNN)|可视化CNN的中间输出（中间激活）<br>可视化CNN的过滤器<br>可视化图像中类激活的热力图|

### 2.２《深度学习之TensorFlow》

TensorFlow框架学习

|项目|内容|
| :--: |:--: |
|[线性回归](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E4%B9%8BTensorFlow/01-%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92)|使用TensorFlow进行线性回归|
|[MNIST](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E4%B9%8BTensorFlow/02-MNIST)|使用最简单的机器学习模型--单一softmax regression对MNIST进行分类,主要目的是熟悉TensorFlow的执行流程|
|[softmax算法与损失函数](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E4%B9%8BTensorFlow/03-softmax%E7%AE%97%E6%B3%95%E4%B8%8E%E6%8D%9F%E5%A4%B1%E5%87%BD%E6%95%B0)|使用softmax计算loss|
|[退化学习率](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E4%B9%8BTensorFlow/04-%E9%80%80%E5%8C%96%E5%AD%A6%E4%B9%A0%E7%8E%87)|使用退化学习率，在训练速度和精度之间找到平衡|
|[线性分类](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Deep%20Learning/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E4%B9%8BTensorFlow/05-%E7%BA%BF%E6%80%A7%E5%88%86%E7%B1%BB)|线性单分类和线性多分类问题分析|

## 3 数据处理

### 3.1 [《利用Python进行数据分析》](https://github.com/wesm/pydata-book)

强烈推荐，由浅入深介绍数据处理常用的工具，并且例子非常清晰易懂。

主要包括利用Pandas, Numpy等科学计算工具包进行数据分析。

|章节|内容|
| :--: |:--: |
|[Python内建数据结构](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/001-Python%E5%86%85%E5%BB%BA%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84)|[【元组】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/001-Python%E5%86%85%E5%BB%BA%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/01_Tuple.py)<br>[【列表】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/001-Python%E5%86%85%E5%BB%BA%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/02_List.py)<br>[【内建函数】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/001-Python%E5%86%85%E5%BB%BA%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/03_Built-in_Sequence_Functions.py)<br>[【字典】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/001-Python%E5%86%85%E5%BB%BA%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/04_Dictionary.py)<br>[【集合】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/001-Python%E5%86%85%E5%BB%BA%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/05_Set.py)<br>[【推导式】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/001-Python%E5%86%85%E5%BB%BA%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/06_Comprehensions.py)<br>[【总结：常用集合元素操作】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/001-Python%E5%86%85%E5%BB%BA%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84#%E5%B8%B8%E7%94%A8%E9%9B%86%E5%90%88%E5%85%83%E7%B4%A0%E6%93%8D%E4%BD%9C)|
|[Python函数](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/002-Python%E5%87%BD%E6%95%B0)|[【基本用法】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/002-Python%E5%87%BD%E6%95%B0/01_Basic.py)<br>[【Lambda】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/002-Python%E5%87%BD%E6%95%B0/02_Lambda.py)<br>[【科里化】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/002-Python%E5%87%BD%E6%95%B0/02_Lambda.py)<br>[【生成器】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/002-Python%E5%87%BD%E6%95%B0/04_Generators.py)|
|[文件操作](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/003-%E6%96%87%E4%BB%B6%E6%93%8D%E4%BD%9C)|[【总结：常见文件操作】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/003-%E6%96%87%E4%BB%B6%E6%93%8D%E4%BD%9C#%E5%B8%B8%E8%A7%81%E6%96%87%E4%BB%B6%E6%93%8D%E4%BD%9C)<br>[【总结：Python文件模式】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/003-%E6%96%87%E4%BB%B6%E6%93%8D%E4%BD%9C#python%E6%96%87%E4%BB%B6%E6%A8%A1%E5%BC%8F)|
|[NumPy基础](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80)|[【ndarray操作】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80/01_ndarray.py)<br>[【使用数组进行面向对象编程】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80/03_Array_Oriented_Programming.py)<br>[【使用数组进行文件输入输出】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80/04_File_Input_and_Output_with_Arrays.py)<br>[【线性代数】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80/05_%20Linear_Algebra.py)<br>[【伪随机数生成】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80/06_Pseudorandom_Number_Generation.py)<br>[【随机漫步】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80/07_Random_Walks.py)<br>[【总结：数组生成函数】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80#%E6%95%B0%E7%BB%84%E7%94%9F%E6%88%90%E5%87%BD%E6%95%B0)<br>[【总结：一元通用函数】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80#%E4%B8%80%E5%85%83%E9%80%9A%E7%94%A8%E5%87%BD%E6%95%B0)<br>[【总结：二元通用函数】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80#%E4%BA%8C%E5%85%83%E9%80%9A%E7%94%A8%E5%87%BD%E6%95%B0)<br>[【总结：基础数组统计方法】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80#%E5%9F%BA%E7%A1%80%E6%95%B0%E7%BB%84%E7%BB%9F%E8%AE%A1%E6%96%B9%E6%B3%95)<br>[【总结：数组的集合操作】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80#%E6%95%B0%E7%BB%84%E7%9A%84%E9%9B%86%E5%90%88%E6%93%8D%E4%BD%9C)<br>[【总结：常用numpy.linalg函数】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80#%E5%B8%B8%E7%94%A8numpylinalg%E5%87%BD%E6%95%B0)<br>[【总结：numpy.random中部分函数列表】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/004-NumPy%E5%9F%BA%E7%A1%80#numpyrandom%E4%B8%AD%E9%83%A8%E5%88%86%E5%87%BD%E6%95%B0%E5%88%97%E8%A1%A8)|
|[pandas入门](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/005-pandas%E5%85%A5%E9%97%A8)|[【pandas数据结构】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/blob/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/005-pandas%E5%85%A5%E9%97%A8/01_pandas_Data%20_Structures.py)<br>[【总结：DataFrame构造函数的有效输入类型】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/005-pandas%E5%85%A5%E9%97%A8#dataframe%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0%E7%9A%84%E6%9C%89%E6%95%88%E8%BE%93%E5%85%A5)<br>[【总结：一些索引对象的方法和属性】](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/tree/master/Data%20Science/%E5%88%A9%E7%94%A8Python%E8%BF%9B%E8%A1%8C%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90/005-pandas%E5%85%A5%E9%97%A8#%E4%B8%80%E4%BA%9B%E7%B4%A2%E5%BC%95%E5%AF%B9%E8%B1%A1%E7%9A%84%E6%96%B9%E6%B3%95%E5%92%8C%E5%B1%9E%E6%80%A7)|

## ４ 学习笔记

|类别|内容|
| :--: |:--: |
|深度学习|[激活函数总结](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/issues/1)<br>[损失函数总结](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/issues/3)|
|NumPy|[np.random函数总结](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/issues/4)<br>[NumPy中axis用法解析](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/issues/6)|
|sklearn|[OneHotEncoder用法解析](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/issues/5)|
|Math|[分类模型评估指标总结](https://github.com/huuuuusy/Deep-Learning-Practice-Everyday/issues/8)|
