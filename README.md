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


## データの整備

## 決定木での学習

