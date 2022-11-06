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

## API
- `estimator`
    - `fit()`
        - a dataset
        - a dataset + labels
    - `imputer.strategy`
    - `imputer.statistics_`
- transformers
    - `fit()`
    - `transform()`
- predictors
    - `fit()`
    - `predict()`
    - `score()`

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
* `check_scoring(estimator, scoring=None, allow_none=False)`
    * `scoring`
        * `<score>_<average>`
            * `<score>`
                * `f1`,
                * `precision`,
                * `precision`,
* `fbeta_score(y_true, y_pred, beta, labels=None, pos_label=1, average='binary', sample_weight=None)`
    * The F-beta score is the weighted harmonic mean of precision and recall

```
SCORERS = dict(explained_variance=explained_variance_scorer,
               r2=r2_scorer,
               max_error=max_error_scorer,
               neg_median_absolute_error=neg_median_absolute_error_scorer,
               neg_mean_absolute_error=neg_mean_absolute_error_scorer,
               neg_mean_squared_error=neg_mean_squared_error_scorer,
               neg_mean_squared_log_error=neg_mean_squared_log_error_scorer,
               accuracy=accuracy_scorer, roc_auc=roc_auc_scorer,
               balanced_accuracy=balanced_accuracy_scorer,
               average_precision=average_precision_scorer,
               neg_log_loss=neg_log_loss_scorer,
               brier_score_loss=brier_score_loss_scorer,
               # Cluster metrics that use supervised evaluation
               adjusted_rand_score=adjusted_rand_scorer,
               homogeneity_score=homogeneity_scorer,
               completeness_score=completeness_scorer,
               v_measure_score=v_measure_scorer,
               mutual_info_score=mutual_info_scorer,
               adjusted_mutual_info_score=adjusted_mutual_info_scorer,
               normalized_mutual_info_score=normalized_mutual_info_scorer,
               fowlkes_mallows_score=fowlkes_mallows_scorer)
```

* `accuracy_score`
    * 正解率を出す
    * 多クラスの場合は、当たった数 / 全体
* `precision_score`
    * calculate precision
* `recall_score`
    * calculate recall
* `f1_score(y_true, y_pred, labels=None, pos_label=1, average=’binary’, sample_weight=None)`
    * calcualte F1-score
    * `average`
        * `None`
        * `binary`
        * `micro`
            * Calculate metrics globally by counting the total true positives, false negatives and false positives.
        * `macro`
            * Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.
        * `weighted`
            * Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account.
        * `samples`

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

## svm
* `SVC`
    * `kernel`
        * `precomputed`
            * you need to pass square kernel matrix
    * `C`

### ensemble

* `RandomForestClassifier`
    * `fit(self, X, y, sample_weight=None)`
        * `X` is converted to `np.float32`
        * `y` is converted to `np.float32`

* `GradientBoostingClassifier`
    * `loss`
    * `subsample`
        * The fraction of samples to be used for fitting the individual base learners.
        * if smaller than 1.0 this results in Stochastic Gradient Boosting
    * `criterion`
        * `friedman_mse`
            * the mean squared error with improvement score by Friedman
        * `mse`
            * mean squared error
        * `mae`
            * mean absolute error
    * `min_samples_split`
        * int
            * consider min_samples_split as the minimum number.
        * float
            * a fraction and ceil(min_samples_split * n_samples) are the minimum number of samples for each split
    * `min_samples_leaf`
        * int
        * float
    * `min_impurity_decrease`
    * `init`
        * An estimator object that is used to compute the initial predictionsstimator
        * None
            * it uses loss.init_estimator.
    * `max_features`
        * int
        * float
        * auto
        * sqrt
        * log2
        * None
            * max_features=n_features.
    * `max_leaf_nodes`
    * `warm_start`
    * `presort`
        * bool
        * `auto`
    * `n_iter_no_change`
        * None
            * disable early stopping
    * `validation_fraction`
        * Only used if n_iter_no_change is set to an integer.
    * `random_state`
        * `None`
            * the random number generator is the RandomState instance used by np.random.


### datasets
* `make_moon`
    * create data whose points draw harf circle
* `make_circles`
    * create data whose points draw a concentric circle

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

## pipeline
* `Pipeline([('name1', estimator1), ('name2', estimator2)])`
    * `estimator` has to have `fit` or `fit_transform`, and  `transform` methods
        * if `estimator` has `fit_transform`, `fit_transform` is called instead of `fit`
    * the input of `estimator2` is the result of `estimator1.fit_transform()` or `estimator1.fit().transform()`

## Reference
