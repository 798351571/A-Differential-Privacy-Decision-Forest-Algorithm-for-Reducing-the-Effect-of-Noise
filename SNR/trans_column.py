import pandas as pd

# 读取数据文件
data = pd.read_csv('../dataset/diabetes.csv')

# 获取列名
columns = data.columns.tolist()

# 将最后一列的名称移动到列表的开头
columns.insert(0, columns.pop())

# 重新排列 DataFrame 的列
data = data[columns]

# 保存到新的文件（如果需要）
data.to_csv('../dataset/diabetes.csv', index=False)
