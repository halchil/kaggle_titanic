import pandas as pd
from sklearn import tree
from sklearn.tree import export_text
import numpy as np
import matplotlib.pyplot as plt

o_train = pd.read_csv('/home/mainte/kaggle_titanic/data/train_fix.csv')
o_test = pd.read_csv('/home/mainte/kaggle_titanic/data/test_fix.csv')

# print(o_train.isnull().sum())
# print(o_test.isnull().sum())

m_target = o_train['Survived'].values
# print(m_target)

m_features_one = o_train[['Pclass', 'Sex', 'Age', 'Fare']].values
# print(m_features_one)

o_my_tree_one = tree.DecisionTreeClassifier()
# print(o_my_tree_one)

# trainでの説明変数と目的変数を代入して、学習させる
# 分類する順番がどう決まるのか気になる
o_my_tree_one = o_my_tree_one.fit(m_features_one, m_target)
# print(o_my_tree_one)

m_test_features = o_test[['Pclass', 'Sex', 'Age', 'Fare']].values
# print(m_test_features)

m_my_prediction = o_my_tree_one.predict(m_test_features)
# print(m_my_prediction)

m_PassengerId = np.array(o_test['PassengerId']).astype(int)
# print(m_PassengerId)

m_my_solution = pd.DataFrame(m_my_prediction,m_PassengerId, columns=['Survived'])
# print(m_my_solution.head(20))

m_my_solution.to_csv('/home/mainte/win_data/my_tree_one.csv', index_label = ['PassengerId'])

'''
# 決定木の詳細を表示します
tree_rules = export_text(o_my_tree_one, feature_names=['Pclass', 'Sex', 'Age', 'Fare'])
# print(tree_rules)

plt.figure(figsize=(100, 50))
tree.plot_tree(o_my_tree_one, feature_names=['Pclass', 'Sex', 'Age', 'Fare'], 
               class_names=['Not Survived', 'Survived'], 
               filled=True, rounded=True)
# plt.show()

plt.savefig('/home/mainte/win_data/decision_tree.png', format='png')
'''