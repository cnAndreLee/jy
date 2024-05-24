# jy

cat /tmp/610821003303_CDDY_20240514133511.txt | tr '~' '\n' |awk -F ';' '{print NR,$4}'

