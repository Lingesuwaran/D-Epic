import fitz
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import os

blacklist = [   '[document]',   'noscript', 'header',   'html', 'meta', 'head','input', 'script', 'style'  ]

data = "/content/AGT_rpg/Books/"
file_names = os.listdir(data)
file_name=data+str(file_names[0])
file_ext = file_name.split('.')



def	epub2html(epub_path):
	book = epub.read_epub(epub_path)
	chapters = []
	for i in book.get_items():
		if i.get_type() == ebooklib.ITEM_DOCUMENT:
			chapters.append(i.get_content())
	return chapters

def chap2text(chap):
	output = ''
	soup = BeautifulSoup(chap,'html.parser')
	text = soup.find_all(text=True)
	for t in text:
		if t.parent.name not in blacklist:
			output += '{}'.format(t)
	return output

def thtml2ttext(thtml):
  Output = []
  for html in thtml:
    text =  chap2text(html)
    Output.append(text)
  return Output

def epub2text(epub_path):
  chapters = epub2html(epub_path)
  ttext = thtml2ttext(chapters)
  return ttext

if file_ext[1] == 'pdf':
  pdf=fitz.open(file_name)
  n=pdf.pageCount
  for i in range(n):
    page = pdf.loadPage(i)
    text = page.getText('text')
    with open('/content/AGT_rpg/Books/data.txt','a')as file:
      text = text.replace('\n',' ')
      text = text.replace('”','')
      text = text.replace('“','')
      file.write(text.replace('\t',' '))
  pdf.close()
elif file_ext[1] == 'epub':
  text_L = epub2text(file_name)
  text = ''''''
  for i in text_L:
    text += i
  text = text.replace('\n',' ')
  text = text.replace('”','')
  text = text.replace('“','')
  with open('/content/AGT_rpg/Books/data.txt','a')as file:
      file.write(text.replace('\t',' '))
elif file_ext[1]== 'txt':
  text=""
  with open("/content/AGT_rpg/Books/data.txt",'r')as file:
    text=file.read()  
  text = text.replace('\n',' ')
  text = text.replace('”','')
  text = text.replace('“','')
  with open('/content/AGT_rpg/Books/data.txt','w')as file:
    file.write(text.replace('\t',' '))
else:
  print('invalid')

