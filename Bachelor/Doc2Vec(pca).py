# -*- coding: utf-8 -*-
#Doc2Vecで作成した講義の特徴量を次元削減(pca)で可視化
from gensim import models
from gensim.models.doc2vec import Doc2Vec
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import re
import numpy as np
import warnings

warnings.filterwarnings('ignore')

PATH='{0}/{1}'
file='All.model'
model=Doc2Vec.load(file)

# 入力した講義に対する類似度の高い講義を出力
def search_similar(path):
  docs=[]
  d_vecs=[]
  d_vals=[]
  most_similar_texts=model.docvecs.most_similar(path, topn=50)
  print('入力講義：{0}/{1}'.format(Course, Course_Tiile))
  for most_similar in most_similar_texts:
    if '本科' not in most_similar[0]:
      print(most_similar)
      docs.append(most_similar[0])
      if len(docs)==45:
        break
  for doc in docs:
    d_vecs.append(model.infer_vector(doc))
  input_vec=model.infer_vector(path)
  docs.insert(0, path)
  d_vecs.insert(0, input_vec)
  scatter_plot_2d(d_vecs, docs)
  scatter_plot_3d(d_vecs, docs)

# 入力した講義に対する類似度の高い講義をpcaで次元削減(2次元)し、2次元座標に表示
def scatter_plot_2d(d_vecs, docs):
  n_components=2
  X=[]
  Y=[]
  pca=PCA(n_components=n_components).fit_transform(d_vecs)   #次元削減
  fig=plt.figure(1)
  #座標
  for i, name in enumerate(docs):
    X.append(pca[i,0])
    Y.append(pca[i,1])
  scatter=plt.scatter(X, Y, s=20, c=Y, cmap=plt.cm.viridis)
  for i, name in enumerate(docs):
    if i==0:
      plt.text(X[i], Y[i],  '%s' % docs[i], size=8, zorder=1, color='r')
    else:
      plt.text(X[i], Y[i],  '%s' % docs[i], size=8, zorder=1, color='k')
  plt.colorbar(scatter)
  plt.show()

# 入力した講義に対する類似度の高い講義をpcaで次元削減(3次元)し、3次元座標に表示
def scatter_plot_3d(d_vecs, docs):
  X=[]
  Y=[]
  Z=[]
  n_components=3           #次元数
  fig=plt.figure(3)
  ax=Axes3D(fig)
  pca=PCA(n_components=n_components).fit_transform(d_vecs)   #次元削減

  #座標
  for i, name in enumerate(docs):
    X.append(pca[i,0])
    Y.append(pca[i,1])
    Z.append(pca[i,2])
  scatter=ax.scatter3D(X, Y, Z, s=30, c=Z, cmap=plt.cm.viridis)  #出力される講義
  #点のラベル(講義名)
  for i, name in enumerate(docs):
    if i==0:
      ax.text(X[i], Y[i], Z[i],  '%s' % docs[i], size=8, zorder=1, color='r')
    else:
      ax.text(X[i], Y[i], Z[i],  '%s' % docs[i], size=8, zorder=1, color='k')
  plt.colorbar(scatter)
  plt.show()

if __name__=='__main__':
  Course=input('学科：>')
  Course_Tiile=input('講義名：>')
  print('\n')
  search_similar(PATH.format(Course, Course_Tiile))
