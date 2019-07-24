# wordtext
A project for writers using `word` to edit novels on mobile devices.  
( I've been using `ward` to format novels )
  
`wordtotxt.py`・・・It converts word into text.  
`addtxttoword.py`・・・It reflects the added sentences in text to word.  
  
## Usage
Install `python-docx`
```
pip install python-docx
```
__config__  
Please set the home path of word you want to edit and word file name in the `conf/const.ini` 
__you have to create `conf/const.ini` in the this project.__ 
  
Example  
word file you want to edit : /home/test.docx
```const.ini
[common]
const_path = /home/
file_name = test
old_date = 20190725232358
```
  
__command__
```
python wordtotext.py
python addtxttoword.py
```  
when `python wordtotext.py` runs ...  
created `{const_path}/{file_name}_nowdatetime_.txt`  
( nowdatetime is saved as old_date in `conf/const.ini`)  
  
when `python addtxttoword.py` runs ...   
reflected the added sentences in `{const_path}/{file_name}_{old_date}_.txt` to `{const_path}/{file_name}.docx`.  
and, created `{const_path}/bk/{file_name}_nowdatetime_.docx` as backup file.  
  
I use `JotterPad`, writing the novel on a mobile device.  
`JotterPad` : https://play.google.com/store/apps/details?id=com.jotterpad.x  
I recommend saving the text file to the your google drive.
