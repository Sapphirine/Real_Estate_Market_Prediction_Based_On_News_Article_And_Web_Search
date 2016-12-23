#!/usr/bin/python -tt

import requests
import re
import csv
from bs4 import BeautifulSoup
import os
import time
import random
import sys

#.csv file writer
def ofile_writer(name, data_writer):
   f = open(name, "w")
   
   writer = f.write(data_writer)

   f.close()

#single page of news we collect
#out put them as .txt file
def single_newspage(homepage):
    url = homepage
    ofile_name = time +'.txt'

    try:
        html = requests.get(url)

        #using Beautiful Soup
        soup = BeautifulSoup(html.text,"html.parser")

        #find article
        article = soup.find('article')

        #colloect all the paragraph
        paragraphs = article.find_all('p')
        record_article = ''
        
        if paragraphs:

            for paragraph in paragraphs:
                try:
                    record_article = record_article + '\n' + paragraph.string
                except AttributeError as err:
                    print (err)

        ofile_writer(ofile_name, record_article)
    except requests.exceptions.HTTPError as err:
        print (err)
        print ('unable to access' + homepage)

def main():
    url_list = []
    time_list = []
    open('real-estate.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            url_list.append(row['url'])
            time_list.append(row['date'])

    for url in url_list:
        for time in time_list:
            single_newspage(url, time)

if __name__=='__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()