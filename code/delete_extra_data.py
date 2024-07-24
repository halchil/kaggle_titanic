# パッケージの読み込み
import numpy as np
import pandas as pd

# csvデータの取り込み(これは抽象的なオブジェクトのため、表示などはできない)
train = pd.read_csv("/home/mainte/kaggle_titanic/data/train.csv")
test = pd.read_csv("/home/mainte/kaggle_titanic/data/test.csv")

#データの大きさ表示
print(train.shape)
print(test.shape)
print("===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ")

# データの代表的な値を表示
print(train.describe)
print("===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ")
print(test.describe)