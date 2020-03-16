# system level impot first
import sys
import io
import os

import gzip
import requests
import argparse

# specific dependency modules next
from bs4 import BeautifulSoup
# from datetime import datetime
from urllib.request import Request, urlopen

'''
USAGE : python src/url/asiapharmaceutics.py "http://www.asiapharmaceutics.info/
     index.php/ajp/issue/archive"

link : http://www.asiapharmaceutics.info/index.php/ajp/issue/archive"
'''

agent = {"User-Agent": 'Mozilla/5.0  \
    (Windows NT 6.3; WOW64) AppleWebKit/537.36  \
    (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}


# Asiapharmaceutics/ html/ directory create method
def gzip_collection(url, target_path, agent=agent):

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    url_get3 = requests.get(url, headers=agent, timeout=120)
    name_url = url_get3.url
    name = name_url.replace('/', '-')
    url3 = url_get3.text

    soup3 = BeautifulSoup(url3, 'lxml')
    outfilename = target_path + "{}.html.gz".format(name)

    with gzip.open(outfilename, 'wb') as output:

        with io.TextIOWrapper(output, encoding='utf-8') as enc:
            enc.write(soup3.prettify())
            print(outfilename, 'contains', os.stat(
                outfilename).st_size, 'bytes')
            os.system('file -b --mime {}'.format(outfilename))
            print("\n" + ('-' * 80) + "\n")


def paginated_spider(url, target_path, agent=agent):
    '''
    collect the url links
    '''
    url = sys.argv[1]
    request = Request(url, headers=agent)
    urls = urlopen(request)
    soup = BeautifulSoup(urls, 'lxml')

    for li in soup.find_all("li", attrs={"id": "current"}):
        a = li.find("a")
        current = a['href']

        reqs = Request(current, headers=agent)
        urls = urlopen(reqs)
        soups = BeautifulSoup(urls, 'lxml')

        for div in soups.find_all("div", attrs={"class": "tocTitle"}):

            for a_tag in div.find_all("a"):
                article = a_tag['href']
                print(article)
                gzip_collection(article, target_path)


if __name__ == '__main__':
    # command line arguments parser
    parser = argparse.ArgumentParser()

    # get target journal
    parser.add_argument("url")
    parser.add_argument("target_path")
    args = parser.parse_args()

    # call artcle collector
    paginated_spider(args.url, args.target_path)
