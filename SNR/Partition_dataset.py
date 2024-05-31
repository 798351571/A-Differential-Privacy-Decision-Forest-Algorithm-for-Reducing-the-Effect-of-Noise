import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def DivideDataset(df, num):
    grouped = df.groupby("class")
    split_data = {}
    for name, group in grouped:
        # 将数据分为五个子集
        subgroups = np.array_split(group, num)
        # 将每个子集存储到字典中的相应键中
        for i in range(num):
            if i in split_data:
                split_data[i] = pd.concat([split_data[i], subgroups[i]])
            else:
                split_data[i] = subgroups[i]
    return_list = []
    for i in range(num):
        return_list.append(split_data[i])
    return return_list

if __name__ == '__main__':
    # 示例 DataFrame，假设有 "class" 列
    # data = pd.read_csv('../dataset/mammo.data', sep=',', header=0)
    #
    # # 按 "class" 分组
    # grouped = data.groupby("class")
    #
    # # 计算每个组的大小
    # group_sizes = grouped.size()
    #
    # # 计算划分比例
    # total_samples = len(data)
    # train_ratio = 0.6
    # test_ratio = 0.2
    # validation_ratio = 0.2
    #
    # # 计算每个组的划分数量
    # train_sizes = (group_sizes * train_ratio).astype(int)
    # test_sizes = (group_sizes * test_ratio).astype(int)
    # validation_sizes = (group_sizes * validation_ratio).astype(int)
    #
    # # 创建训练集、测试集和验证集
    # train_data, test_data, validation_data = [], [], []
    # for name, group in grouped:
    #     train, test = train_test_split(group, train_size=train_sizes[name],
    #                                    test_size=test_sizes[name] + validation_sizes[name], random_state=42)
    #     test, validation = train_test_split(test, train_size=test_sizes[name], test_size=validation_sizes[name],
    #                                         random_state=42)
    #     train_data.append(train)
    #     test_data.append(test)
    #     validation_data.append(validation)
    #
    # # 合并数据集
    # train_data = pd.concat(train_data)
    # test_data = pd.concat(test_data)
    # val_data = pd.concat(validation_data)
    #
    # train_data.to_csv('../dataset/train_mammo.csv', index=False)
    # val_data.to_csv('../dataset/val_mammo.csv', index=False)
    # test_data.to_csv('../dataset/test_mammo.csv', index=False)

    import pandas as pd
    import numpy as np

    # 假设你的数据已经加载到一个名为'data'的DataFrame中
    data = pd.read_csv('../dataset/diabetes.csv', sep=',', header=0)
    # 首先，将数据集打乱顺序
    data = data.sample(frac=1, random_state=42)

    # 计算划分比例
    total_samples = len(data)
    train_ratio = 0.8
    val_ratio = 0.2

    # 计算样本数量
    train_samples = int(total_samples * train_ratio)
    val_samples = int(total_samples * val_ratio)

    # 划分数据集
    train_data = data[:train_samples]
    test_data = data[train_samples:train_samples + val_samples]

    # 创建文件夹来存储数据
    import os

    # 将数据保存为CSV文件
    train_data.to_csv('../dataset/train_pima.csv', index=False)
    test_data.to_csv('../dataset/test_pima.csv', index=False)

    print("数据集划分并保存为CSV文件完成。")
