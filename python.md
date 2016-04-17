# python

## 環境構築
### windows
[link1](http://qiita.com/y__sama/items/5b62d31cb7e6ed50f02c)
* `choco install miniconda`は動かない。
* `choco install miniconda3`は動かない。
1.[link](http://conda.pydata.org/miniconda.html)からinstallを落とす。
2. インストーラーをぽちぽちして、パスなどは通しておく。
3. おわり。


## anaconda
下記のコピペ。
[link1](http://qiita.com/y__sama/items/5b62d31cb7e6ed50f02c)

### 仮想環境
* 仮想環境構築
```
conda create -n py2 python=2.7 numpy scipy pandas jupyter
#anacondaとしてまとめて入れることも可能。
conda create -n anaconda2 python=2.7 anaconda
```
* 仮想環境確認
```
conda env list
# こちらでも出る。
conda info -e
```
* 仮想環境の出入り
```
# 仮想環境に入る
source activate py2
# windowsではactivate py2
# 仮想環境から抜ける
source deactivate
# windowsではdeactivate
```
* 仮想環境の削除
```
conda remove -n py2 --all
```

### パッケージ管理
* パッケージのインストール&アンインストール
```
conda install numpy scipy # pipと同じでスペース区切りで複数OK
conda install numpy=1.10.4 # バージョン指定も可能
conda install -n py2 numpy scipy # -nで環境名を指定もできる

conda update numpy # update

pip install numpy # pipも使える。condaにないときはこちらを利用
source activate py2;pip install numpy # 仮想環境に入れるときは、activateしなければいけない

conda uninstall -n py2 numpy # アンインストール
```
* パッケージの確認
```
conda list
# 現在入っているパッケージリスト

conda list -n py2
# -nで仮想環境下も選択可能

conda list --export > env.txt
conda create -n py2_copy --file env.txt
# エクスポートして再利用することも可能だが、
# pipで入れたパッケージはエクスポートできないのでpip freezeで別途出力しておく必要がある。
```


