# -*- coding: utf-8 -*-
from tokenize import group
import pandas as pd
import numpy as np
import random
df =pd.read_csv(u'19级加权平均成绩统计列表.csv', encoding='gbk')

names = df.iloc[:,5].values[2:]
total = 194
step = 24
num_group = 6
l=0
groups = [[],[],[],[],[],[]]



while(step*(l+1)<total):
    idx = np.arange(step*l,step*(l+1))
    y = random.sample(list(idx),step)
    l=l+1
    for t in range(num_group):

        groups[t].extend(y[t*(step//num_group):(t+1)*(step//num_group)])

idx = np.arange(step*l,total)
y = random.sample(list(idx),total-step*l)
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
