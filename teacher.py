# -*- coding: utf-8 -*-
from tokenize import group
import pandas as pd
import numpy as np
import random
def _print(item):
    print(item)
    exit(0)
df =pd.read_csv(u'教师.csv', encoding='gbk')
names = df.iloc[:,1].values
zhicheng = df.iloc[:,2].values
jiao_fujiao = 16
jiangshi = 11

total = 194
step = 24
num_group = 6
l=0
groups = [[],[],[],[],[],[]]
zuzhang_group = []
mishu_group = []

#pick zuzhang
idx = np.arange(0,jiao_fujiao)
y = random.sample(list(idx),num_group)
for i, item in enumerate(y):
    groups[i%num_group].append(item)
    zuzhang_group.append(item)
#pick mishu
idx = np.arange(jiao_fujiao,jiao_fujiao+jiangshi)
y = random.sample(list(idx),num_group)
for i, item in enumerate(y):
    groups[i%num_group].append(item)
    mishu_group.append(item)

# get left teacher
left = []
for i in range(len(names)):
  if not i in zuzhang_group:
    if not i in mishu_group:
      left.append(i)

# put the left in groups
y = random.sample(list(left),len(left))
for i, item in enumerate(y):
    groups[i%num_group].append(item)




test = pd.DataFrame()
col_name = []
for i in range(1,num_group+1):
    col_name.append(str(i))
# col_name = ['第一组', '第二组','第三组','第四组','第五组','第六组']
for i in range(num_group):
    ans = list(names[groups[i]])
    if len(groups[i]) != len(groups[0]):
        ans.append('')
    test[col_name[i]] = ans
print(test)
# test.to_csv(u'./group.csv', encoding='gbk', index=False)
