# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2019-03-30 15:11:19
# @Last Modified by:   Marte
# @Last Modified time: 2019-03-30 15:32:14


import numpy as np

import pandas as pd

f=pd.read_csv('e:/python_29/3/data.csv',header=None)

#print(f)

a=f[f>0]

#print(a.count())

b=f.sum()/a.count()  #按列

c=b.sort_values()

print(list(c.index))

###############

a1=[]
for i in range(10):
    temp=[]
    for j in range(10):
        x=f[f[i]<f[j]].count()[0]
        y=0
        for k in range(10):
            y=y+f[f[i]<f[k]].count()[0]
        temp.append(x/y)
    a1.append(temp)

res= pd.DataFrame(a1)

####################

a2=[]
for i in range(10):
    temp=[]
    for j in range(10):
        x=f[f[i]>f[j]].count()[0]
        y=0
        for k in range(10):
            y=y+f[f[i]>f[k]].count()[0]
        temp.append(x/y)
    a2.append(temp)

res1= pd.DataFrame(a2)

res_=1.087*res-0.087*res1


##################

test=np.zeros((10,10))
for k in range(10):
    temp=f.loc[k]>=f.mean(axis='columns')[k]
    res=temp[list(temp)].index
    val=np.zeros((10,10))
    for i in range(10):
        for j in range(10):
            if (i in res) and (j in res) or (i==j):
                val[i][j]=1
    test+=val

test=pd.DataFrame(test)

######################


test1=np.zeros((10,10))
for i in range(10):
    temp=f.loc[i]>=f.mean(axis='columns')[i]
    res=temp[list(temp)].count()
    val=0
    for j in range(res):
        val+=np.log2(res)*test[i][j]
    val=1/val
    test1[i][i]=val

test1=pd.DataFrame(test1)

######################

test2=np.dot(test1,test)
test2_=pd.DataFrame(test2)

test3=np.dot(res_,test2_)
test3_=pd.DataFrame(test3)

####################
#第二位用户为例子

sumval=np.zeros((10,))
temp=f.loc[2]>=f.mean(axis='columns')[2]
res=temp[list(temp)].index
for i in res:
    t=f[2][i]*(test3_.iloc[i])
    sumval+=t

fval=sumval.sort_values(ascending = False)[:4].index

print(fval)  #即为推荐列表

