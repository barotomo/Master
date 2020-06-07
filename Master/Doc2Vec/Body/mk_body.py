import os, re

cat=input('カテゴリ:')

if cat=='0':
    INPUT_DIR='/Users/Baron/Document/text_mining/Texts/source/dokujo-tsushin'
    OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/body/dokujo-tsushin'
elif cat=='1':
    INPUT_DIR='/Users/Baron/Document/text_mining/Texts/source/it-life-hack'
    OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/body/it-life-hack'
elif cat=='2':
    INPUT_DIR='/Users/Baron/Document/text_mining/Texts/source/sports-watch'
    OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/body/sports-watch'
elif cat=='3':
    INPUT_DIR='/Users/Baron/Document/text_mining/Texts/source/movie-enter'
    OUTPUT_DIR='/Users/Baron/Document/text_mining/Texts/body/movie-enter'


files=os.listdir(INPUT_DIR)
dic={}
lines=[]
titles=[]
for i in files:
    with open(INPUT_DIR+'/'+i, 'r', errors='ignore') as I:
        if I == INPUT_DIR+'/'+'LISENCE.txt':continue
        elif I== INPUT_DIR+'/'+'.DS_Store':continue
        text=I.readlines()
#         del text[0:2]
        titles.append(text[2])
#         lines.append(text[1:])
        lines.append(text[:])

for i, j in zip(titles, lines):
    j=''.join(j)
    i=i.replace('\n', '').replace('\u3000', ' ')   #改行削除, null byte削除
    try:
        with open(OUTPUT_DIR+'/'+i, 'w') as O:
            O.write(j)
    except:
        print('Error File :'+i)
        continue
