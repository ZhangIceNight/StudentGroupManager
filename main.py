# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import random

def stu27():
    df = pd.read_csv(u'2021级加权平均成绩统计列表.csv', encoding='gbk', error_bad_lines=False)

    # 读取第6列（学生名字）和第8列（序号）
    names = df.iloc[2:, 5].values  # 学生名字
    indices = df.iloc[2:, 7].values  # 序号

    total = len(names)

    step = 25
    l = 0
    groups = [[] for _ in range(step)]

    while (step * (l + 1) < total):
        idx = np.arange(step * l, step * (l + 1))
        y = random.sample(list(idx), step)
        l += 1
        for i in range(step):
            groups[i].append(y[i])

    idx = np.arange(step * l, total)
    y = random.sample(list(idx), total - step * l)
    for i, item in enumerate(y):
        groups[i % step].append(item)

    test = pd.DataFrame()
    col_name = [str(x) for x in range(1, step + 1)]

    for i in range(step):
        ans = list(names[groups[i]])
        if len(groups[i]) != len(groups[0]):
            ans.append('')  # 如果不满，添加空字符串
            groups[i].append('null')
        for j, item in enumerate(ans):
            if ans[j] != '':
                # 使用第8列的序号进行拼接
                original_index = indices[groups[i][j]]  # 直接获取序号
                ans[j] = ans[j] + str(original_index)

        test[col_name[i]] = ans

    test.to_csv(u'./student_teacher_2021.csv', encoding='gbk')

if __name__ == "__main__":
    stu27()
