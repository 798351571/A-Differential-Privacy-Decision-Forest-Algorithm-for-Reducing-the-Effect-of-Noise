from sklearn.preprocessing import LabelEncoder
import pandas as pd

# 创建一个示例 DataFrame
data = pd.read_csv('../dataset/diabetes.csv', sep=',', header=0)

# 初始化 LabelEncoder
label_encoder = LabelEncoder()
# for key in data.columns:
data["class"] = label_encoder.fit_transform(data["class"])
print(data)
data.to_csv('../dataset/diabetes.csv', index=False)