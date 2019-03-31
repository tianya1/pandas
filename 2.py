import pandas as pd
s = pd.Series([7,-3,4,-2])   s2 = pd.Series([7,-3,4,-2], index=['d','b','a','c'])
pd.Series(5, index=list('abcde'))  pd.Series({2:'a',1:'b',3:'c'}, index=[3,2])

s.dtype
s.values
s.index    设置值  s.index = ['a','b','c','d']

获取
s2['a']
s2[['c','a','d']]
s2[s2>0]
s2*2

in not in
isnull notnull

dic = {'beijing':35000,'shanghai':71000,'guangzhou':16000,'shenzhen':5000}
s3=pd.Series(dic)
s3.keys()
 s3.items()
 list(s3.items())


 f=pd.DataFrame(data)     pd.DataFrame(data, columns=['year','state','pop'])
 pd.DataFrame(data, columns=['year','state','pop'],index=['a','b','c','d','e','f'])
 f.columns
 f.index
  f.dtypes
  f.values

  f2.loc['a']  行
  f2['year']   列
  f2['debt'] = val  追加列
  df.append(df1)    追加行
  del f2['new']     删除行

  f2.T
   f2.index.name = 'order';f2.columns.name='key'
    f2.values

  obj.reindex(list('abcde'))  重建索引


  df.drop('two',axis = 1)  # 指定删除列，而不是默认的行

  核心思维：在DataFrame中，优先按列操作！
  切片的时候居然是按行进行！

  df.loc['b', ['two','four']]  # 使用显式索引值，用逗号分隔行和列参数
  df.loc['b':, 'two':'four']  # 切片方式，注意区间
  df.iloc[2, [3, 0, 1]]
  df.iloc[2]

  df.iloc[行][列]

  apply()是整行整列的操作，applymap()是逐一对每个元素进行操作。
####################

