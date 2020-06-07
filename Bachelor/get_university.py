#Excelから茨城大学工学部における各学科のシラバスデータを取得
import xlrd
import os

xls_file=input("Enter the xls_file name >> ")  # 取得したい学科を入力
file='{0}({1}).txt'    # {講義名}(講義コード).txt

xls_workbook = xlrd.open_workbook(xls_file+'.xls')  #Excelファイル読み込み
sheet = xls_workbook.sheet_by_index(0)       # インデックス番号で指定したシートに接続する:sheet名'シラバス'に接続

# Excelの8行目から最後の行までを参照する
for row_index in range(7, sheet.nrows-1):
	os.chdir('./シラバスデータ/'+xls_file)                     # ディレクトリを取得して移動
	Course_Title=sheet.cell_value(rowx=row_index, colx=4)    #講義名
	Remarks=sheet.cell_value(rowx=row_index, colx=13)        #科目コード
	outline = sheet.cell_value(rowx=row_index, colx=17)      #概要
	goals = sheet.cell_value(rowx=row_index, colx=19)        #到達目標
	fname=file.format(Course_Title, Remarks)                 # fileに代入
	# 各講義のテキストファイルを作成
	with open(fname, 'w') as f:
		raw_str=''.join(outline+'\n'+goals)                 # 内容を概要と到達目標で構成
		f.write(raw_str)
	os.chdir('../../')    # 移動前のディレクトリに戻る

print('ok!')
