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

# print(null_train_val)

null_test = test.isnull()
null_test_val = null_test.sum()

# print(null_test_val)

#

'''
len_train = len(train) #行数の表示
# print(len_train)

train_null_percent = train.isnull().sum()*100 / len(train) 
test_null_percent = test.isnull().sum()*100 / len(test)
print(train_null_percent)

kesson_table = pd.concat([null_train_val,train_null_percent,null_test_val,test_null_percent], axis=1)
m_kesson_table = kesson_table.rename(columns={0:'欠損数'})

print(m_kesson_table)

'''

# 上記を変数に書き換える
def f_kesson_table(o_df):
    m_null_val = o_df.isnull().sum()
    m_percent = 100 * m_null_val / len(o_df)
    m_kesson_table = pd.concat([m_null_val,m_percent],axis=1)
    m_kesson_table_ren_columns = m_kesson_table.rename(columns={0:'欠損値', 1:'%'})
    return m_kesson_table_ren_columns

print(f'train is {train.shape}')
print(f_kesson_table(train))

print(f'test is {test.shape}')
print(f_kesson_table(test))

# print(train.describe())

# Ageの欠損値は、中央値medianでfillnaする。
train['Age'] = train['Age'].fillna(train['Age'].median())
test['Age'] = test['Age'].fillna(test['Age'].median())
test['Fare'] = test['Fare'].fillna(test['Fare'].median())

# Embarkedは2件欠損があったが、最もおおいSで置き換える
train['Embarked'] = train['Embarked'].fillna('S')


print(f'train is {train.shape}')
print(f_kesson_table(train))

print(f'test is {test.shape}')
print(f_kesson_table(test))

# 文字列を数値に変換する

'''
この書き方は推奨されていない
train["Sex"][train["Sex"] == "male"] = 0
train["Sex"][train["Sex"] == "female"] = 1
train["Embarked"][train["Embarked"] == "S" ] = 0
train["Embarked"][train["Embarked"] == "C" ] = 1
train["Embarked"][train["Embarked"] == "Q"] = 2
'''

# train['Sex'].loc[train['Sex'] == 'male'] = 0
train.loc[train['Sex'] == 'male', 'Sex'] = 0

# train['Sex'].loc[train['Sex'] == 'female'] = 1
train.loc[train['Sex'] == 'female', 'Sex'] = 1

# train['Embarked'].loc[train['Embarked'] == 'S'] = 0
train.loc[train['Embarked'] == 'S', 'Embarked'] = 0
train.loc[train['Embarked'] == 'C', 'Embarked'] = 1
train.loc[train['Embarked'] == 'Q', 'Embarked'] = 2

print(train.head(10))

test.loc[test['Sex'] == 'male', 'Sex'] = 0
test.loc[test['Sex'] == 'female', 'Sex'] = 1

test.loc[test['Embarked'] == 'S', 'Embarked'] = 0
test.loc[test['Embarked'] == 'C', 'Embarked'] = 1
test.loc[test['Embarked'] == 'Q', 'Embarked'] = 2


print(test.head(10))

d_train_fix = pd.DataFrame(train)
d_test_fix = pd.DataFrame(test)

d_train_fix.to_csv('/home/mainte/kaggle_titanic/data/train_fix.csv')
d_test_fix.to_csv('/home/mainte/kaggle_titanic/data/test_fix.csv')