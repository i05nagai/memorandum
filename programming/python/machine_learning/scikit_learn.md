---
tittle: scikit-learn
---

## scikit-learn

## Install

```
pip install sklearn
```

```
conda install -c anaconda scikit-learn
```

### model_selection
* `train_test_split`
    * データを訓練データとテストデータに分ける
* `learning_curve`
    * 横軸にnumber of training samples
    * 縦軸に精度のグラフを書くための計算をestimatorを渡すとやってくれる　
* `validation_curve`
    * 横軸にparameterの値
    * 縦軸に精度のグラフを書くための計算をestimatorを渡すとやってくれる　
* `cross_val_score`
    * cross validatinの処理を一括でやってくれる
* `GridSearchCV`
    * 

```python
X_train = []
y_train = []
import sklearn.svm as svm
import sklearn.pipeline as pipeline
import sklearn.preprocessiong as preprocessing
pipe_svc = pipeline.Pipeline([
    ("scl", preprocessing.StandardScaler()),
    ("clf", svm.SVC(random_state=1))
])
param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
param_grid = [
    {
        "cld__C": param_range,
        "clf__kernel": ["linear"],
    },
    {
        "clf__C": param_range,
        "clf__gamma": param_range,
        "clf__kernel": ["rbf"]
    }
]
gs = model_selection.GridSearchCV(estimator=pipe_svc, param_grid=param_grid, scoring="accuracy", cv=10, n_jobs=-1)
gs = gs.fit(X_train, y_train)
print(gs.best_score_)
print(gs.best_params_)
```

### pipeline
* `Pipeline`
    * 幾つかのestimatorをつなげる

### preprocessing
* `StandardScaler`
    * データの平均と分散を標準化してくれる
* `MinMaxScaler`
    * x - x_{mim} / (x_{max} - x_{min})
* `Imputer`
    * 指定した値(NaNなど)を前後の値を使って補間する
* `LabelEncoder`
    * カテゴリについたテキストラベルを数値に変換する


### metrics
* `accuracy_score`
    * 正解率を出す
    * 多クラスの場合は、当たった数 / 全体
* `precision_score`
	* 適合率、精度をだす
* `recall_score`
	* 再現度をだす
* `f1_score`
	* F値をだす

```python
import sklearn.metrics as metrics
print("Precision: {0}".format(metrics.precision_score(y_true=y_test, y_pred=y_pred)))
print("Recall: {0}".format(metrics.recall_score(y_true=y_test, y_pred=y_pred)))
print("F1: {0}".format(metrics.f1_score(y_true=y_test, y_pred=y_pred)))
```

* `roc_curve`
	* true_positive rateとfalse positive rateとthreshfoldを計算する
	* scoresの閾値を決めた時に、閾値以上を真、未満？を偽と予測した時のTPとFP
	* 閾値をscoresの最小値から最大値まで変化させた時のTPとFPが計算される

```python
y = np.array([1, 1, 2, 2])
scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = metrics.roc_curve(y, scores, pos_label=2)
```

* `roc_auc_score`
	* ROCのAUCの値を計算

### tree
* `export_graphviz`
    * 決定木の結果をgraphgiz形式で出力
    * `dot -Tpng tree.dot -o tree.png`でPngに

### linear_model
* `LogisticRegression`
    * クラス分類はdefaultでは1 vs ALL(One-vs-Rest)
    * クラス分類では`fit`後に`intercept_`にOvSの結果が入っている
    * `intercept_`は回帰式の定数項
        * `intercept_[0]`は0番目のクラスと残りのクラスの分類結果
        * `intercept_[1]`は1番目のクラスと残りのクラスの分類結果

### ensemble

### datasets
* `make_moon`
    * 半月状のデータを生成する
* `make_circles`
    * 同心円のデータを生成する

### feature_extraction
* `text.TfidfVectorizer` 
    * filename, file, 文字列を渡して、tfidfを計算する
    * `strip_accents`アクセントをぬく
    * `lowercase`はlowercaseに変換するか
    * `preprocessor`はn-gramsの作成と単語のtoken化の処理をユーザ関数で上書きする
* `text.HashingVectorizer`
    * 文字列から単語ごとの特徴量をつくる
    * `transform`で文字列をsparse matrixに変換した行列を得られる
        * 行が文書番号、列が単語番号で、値に特徴量が入っている

## Reference
