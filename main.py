# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import random

def group_student():
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



def defense_grouping():
    # 读取学生数据
    df = pd.read_csv(u'19级加权平均成绩统计列表.csv', encoding='gbk')
    names = df.iloc[:, 5].values[2:]  # 获取第6列（索引为5）的学生姓名

    # 初始化参数
    total = 194  # 学生总数
    step = 24    # 每次分组的数量
    num_group = 6  # 组的数量
    l = 0  # 计数器
    groups = [[] for _ in range(num_group)]  # 初始化空组列表

    # 随机分组学生
    while step * (l + 1) < total:  # 只要还有足够的学生
        idx = np.arange(step * l, step * (l + 1))  # 当前分组的索引范围
        y = random.sample(list(idx), step)  # 随机抽取学生索引
        l += 1  # 增加计数器
        # 将抽取的学生分配到各个组
        for t in range(num_group):
            groups[t].extend(y[t * (step // num_group):(t + 1) * (step // num_group)])

    # 处理剩余学生
    idx = np.arange(step * l, total)  # 剩余学生的索引
    y = random.sample(list(idx), total - step * l)  # 随机抽取剩余学生
    for i, item in enumerate(y):
        groups[i % num_group].append(item)  # 将剩余学生分配到组中

    # 创建输出 DataFrame
    test = pd.DataFrame()  # 初始化空的 DataFrame
    col_name = [str(i) for i in range(1, num_group + 1)]  # 组的列名

    # 将每组的学生姓名添加到 DataFrame 中
    for i in range(num_group):
        ans = list(names[groups[i]])  # 获取当前组的学生姓名
        if len(groups[i]) != len(groups[0]):  # 确保每组长度一致
            ans.append('')  # 如果组长度不一致，添加空字符串
        test[col_name[i]] = ans  # 将学生姓名存入 DataFrame

    print(test)  # 打印分组结果
    # test.to_csv(u'./group.csv', encoding='gbk', index=False)  # 保存结果到 CSV 文件

if __name__ == "__main__":
    group_student()
    # defense_grouping()
