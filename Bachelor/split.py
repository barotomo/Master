#分かち書きファイル作成
# -*- coding:utf-8 -*-

import os, re, shutil, glob
import MeCab, nltk, mojimoji
import unicodedata

INPUT_UNIVERSITY_DIR='./H29茨城大学シラバス/'
INPUT_TECH_COLLEGE_DIR='./H29茨城高専シラバス/'


def split_words(text):
  text=text.strip('')                                       #空白文字の除去(文字の間の空白は除去されない)
  text=mojimoji.zen_to_han(text, kana=False)                #全角を半角にする(カタカナは無効)

  text=unicodedata.normalize('NFC', text)                   #文字列の正規化（主に文字と濁点の結合）

  alpha_digit_symbolReg=re.compile(r"[ぁ-んァ-ン一-龥]")      #ひらがな、カタカナ、漢字の判定
  # テキストを1行ずつ処理
  lines=text.split("\r\n")                                  #改行で区切る
  result=[]
  for line in lines:
    res=[]
    if alpha_digit_symbolReg.search(line) is not None:   #日本語文章の場合
      line=line.replace(" ", "")
      mecab=MeCab.Tagger("-Owakati")
      mecab.parse('')
      node=mecab.parseToNode(line)          #parseToNode()：形態素の詳細情報が得られる
      while node:
        fields=node.feature.split(',')      #node.feature：形態素情報を返す
        if fields[0] == '名詞' or fields[0] == '動詞' or fields[0] == '形容詞' or fields[0] == '記号':     #名詞、動詞、形容詞のみを抽出
          res.append(node.surface)          #node.surface：表層形を返す
          res.append(' ')
        node=node.next
    else:                                                 #英文の場合
      words=nltk.word_tokenize(line)
      k=" ".join(words)
      res.append(k)
    res.append('\n')
    l="".join(res)
    result.append(l)
  return result

def mk_wakati(DIR):
  INPUT_DIR=DIR
  if INPUT_DIR=='./H29茨城大学シラバス/':
    syllabuses=['H29マテ', 'H29メディア', 'H29機械', 'H29情報', 'H29生体', 'H29全学科', 'H29知能A', 'H29知能B', 'H29電電', 'H29都市']
  elif INPUT_DIR=='./H29茨城高専シラバス/':
    syllabuses=['本科・専門共通', '本科・機械システム工学科', '本科・電気電子システム工学科', '本科・電子情報工学科', '本科・電子制御工学科', '本科・物理工学科']

  class_count={}
  for syllabus in syllabuses:
    syllabus_dir=INPUT_DIR+syllabus
    files=sorted(os.listdir(syllabus_dir))     #./シラバスデータ/syllabus内の全ファイル
    class_count[syllabus]=0
    for Class in files:                        #./シラバスデータ/syllabus内のファイルを1つずつ参照
      results=[]
      print(syllabus, Class)
      class_count[syllabus]+=1
      class_file=syllabus_dir+'/'+Class        #./シラバスデータ/syllabus/Class
      try:
        with open(class_file, 'r', encoding='utf-8', errors='ignore') as Input_f:         #ファイル読み込み
          x=Input_f.read()
          x=x.split('\n')
          s=''.join(x[:-2])
          lines=split_words(s)  #形態素解析
          results+=lines
      except Exception as e:                   #エラーが生じた際の処理
        print('[error]', class_file, e)
        continue

      os.chdir(INPUT_DIR+syllabus+'_wakati')           #ディレクトリ移動
      fname=Class.replace(".txt", ".wakati")
      with open(fname, 'w', encoding='utf-8') as Output_f:                                   #ファイル書き込み
        Output_f.write(''.join(results))
      os.chdir('../../')                         #ディレクトリ移動

  print("講義数：", class_count)


if __name__=='__main__':
  a=input("H29茨城大学シラバス：0  /  H29茨城高専シラバス：1 >>")
  if a=='0':
    mk_wakati(DIR=INPUT_UNIVERSITY_DIR)
  elif a=='1':
    mk_wakati(DIR=INPUT_TECH_COLLEGE_DIR)
