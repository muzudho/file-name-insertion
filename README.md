# file-name-insertion

ファイル名に修正日時を入れたりするのに使う（＾～＾）

# Run

```shell
python main.py

# ファイルに出力するなら
python main.py > foo.log
```

# Case study

## Case 1

例えばファイル名を以下のように付けているとする。  

```plaintext
201409__shogi-sdt2__suji115-120.png
```

これを以下のように変形したい。  

```plaintext
201409__shogi-sdt2__01-suji115-120.png
```

ならば正規表現は以下のようにする。  

```plaintext
^(201409__shogi-sdt2__)([^\.]*.png)$
```

文字列フォーマットは以下のようにする。  

```plaintext
{0}{2}-{1}
```
