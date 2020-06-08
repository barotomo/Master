# 研究テーマ<br>
「Doc2Vecを用いたニュースヘッドラインの自動分類」<br>
## 概要<br>
### Doc2Vec<br>
Doc2Vecでモデルを作成
#### Body（ヘッドライン+本文）<br>
##### mk_body.py<br>
ニュース記事からヘッドラインと本文で構成した各記事をテキストファイルで作成
##### wakati.py<br>
作成したテキストファイルを分かち書きし、分かち書きされたテキストファイルを作成
##### mk_model.ipynb<br>
Doc2Vecモデルの作成
##### mk_pickle.ipynb<br>
pickleの作成
##### MLP.ipynb.ipynb<br>
MLPでの分類
##### Naive Baye.ipynb<br>
Naive Bayesでの分類
##### Random Forest.ipynb<br>
Random Forestでの分類
#### Headline(ヘッドラインのみ)<br>
##### mk_head.py<br>
ニュース記事からヘッドラインのみで構成した各記事をテキストファイルで作成
##### wakati.py<br>
作成したテキストファイルを分かち書きし、分かち書きされたテキストファイルを作成
##### mk_model.ipynb<br>
Doc2Vecモデルの作成
##### mk_pickle.ipynb<br>
pickleの作成
##### MLP.ipynb.ipynb<br>
MLPでの分類
##### Naive Baye.ipynb<br>
Naive Bayesでの分類
##### Random Forest.ipynb<br>
Random Forestでの分類<br>
--------------------------------------------------------------------------------------------------------<br>
### TF-IDF<br>
TF-IDFでモデルを作成
#### Body（ヘッドライン+本文）<br>
##### tfidf.py<br>
ヘッドラインと本文で構成された各記事のテキストファイルをベクトル化
##### mk_pickle.ipynb<br>
pickleの作成
##### MLP.ipynb.ipynb<br>
MLPでの分類
##### Naive Baye.ipynb<br>
Naive Bayesでの分類
##### Random Forest.ipynb<br>
Random Forestでの分類
#### Headline（ヘッドラインのみ）<br>
##### tfidf.py<br>
ヘッドラインのみで構成された各記事のテキストファイルをベクトル化
##### mk_pickle.ipynb<br>
pickleの作成
##### MLP.ipynb.ipynb<br>
MLPでの分類
##### Naive Baye.ipynb<br>
Naive Bayesでの分類
##### Random Forest.ipynb<br>
Random Forestでの分類
