cd /content/D-Epic/app/
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1-AEvdJoWZ35da8p5qRdXimpQe9wQ4hZq' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1-AEvdJoWZ35da8p5qRdXimpQe9wQ4hZq" -O models.zip && rm -rf /tmp/cookies.txt
unzip models.zip
rm models.zip