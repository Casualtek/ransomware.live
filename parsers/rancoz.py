
"""
+------------------------------+------------------+----------+
| Description | Published Date | Victim's Website | Post URL |
+------------------------------+------------------+----------+
|      X      |                |          X       |          |
+------------------------------+------------------+----------+
Rappel : def appender(post_title, group_name, description="", website="", published="", post_url=""):
"""
import os
from bs4 import BeautifulSoup
from sharedutils import errlog
from parse import appender

def main():
    for filename in os.listdir('source'):
        try:
            if filename.startswith('rancoz-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                divs_name=soup.find_all('tr', {"class": "trow"})
                for div in divs_name:
                    title = div.find_all('td')[0].text.strip()
                    description = div.find_all('td')[2].text.strip()
                    parts = filename.split('-')
                    url = parts[1].replace('.html','')
                    link = div.find('a')
                    link = link.get('href')
                    post_url = 'http://' + url + '.onion' + link
                    appender(title, 'rancoz', description,'','',post_url)
                file.close()
        except:
            errlog('rancoz: ' + 'parsing fail')
            pass    
