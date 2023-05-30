"""
+------------------------------+------------------+----------+
| Description | Published Date | Victim's Website | Post URL |
+------------------------------+------------------+----------+
|      X      |                |                  |    x     |
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
            if filename.startswith('ragroup-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                divs_name=soup.find_all("div", {"class": "posts-line"})
                for div in divs_name:
                    title = div.find("a").text
                    url =  div.find("a")["href"]
                    parts = filename.split('-')
                    site = parts[1].replace('.html','')
                    post_url = 'http://' + site + '.onion' + url
                    if "(Full Leaked)" not in title:
                        appender(title, 'ragroup', '','','',post_url)
                file.close()
        except:
            errlog('ragroup: ' + 'parsing fail')
            pass    
