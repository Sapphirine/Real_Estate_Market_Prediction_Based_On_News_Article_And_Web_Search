# Obtain the url address of online articles

import csv
import json
from nytimesarticle import articleAPI
api = articleAPI('Your API Key')

# articles = api.search( q = 'Real Estate', 
#      fq = {'headline':'Real Estate', 'source':['Reuters','AP', 'The New York Times']}, 
#      begin_date = 20111231 )
# print json.dumps(articles)

def parse_articles(articles):
    '''
    This function takes in a response to the api and parses
    the articles into a list of dictionaries
    '''

    news = []
    for i in articles['response']['docs']:
        dic = {}
        dic['id'] = i['_id']
        if i['abstract'] is not None:
            dic['abstract'] = i['abstract'].encode("utf8")
        dic['headline'] = i['headline']['main'].encode("utf8")
        dic['desk'] = i['news_desk']
        dic['date'] = i['pub_date'][0:6] # cutting time of day. 0:10
        dic['section'] = i['section_name']
        if i['snippet'] is not None:
            dic['snippet'] = i['snippet'].encode("utf8")
        dic['source'] = i['source']
        dic['type'] = i['type_of_material']
        dic['url'] = i['web_url']
        dic['word_count'] = i['word_count']
        # locations
        locations = []
        for x in range(0,len(i['keywords'])):
            if 'glocations' in i['keywords'][x]['name']:
                locations.append(i['keywords'][x]['value'])
        dic['locations'] = locations
        # subject
        subjects = []
        for x in range(0,len(i['keywords'])):
            if 'subject' in i['keywords'][x]['name']:
                subjects.append(i['keywords'][x]['value'])
        dic['subjects'] = subjects   
        news.append(dic)
    return(news) 

def get_articles(date,query):
    '''
    This function accepts a year in string format (e.g.'2016')
    and a query (e.g.'Real Estate') and it will 
    return a list of parsed articles (in dictionaries)
    for that year.
    '''
    all_articles = []
    api = articleAPI('Your API key')
    for i in range(0,99): #NYT limits pager to first 100 pages. But rarely will you find over 100 pages of results anyway.
        articles = api.search( q = 'RealEstate',
               fq = {'headline':'RealEstate','source':['Bloomberg','Wall Street Journal', 'The New York Times']},
               begin_date = 20070101 )#date + '0101',
               #end_date = date + '1231')
               #sort='oldest')
               #page = str(i))
        articles = parse_articles(articles)

        all_articles = all_articles + articles
    return(all_articles)

RealEstate_all = []
for i in range(2007,2017):
    print 'Processing' + str(i) + '...'
RealEstate_year =  get_articles(str(i),'Real Estate')
RealEstate_all = RealEstate_all + RealEstate_year

keys = RealEstate_all[0].keys()
with open('real-estate.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(RealEstate_all)