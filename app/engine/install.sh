#wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1N7LVLbxuL67_irmuSmJp_WRmSDHxanu5' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1N7LVLbxuL67_irmuSmJp_WRmSDHxanu5" -O checkpoint.zip && rm -rf /tmp/cookies.txtpip install gpt-2-simple
#unzip checkpoint.zip -d /content/AGT_rpg/
#rm checkpoint.zip
pip install Pillow==2.2.1
pip install pyfiglet
pip install colorama
pip install fitz
pip install PyMuPDF
pip install ebooklib
pip install flask_ngrok
pip install gpt_2_simple

cd /content/app/

python db_create.py

cd /content/app/engine/

python language_m_downloader.py