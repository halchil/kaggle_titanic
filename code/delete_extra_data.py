# パッケージの読み込み
import numpy as np
import pandas as pd

# csvデータの取り込み(これは抽象的なオブジェクトのため、表示などはできない)
train = pd.read_csv("/home/mainte/kaggle_titanic/data/train.csv")
test = pd.read_csv("/home/mainte/kaggle_titanic/data/test.csv")

#データの大きさ表示
'''
print(train.shape)
print(test.shape)
print("===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ")
'''
# データの代表的な値を表示
'''
print(train.describe())
print("===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ")
print(test.describe())
'''

# データの欠損の確認

null_train = train.isnull() # 各要素に対して判定を行い、欠損値NaNであればTrue、欠損値でなければFalse
null_train_val = null_train.sum()

print(null_train_val)

null_test = test.isnull()
null_test_val = null_test.sum()

print(null_test_val)

#

len_train = len(train) #行数の表示
print(len_train)

train_null_percent = train.isnull().sum()*100 / len(train) 
print(train_null_percent)
