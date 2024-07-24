![logo](./fig/titanic-logo.png)

## はじめに

今回、Kaggleに登録したことに際してせっかくならコードを蓄積させていこうと考えている。  
Pythonはprint程度、numpy,pandasはインストールくらいの経験値なので、1つ1つ丁寧に確認する。

各ステップごとに、その状態のcodeを保存して積み上げていくイメージで作成していく。

今まで、前に書いた処理を何の目的で入れたか・もしくは入れたこと自体よく忘れてしまうことが多かった。
そのため、後で読み返すと一から読み返すくらい工数がかかる。

しかも、実践したことも忘れてることが多い。  
そうなると、やってきた実感もわかないというところで、コーディングを先延ばしにしていた。

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

## 決定木での学習

