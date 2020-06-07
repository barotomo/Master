#TF-IDFで作成した講義の特徴量を次元削減(pac)で可視化
import numpy as np
import glob, os
from sklearn.feature_extraction.text import TfidfVectorizer
import math

from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

np.set_printoptions(threshold=np.inf)

INPUT_UNIVERSITY_DIR='./H29茨城大学シラバス/'
INPUT_TECH_COLLEGE_DIR='./H29茨城高専シラバス/'
syllabuses_1=['H29マテ', 'H29メディア', 'H29機械', 'H29情報', 'H29生体', 'H29全学科', 'H29知能A', 'H29知能B', 'H29電電', 'H29都市']
syllabuses_2=['本科・専門共通', '本科・機械システム工学科', '本科・電気電子システム工学科', '本科・電子情報工学科', '本科・電子制御工学科', '本科・物理工学科']

# 茨城大学シラバス
def university(DIR=syllabuses_1):
    docs_1=[]
    tags_1=[]
    # 茨城大学シラバスフォルダの各学科フォルダを参照
    for syllabus in DIR:
        syllabus_dir=INPUT_UNIVERSITY_DIR+syllabus+'_wakati'
        files=os.listdir(INPUT_UNIVERSITY_DIR+syllabus+'_wakati')
        # 各学科フォルダ内のファイルを参照
        for file in files:
            # ファイル読み込み
            with open(syllabus_dir+'/'+file, 'r', encoding='utf-8', errors='ignore') as f:
                line=f.read()
                docs_1.append(line)  # 読み込んだテキストをリストに追加
                tags_1.append(syllabus+'/'+file.replace(INPUT_UNIVERSITY_DIR, '').replace('_wakati' ,'').replace('.wakati', ''))   # タグ（学科名/講義名）を作成しリストに追加

    docs_1=[s.replace('\n', '') for s in docs_1]         #文書内容(入力文書を含む)

    return docs_1, tags_1

# 茨城高専シラバス
def tech_college(DIR=syllabuses_2):
    docs_2=[]
    tags_2=[]
    # 茨城高専シラバスフォルダの各学科フォルダを参照
    for syllabus in DIR:
        syllabus_dir=INPUT_TECH_COLLEGE_DIR+syllabus+'_wakati'
        files=os.listdir(INPUT_TECH_COLLEGE_DIR+syllabus+'_wakati')
        # 各学科フォルダ内のファイルを参照
        for file in files:
            # ファイル読み込み
            with open(syllabus_dir+'/'+file, 'r', encoding='utf-8', errors='ignore') as f:
                line=f.read()
                docs_2.append(line)   # 読み込んだテキストをリストに追加
                tags_2.append(syllabus+'/'+file.replace(INPUT_TECH_COLLEGE_DIR, '').replace('_wakati' ,'').replace('.wakati', ''))   # タグ（学科名/講義名）を作成しリストに追加

    docs_2=[s.replace('\n', '') for s in docs_2]         #文書内容(入力文書を含む)

    return docs_2, tags_2

# TF-IDFで講義の特徴量を作成
def tfidf(docs, tags):
    dic={}
    np.set_printoptions(precision=2)
    vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u'(?u)\\b\\w+\\b')  # 文書のベクトル化
    vecs = vectorizer.fit_transform(docs)  # 値を正規化

    values=vecs.toarray()

    dic=dict(zip(tags, values))

    Course=input('学科：>')
    Course_Tiile=input('講義名：>')
    path='{0}/{1}'.format(Course, Course_Tiile)

    value=dic[path]    #入力した講義のベクトル
    print("入力講義："+str(path))


    d={}
    for i in dic:
        if i==path:
            continue
        else:
            d.update([(i, cosine_similarity(value, dic[i]))])

    a=[]
    b=[]
    a.insert(0, path)
    b.insert(0, value)

    scatter_plot_2d(b, a)
    scatter_plot_3d(b, a)

# cos類似度
def cosine_similarity(v1, v2):
    result=np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    if math.isnan(result)==True:
        result=0.0

    return result

# 入力した講義に対する類似度の高い講義をpcaで次元削減(2次元)し、2次元座標に表示
def scatter_plot_2d(b, a):
  n_components=2
  X=[]
  Y=[]
  pca=PCA(n_components=n_components).fit_transform(b)   #次元削減
  fig=plt.figure(1)

  #座標
  for i, name in enumerate(a):
    X.append(pca[i,0])
    Y.append(pca[i,1])

  scatter=plt.scatter(X, Y, s=20, c=Y, cmap=plt.cm.viridis)
  for i, name in enumerate(a):
    if i==0:
      plt.text(X[i], Y[i],  '%s' % a[i], size=7, zorder=1, color='r')
    else:
      plt.text(X[i], Y[i],  '%s' % a[i], size=7, zorder=1, color='k')

  plt.colorbar(scatter)
  plt.show()

# 入力した講義に対する類似度の高い講義をpcaで次元削減(3次元)し、3次元座標に表示
def scatter_plot_3d(b, a):
  X=[]
  Y=[]
  Z=[]
  n_components=3
  fig=plt.figure(3)
  ax=Axes3D(fig)
  pca=PCA(n_components=n_components).fit_transform(b)   #次元削減

  #座標
  for i, name in enumerate(a):
    X.append(pca[i,0])
    Y.append(pca[i,1])
    Z.append(pca[i,2])

  scatter=ax.scatter3D(X, Y, Z, s=30, c=Z, cmap=plt.cm.viridis)  #出力される講義

  #点のラベル(講義名)
  for i, name in enumerate(a):
    if i==0:
      ax.text(X[i], Y[i], Z[i],  '%s' % a[i], size=7, zorder=1, color='r')
    else:
      ax.text(X[i], Y[i], Z[i],  '%s' % a[i], size=7, zorder=1, color='k')
  plt.colorbar(scatter)
  plt.show()

if __name__=='__main__':
    docs=[]
    tags=[]
    # テキストをリストに追加
    docs.extend(university(syllabuses_1)[0])
    docs.extend(tech_college(syllabuses_2)[0])
    # タグをリストに追加
    tags.extend(university(syllabuses_1)[1])
    tags.extend(tech_college(syllabuses_2)[1])

    tfidf(docs, tags)
