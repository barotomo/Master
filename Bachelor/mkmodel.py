# -*- coding:utf-8 -*-
# Doc2Vecモデル作成
import glob, os
from gensim import models
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

INPUT_UNIVERSITY_DIR='./H29茨城大学シラバス/'
INPUT_TECH_COLLEGE_DIR='./H29茨城高専シラバス/'

syllabuses_1=['H29マテ', 'H29メディア', 'H29機械', 'H29情報', 'H29生体', 'H29全学科', 'H29知能A', 'H29知能B', 'H29電電', 'H29都市']
syllabuses_2=['本科・専門共通', '本科・機械システム工学科', '本科・電気電子システム工学科', '本科・電子情報工学科', '本科・電子制御工学科', '本科・物理工学科']

# パラメータ ***********************************************************************
    #alpha: 学習率 (徐々にmin_alphaに近く)
    #min_count: 出現回数がmin_count以上のものだけ単語としてとる(default=5)
    #window: 対象語から調べる前後の語の数(default=5)
    #epochs: 反復学習(ここではtrainingsとして扱っている)
#----------------------------------------------------------------------------------
    #vector：分散表現（中間層）の次元数(デフォルトで100次元)
    #min_alpha：最小学習率
#**********************************************************************************
# Doc2Vecパラメータの設定
alpha=0.025
trainings=60
min_c=1
w_size=5
v_size=100
min_alpha=1.0e-7

# 茨城大学シラバス
def university(DIR=syllabuses_1):
    docs_1=[]
    tags_1=[]
    result_1=[]
    # 学科のフォルダ内ファイルを参照
    for syllabus in DIR:
        syllabus_dir=INPUT_UNIVERSITY_DIR+syllabus+'_wakati'
        files=os.listdir(syllabus_dir)    # フォルダ内ファイルをリストとして取得
        # フォルダ内ファイルを参照
        for file in files:
            #ファイル読み込み
            with open(syllabus_dir+'/'+file, 'r', encoding='utf-8', errors='ignore') as f:
                line=f.read()
                docs_1.append(line)      # 読み込んだテキストをリストに追加
                tags_1.append(syllabus+'/'+file.replace(INPUT_UNIVERSITY_DIR, '').replace('_wakati' ,'').replace('.wakati', ''))   # タグ（学科名/講義名）を作成しリストに追加

    # テキストとタグを登録
    for i, j in enumerate(docs_1):
        sentence=TaggedDocument(j, ['%s' % tags_1[i]])
        result_1.append(sentence)

    return result_1

# 茨城高専シラバス
def tech_college(DIR=syllabuses_2):
    docs_2=[]
    tags_2=[]
    result_2=[]
    # 学科のフォルダ内ファイルを参照
    for syllabus in DIR:
        syllabus_dir=INPUT_TECH_COLLEGE_DIR+syllabus+'_wakati'
        files=os.listdir(syllabus_dir)    # フォルダ内ファイルをリストとして取得
        # フォルダ内ファイルを参照
        for file in files:
            #ファイル読み込み
            with open(syllabus_dir+'/'+file, 'r', encoding='utf-8', errors='ignore') as f:
                line=f.read()
                docs_2.append(line)  # 読み込んだテキストをリストに追加
                tags_2.append(syllabus+'/'+file.replace(INPUT_TECH_COLLEGE_DIR, '').replace('_wakati' ,'').replace('.wakati', ''))  # タグ（学科名/講義名）を作成しリストに追加

    # テキストとタグを登録
    for i, j in enumerate(docs_2):
        sentence=TaggedDocument(j, ['%s' % tags_2[i]])
        result_2.append(sentence)

    return result_2

if __name__=='__main__':
    training_docs=university(syllabuses_1)   # 茨城大学シラバスのリストを取得
    training_docs.extend(tech_college(syllabuses_2))  # 茨城高専シラバスのリストを取得し、茨城大学シラバスのリストに追加
    # モデルの学習
    model=Doc2Vec(dm=1,
                  vector_size=v_size,
                  min_count=min_c,
                  window=w_size,
                  epochs=trainings,
                  alpha=alpha,
                  min_alpha=min_alpha
                 )
    model.build_vocab(training_docs)                                                  #文の順序から語彙を構築する
    model.train(training_docs, epochs=model.iter, total_examples=model.corpus_count)  #学習する
    model.save('All.model')    # モデルの保存

    print('Ok')
