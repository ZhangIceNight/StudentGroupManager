# -*- coding: utf-8 -*-
from tokenize import group
import pandas as pd
import numpy as np
import random
df =pd.read_csv(u'19级加权平均成绩统计列表.csv', encoding='gbk')

names = df.iloc[:,5].values[2:]
step = 24
l=0

groups = []
for i in range(step):
    groups.append([])

while(step*(l+1)<194):
    idx = np.arange(step*l,step*(l+1))
    y = random.sample(list(idx),step)
    l=l+1
    for i in range(step):
        groups[i].extend(y[i:i+1])

idx = np.arange(step*l,194)
y = random.sample(list(idx),194-step*l)
for i, item in enumerate(y):
    groups[i%6].append(item)

test = pd.DataFrame()
col_name=[]
for x in np.arange(1,step+1):
    col_name.append(str(x))
for i in range(step):
    ans = list(names[groups[i]])
    if len(groups[i]) != len(groups[0]):
        ans.append('')
    test[col_name[i]] = ans
print(test)
# test.to_csv(u'./res.csv', encoding='gbk')
