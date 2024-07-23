# パッケージの読み込み

import numpy as np
import pandas as pd

# csvデータの取り込み(これは抽象的なオブジェクトのため、表示などはできない)
train = pd.read_csv("/home/mainte/kaggle_titanic/data/train.csv")
test = pd.read_csv("/home/mainte/kaggle_titanic/data/test.csv")

print(train.head()) #trainオブジェクトの最初の10行を表示
print("----- ----- ----- ----- ----- ----- ----- ----- ----- -----")
print(test.head())