import pandas as pd

# 读取数据文件（假设文件名为 data.csv）
data = pd.read_csv('Input/diabetes.csv')

# 提取第一列的数据
first_column_data = data.iloc[:, 0]

# 删除第一列的数据
data = data.drop(data.columns[0], axis=1)

# 将第一列的数据添加到最后一列
data['New_Column_Name'] = first_column_data

# 保存新数据文件
data.to_csv('Input/diabetes.csv', index=False)
