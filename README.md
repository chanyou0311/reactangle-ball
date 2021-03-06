# reactangle-ball

ビリヤードが跳ね返って穴に落ちるまでのシミュレーション

## ルール

テーブル（ビリヤード台）の縦と横の大きさと、ボールの開始座標、ボールの開始方向、ボールの終了座標から、ボールのたどった座標とステップ数を表示するプログラムを書け。

例えば

- テーブルの大きさ (6,3)
- 開始座標 (1,1)
- 開始方向 右下
- 終了座標 (1,3)

とすると、下記のようにテーブルの左上から左下の軌跡を描く。

| ○/1  |      |  9  |     |  5  |     |
| :--: | :--: | :-: | :-: | :-: | :-: |
|      | 2/10 |     | 4/8 |     |  6  |
| ●/11 |      |  3  |     |  7  |     |

これをプログラム上でシミュレートする。

## シミュレート方法

### 動作環境

- Python >= 3.7
- Pipenv (for lint)

### スクリプトの実行

#### ゴールできる場合

```
$ python main.py -t 6,3 -g 1,3
ステップ数: 1, 座標: (1, 1)
ステップ数: 2, 座標: (2, 2)
ステップ数: 3, 座標: (3, 3)
ステップ数: 4, 座標: (4, 2)
ステップ数: 5, 座標: (5, 1)
ステップ数: 6, 座標: (6, 2)
ステップ数: 7, 座標: (5, 3)
ステップ数: 8, 座標: (4, 2)
ステップ数: 9, 座標: (3, 1)
ステップ数: 10, 座標: (2, 2)
ステップ数: 11, 座標: (1, 3)
ゴール！
```

#### ゴールできない場合

```
$ python main.py -t 3,3 -g 1,3
ステップ数: 1, 座標: (1, 1)
ステップ数: 2, 座標: (2, 2)
ステップ数: 3, 座標: (3, 3)
ステップ数: 4, 座標: (2, 2)
ステップ数: 5, 座標: (1, 1)
ゴールできませんでした。
```

### その他のオプション

```
$ python main.py -h
usage: main.py [-h] -t TABLE -g GOAL_COORDINATE [-s START_COORDINATE] [-sd START_DIRECTION]

ビリヤードが跳ね返って穴に落ちるまでのシミュレーション

optional arguments:
  -h, --help            show this help message and exit
  -t TABLE, --table TABLE
                        テーブルのサイズ
  -g GOAL_COORDINATE, --goal_coordinate GOAL_COORDINATE
                        終了時の座標
  -s START_COORDINATE, --start_coordinate START_COORDINATE
                        開始時の座標
  -sd START_DIRECTION, --start_direction START_DIRECTION
                        開始時の方向
```

## テスト実行方法

```
$ python tests.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```
