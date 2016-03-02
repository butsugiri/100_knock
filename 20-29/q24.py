# -*- coding: utf-8 -*-
"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""
import sys
import re

def main(fi):
    p = re.compile(r"\[*(File|ファイル):(?P<media_file_name>.+?\.[a-z]+)\|")
    for line in fi:
        line = line.rstrip()
        matchOB = p.finditer(line)
        for match in matchOB:
            print match.group("media_file_name")

if __name__ == "__main__":
    main(sys.stdin)

"""
❯ python q24.py < data/england.txt
Royal Coat of Arms of the United Kingdom.svg
The British Empire.png
Uk topo en.jpg
BenNevis2005.jpg
Elizabeth II greets NASA GSFC employees, May 8, 2007 edit.jpg
Palace of Westminster, London - Feb 2007.jpg
David Cameron and Barack Obama at the G20 Summit in Toronto.jpg
Soldiers Trooping the Colour, 16th June 2007.jpg
Scotland Parliament Holyrood.jpg
London.bankofengland.arp.jpg
City of London skyline from London City Hall - Oct 2008.jpg
Oil platform in the North SeaPros.jpg
Eurostar at St Pancras Jan 2008.jpg
Heathrow T5.jpg
Anglospeak.svg
CHANDOS3.jpg
PalaceOfWestminsterAtNight.jpg
Westminster Abbey - West Door.jpg
Edinburgh Cockburn St dsc06789.jpg
Canterbury Cathedral - Portal Nave Cross-spire.jpeg
Kew Gardens Palm House, London - July 2009.jpg
2005-06-27 - United Kingdom - England - London - Greenwich.jpg
Stonehenge2007 07 30.jpg
Yard2.jpg
Durham Kathedrale Nahaufnahme.jpg
Roman Baths in Bath Spa, England - July 2006.jpg
Fountains Abbey view02 2005-08-27.jpg
Liverpool Pier Head by night.jpg
Hadrian's Wall view near Greenhead.jpg
Wembley Stadium, illuminated.jpg
"""
