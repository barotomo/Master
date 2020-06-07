#茨城工業高等専門学校のhtmlからシラバスデータをスクレイピング
import requests as web
import bs4
import openpyxl as excel
import os

dir_name=input("Enter the dir_name >>")  # 取得したい学科を入力

files=sorted(os.listdir("./H29茨城高専シラバス/html/"+dir_name)) # フォルダ内のファイル取得
del files[0]  # .DS_Storeの削除

# 取得したhtmlファイルを参照
for file in files:
	l=[]
	html_text=open('./H29茨城高専シラバス/html/'+dir_name+'/'+file, 'r', encoding='utf-8')   # htmlファイル読み込み
	soup = bs4.BeautifulSoup(html_text, "html.parser")  #htmlからBeautifulSoupオブジェクトを作成

	td=soup.find_all("td")    # td要素を取得
	for t in td:
		l.append(t.get_text())   # テキストのみを取得

	os.chdir("./H29茨城高専シラバス/txt/"+dir_name)       # ディレクトリを取得して移動
	# 各講義のテキストファイルを作成
	with open(file.replace('html', 'txt'), "w") as f:
		raw_str=''.join(l[5]+'\n'+l[6]+'\n'+'\n')
		f.write(raw_str)
	os.chdir("../../../")   # 移動前のディレクトリに戻る

print("ok")
