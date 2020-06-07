import os

# INPUT_DIR='/Users/Baron/Document/text_mining/Texts/source/dokujo-tsushin'
# OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/head/dokujo-tsushin'

# INPUT_DIR='/Users/Baron/Document/text_mining/Texts/source/it-life-hack'
# OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/head/it-life-hack'

# INPUT_DIR='/Users/Baron/Document/text_mining/Texts/source/sports-watch'
# OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/head/sports-watch'

INPUT_DIR='/Users/Baron/Document/text_mining/Texts/source/movie-enter'
OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/head/movie-enter'


files=os.listdir(INPUT_DIR)
lines=[]
for i in files:
  with open(INPUT_DIR+'/'+i, 'r', encoding='utf-8', errors='ignore') as I:         #ファイル読み込み
    if I == INPUT_DIR+'/'+'LISENCE.txt':
      continue
    elif I== INPUT_DIR+'/'+'.DS_Store':
      continue
    text=I.readlines()
    lines.append(text[2])

for j in lines:
  k=j.replace('\n', '').replace('\u3000', '')   #改行削除, null byte削除
  try:
    with open(OUTPUT_DIR+'/'+k, 'w') as O:
      O.write(j)
  except:
    print('Error File :'+k)
    continue
