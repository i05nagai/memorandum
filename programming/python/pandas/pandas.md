---
title: pandas
---

## pandas


## Install

```
pip install pandas
```

## Term
* `index`
    * the name of a row
    * by default consecutive interger (i.e. 1, 2, 3, ...)
    * if you count data per date and per some ID say customerID, each data is related to a pair `((date, customerID), (col1_data1, col2_data1))`. In this case, `(date, customerID)` is a index and `(col1_data1, col2_data1` is a data of a column.
* `columns`
    * data
* `Series`
    * One-dimensional ndarray with axis labels (including time series).
    * [pandas\.Series — pandas 0\.23\.1 documentation](https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.Series.html)
    * `data`
    * `index`

## Usage

## DataFrame

### data selection

* `df.loc[col_name]`
* `df.iloc[idx_for_col]`
* `df.iat[idx_for_index, idx_for_col]`
    * access to data (idx_for_index, idx_for_col)
* `df.ix[]`
* `df[col_name]`



```python
# columnの4番目が"Iris-setosa"のもののみ
df[df[4] == "Iris-setosa"]
# column_nameが"Iris-setosa"のもののみ
df.query("column_name == 'Iris-setosa'|column_name == 'Iris-Setosa'")
```

## データソート

```python
df.sort("")
```

## データ変換
* `pandas.get_dummies`
    * [pandas.get_dummies — pandas 0.19.2 documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html)

## データ取得

```python
import pandas as pd
df_wine = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)
df_wine.columns = [
    "Class label",
    "Alcohol",
    "Malic acid",
    "Ash",
    "Alcalinity of ash",
    "Magnesium",
    "Total phenols",
    "Flavanoids",
    "Nonflavanoids pheonls",
    "Proanthocyanins",
    "Color intensity",
    "Hue",
    "OD280/OD315 of diluted wines",
    "Proline"
]
df_wine = df_wine[df_wine["Class label"] != 1]
y = df_wine["Class label"].values
X = df_wine[["Alcohol", "Hue"]].values
import sklearn.preprocessing as preprocessing
import sklearn.model_selection as model_selection
le = preprocessing.LabelEncoder()
y = le.fit_transform(y)
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.4, random_state=1)
```

## method
* pandas.read_csv


### DataFrame
* `df["col"].sum(axis=0)`
    * 0で縦方向の集計
* `df[["col1", "col2"]].sum(axis=1)`
    * 1で縦方向の集計
* `df.pivot_table("col", aggfunc="sum", fill_value=0, )`
* `df.groupby("col")`
* `df.query("col == value")`
    * True/False のlistがかえる
* `df.sort("col", accending=True)`
    * colの昇順ソート
    * defaultはTrue


## Tips

####

```
# co1_value: [['col2_val', col3_val],]
df.groupby('col1').get_group('col1_value')[['col2', 'col3']].values
```

### Iterate


### Remove NaN
* [データフレームから欠損値(np.nan)を除く方法 - ねこゆきのメモ](http://nekoyukimmm.hatenablog.com/entry/2015/02/25/222414)

* `df.dropna(subset=["col"])`
    * colにNanを含む行を除く


### 特定の条件の行を取り出す
行と対応したTrue/Falseのlistを渡せば良い。

```
true_false_list = []
df[true_false_list]
```

### print out all rows and columns
* `pd.set_option("display.max_rows", 101)`
* `pd.set_option("display.max_columns", 101)`


### displayed significant digit
* [ゆるふわPandasチートシート - Qiita](http://qiita.com/tanemaki/items/2ed05e258ef4c9e6caac)


## API

## Reference
* [Python Pandasでのデータ操作の初歩まとめ − 前半：データ作成＆操作編 - Qiita](http://qiita.com/hik0107/items/d991cc44c2d1778bb82e)
* [Python pandas データ選択処理をちょっと詳しく <後編> - StatsFragments](http://sinhrks.hatenablog.com/entry/2014/11/18/003204)
* [Python pandas データ選択処理をちょっと詳しく <中編> - StatsFragments](http://sinhrks.hatenablog.com/entry/2014/11/15/230705)
* [Python Pandasでのデータ操作の初歩まとめ − 後半：データ集計編 - Qiita](http://qiita.com/hik0107/items/0ae69131e5317b62c3b7)
* [Python Pandasでのデータ操作の初歩まとめ − 後半：データ集計編 - Qiita](http://qiita.com/hik0107/items/0ae69131e5317b62c3b7)

