# -*- coding:utf-8 -*-
import os
import MeCab
import re
import unicodedata

cat=input('カテゴリ:')

if cat=='0':
    INPUT_DIR='/Users/Baron/Document/text_mining/Texts/body/dokujo-tsushin'
    OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/wakati_body/dokujo-tsushin'
elif cat=='1':
    INPUT_DIR='/Users/Baron/Document/text_mining/Texts/body/it-life-hack'
    OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/wakati_body/it-life-hack'
elif cat=='2':
    INPUT_DIR='/Users/Baron/Document/text_mining/Texts/body/movie-enter'
    OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/wakati_body/movie-enter'
elif cat=='3':
    INPUT_DIR='/Users/Baron/Document/text_mining/Texts/body/sports-watch'
    OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/wakati_body/sports-watch'


files=os.listdir(INPUT_DIR)
mecab=MeCab.Tagger ("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
####  修正 #########################################
# def split_words(text):
#   result = []
#   word_s = mecab.parse(text)
#   for n in word_s.split("\n"):
#     if n == 'EOS' or n == '': continue
#     p = n.split("\t")
#     q = p[1].split(',')
#     q.insert(0, p[0])
#     h0, h1, h2, h7 = (q[0], q[1], q[2], q[7])
#     if not (h1 in ['名詞', '動詞', '形容詞']): continue
#     if h1 == '名詞' and h2 == '数': continue
#     if h1 == '名詞' and h7 == '*': result.append(h0)
#     result.append(h7)
#   return result
##################################################
def split_words(text):
  result = []
  word_s = mecab.parse(text)
  for n in word_s.split("\n"):
    if n == 'EOS' or n == '': continue
    p = n.split("\t")[1].split(",")
    h, h2, org = (p[0], p[1], p[6])
    if not (h in ['名詞', '動詞', '形容詞']): continue
    if h == '名詞' and h2 == '数': continue
    result.append(org)
  return result

dict={}
for file in files:
  if file=='.DS_Store':
    continue
  else:
    with open(INPUT_DIR+'/'+file, 'r', encoding='utf-8', errors='ignore') as I:         #ファイル読み込み
      text=I.read()
      line=split_words(text)  #形態素解析
      dict[file]=line

# ファイル書き込み
for k, v in dict.items():
  # k=k.replace('\n','')   #null byte削除
  # k=k.replace('\u3000','')   #null byte削除
  s=' '.join(v)+'\n'
  try:
    with open(OUTPUT_DIR+'/'+k, 'w') as O:
      O.write(s)
  except:
    print(v)
    continue
