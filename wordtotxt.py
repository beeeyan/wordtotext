import docx
import datetime
import sys
import configparser

# 各定数の取得
const = configparser.ConfigParser()
const.read('conf/const.ini')
const_path = const.get('common','const_path')
file_name = const.get('common','file_name')

now_date = datetime.datetime.today().strftime("%Y%m%d%H%M%S")

# パス
txt_path = const_path + file_name + '_' + now_date + '_' + '.txt'
word_path = const_path + file_name + '.docx'
doc = docx.Document(word_path)

# ワードから文書を取得してテキストファイルに保存する
with open(txt_path, mode='a') as f:
    for par in doc.paragraphs:
        f.write(par.text + '\n')

const.set('common','old_date',now_date)
# 定数の更新
with open('conf/const.ini', 'w') as f:
    const.write(f)