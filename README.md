![logo](./fig/titanic-logo.png)

## はじめに

Pythonはprint程度、numpy,pandasはインストールくらいの方に向けて、1つ1つ丁寧に確認する。

各ステップごとに、その状態のcodeを保存して積み上げていくイメージで作成していく。

後でコードを読み返すと1から読み返すくらい工数がかかる。
しかも、実践したことも忘れてることが多い。  
そうなると、やってきた実感もわかないというところで、コーディングを先延ばしにしている。

今回は、そんな体質の人ために、1つ1つ積み上げていく実感を持つことで各ステップを記載していく。

## 参考文献
[Kaggle Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic)
[Codexa タイタニック号で生き残るのは誰？](https://www.codexa.net/kaggle-titanic-beginner/)

## 前提条件
Ubuntu
Python3 がインストール済
Python仮想環境について、頭で利用方法をイメージできる
numpyインストール済
pandasインストール済

## データの取得
まず、KaggleのCompetitionにアクセスしてデータを取得する。  

![logo](./fig/fig1.png)

## データを見てみる
とりあえず、CSVを開いて見てみる。
概要は以下。  

![logo](./fig/fig2.png)

## Loading and Displaying CSV
まず、こちらのCSVファイルをUbuntuサーバに格納する。
その後、Pythonコードで読み込み、表示させる。

### Python側にディレクトリ作成
今回の作業を行う用のディレクトリを作成する。
丁寧に作業をしていきたいので、1つ1つ確認しながら進めていきたい。

```
[実行コマンド]
mkdir /home/mainte/kaggle_tiganic

[ディレクトリ移動コマンド]
cd /home/mainte/kaggle_titanic
```

### csvファイルを保存する
ローカルPCでVMwareを使ってUbuntuサーバを立てているので、WinSCPかマウントすることでデータを転送する。
まず、カレントディレクトリ(/home/mainte/kaggle_titanic)内で「data」ディレクトリを作成。

今回、マウントポイントが/home/mainte/win_data/titanic である。
```
[実行コマンド]
ll /home/mainte/win_data/titanic/

[結果]
-rwxrwx--- 1 root vboxsf  3258 Jul 20 05:32 gender_submission.csv*
-rwxrwx--- 1 root vboxsf 28629 Jul 20 05:32 test.csv*
-rwxrwx--- 1 root vboxsf 61194 Jul 20 05:34 train.csv*
```
であり、これを今回利用するディレクトリにコピーする。

```
[実行コマンド]
cp -r /home/mainte/win_data/titanic/* /home/mainte/kaggle_titanic/data/


[確認コマンド]
ll /home/mainte/kaggle_titanic/data/

[結果]
-rwxrwx--- 1 root vboxsf  3258 Jul 20 05:32 gender_submission.csv*
-rwxrwx--- 1 root vboxsf 28629 Jul 20 05:32 test.csv*
-rwxrwx--- 1 root vboxsf 61194 Jul 20 05:34 train.csv*
```

また、現在、rootユーザもしくはvboxsfグループに所属しているユーザ以外はデータを参照できない。
そのため、ファイルの参照権限を変更する。
```
[実行コマンド]
chmod 777 /home/mainte/kaggle_titanic/data/*

[確認コマンド]
ll /home/mainte/kaggle_titanic/data/

[結果]
-rwxrwxrwx 1 mainte mainte  3258 Jul 23 12:29 gender_submission.csv*
-rwxrwxrwx 1 mainte mainte 28629 Jul 23 12:29 test.csv*
-rwxrwxrwx 1 mainte mainte 61194 Jul 23 12:29 train.csv*

```

### display csv

csvを表示するプログラムはこちら、[display_csv.py](./code/display_csv.py)

```
[実行コマンド]
git clone https://github.com/halchil/kaggle_titanic.git

[結果]
Cloning into 'kaggle_titanic'...
remote: Enumerating objects: 52, done.
remote: Counting objects: 100% (52/52), done.
remote: Compressing objects: 100% (35/35), done.
remote: Total 52 (delta 10), reused 48 (delta 9), pack-reused 0
Receiving objects: 100% (52/52), 427.37 KiB | 240.00 KiB/s, done.
Resolving deltas: 100% (10/10), done.
ll /home/mainte/kaggle_titanic/kaggle_titanic/code/display_csv.py 
-rw-rw-r-- 1 mainte mainte 473 Jul 23 13:46 /home/mainte/kaggle_titanic/kaggle_titanic/code/display_csv.py
```
仮想環境に入る。

```
[実行コマンド]
source myenv/bin/activate

[確認コマンド]
echo $VIRTUAL_ENV

[結果]
/home/mainte/myenv

```
`pip list`コマンドで利用可能なパッケージを表示してもいいが、さっそくPyhonのコードを実行する。

```
[実行コマンド]
python3 /home/mainte/kaggle_titanic/kaggle_titanic/code/display_csv.py 

[結果]
   PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
----- ----- ----- ----- ----- ----- ----- ----- ----- -----
   PassengerId  Pclass                                          Name     Sex   Age  SibSp  Parch   Ticket     Fare Cabin Embarked
0          892       3                              Kelly, Mr. James    male  34.5      0      0   330911   7.8292   NaN        Q
1          893       3              Wilkes, Mrs. James (Ellen Needs)  female  47.0      1      0   363272   7.0000   NaN        S
2          894       2                     Myles, Mr. Thomas Francis    male  62.0      0      0   240276   9.6875   NaN        Q
3          895       3                              Wirz, Mr. Albert    male  27.0      0      0   315154   8.6625   NaN        S
4          896       3  Hirvonen, Mrs. Alexander (Helga E Lindqvist)  female  22.0      1      1  3101298  12.2875   NaN        S
```
となり、`train.csv`と`test.csv`を表示することができた。

こちら、train.csvは学習用データなので「Survived」という項目がある。
一方で、test.csvはいわゆる問題用紙のようなもので、モデルを使ってSurvivedの有無を後で書く用のデータである。

(GitHubとのファイルのやり取りがめんどくさいので、マウントポイントなどを工夫してデータ移動工数を下げたい。)


## データの整備

続いて、データの整備を行う。
データの整備とは、欠損値を削除することで、計算等を行いやすくすることである。

デ＝他の整備は、簡単なようで奥が深い。
なぜなら、ただ単に欠損した値を削除するだけだと支障が出る場合がある。
例えば、ある列の半分くらいがNullだった場合などがそうである。

このような場合、Nullを平均値で置き換えるなどセンスが問われる部分が出てきてしまう。

このように、データの整備はただ単に実施する内容が決まっているものではなく臨機応変にデータを扱いやすくすることを言う。

そのため、ある人の考えがデータの内容に影響を及ぼすケースも少なくない。
そのような織り込まれた思想まで管理することができれば、よりよいデータ活用につながるだろう。

今回使うプログラムは、[fix_data.py](./code/fix_data.py)

### データの概要・代表的な値を確認

まずは、pandasのshape機能を使って、

```
[実行コマンド]
python3 /home/mainte/code/fix_data.py 

[結果]
(891, 12)
(418, 11)
===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
       PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200
===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== 
       PassengerId      Pclass         Age       SibSp       Parch        Fare
count   418.000000  418.000000  332.000000  418.000000  418.000000  417.000000
mean   1100.500000    2.265550   30.272590    0.447368    0.392344   35.627188
std     120.810458    0.841838   14.181209    0.896760    0.981429   55.907576
min     892.000000    1.000000    0.170000    0.000000    0.000000    0.000000
25%     996.250000    1.000000   21.000000    0.000000    0.000000    7.895800
50%    1100.500000    3.000000   27.000000    0.000000    0.000000   14.454200
75%    1204.750000    3.000000   39.000000    1.000000    0.000000   31.500000
max    1309.000000    3.000000   76.000000    8.000000    9.000000  512.329200
```

データの代表的な値が分かった。
count: 有効なエントリー数
mean: 平均値
std: 標準偏差
min: 最小値
25%: 第1四分位数（データセットの下位25%の境界にある値）
50%: 中央値
75%: 第3四分位数（データセットの上位75%の境界にある値）
max: 最大値

### 欠損データの確認
欠損データがあると、データ分析がうまくいかないケースがある。
まずは、どの程度欠損データがあるのか把握し、その後でその欠損データの扱いを考えていく。

isnullで判定、sum()で各列の欠損地のデータを出す。
```
python3 /home/mainte/code/fix_data.py 
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
```
パーセントに変換する。

```
PassengerId     0.000000
Survived        0.000000
Pclass          0.000000
Name            0.000000
Sex             0.000000
Age            19.865320
SibSp           0.000000
Parch           0.000000
Ticket          0.000000
Fare            0.000000
Cabin          77.104377
Embarked        0.224467
```

これらより、Cabinのデータは欠損率77%ということで、活用用のデータとしては扱いずらいことが分かった。

