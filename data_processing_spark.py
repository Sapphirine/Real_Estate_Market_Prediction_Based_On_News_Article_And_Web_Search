# Processing data using nlp toolkit and using PySpark
# to paralyzingly process all the articles
#
# -*- coding: utf-8 -*-
#
# Executing Pyspark on local machine
# 
# ./bin/spark-submit /Users/Sophie/Desktop/data_processing_spark.py 


from pyspark import SparkContext, RDD
import sys
from operator import add

import csv
import re
import os

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

reload(sys)
sys.setdefaultencoding('utf-8')

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

dictionary = []

def changeTextFileToRDD(filename):
	file = open(filename)
	text = file.read().split("\n")
	file.close()
	
	texts = []

	for i in text:  
		# clean and tokenize document string
		raw = i.lower()
		tokens = tokenizer.tokenize(raw)

		if tokens:
			# remove stop words from tokens
			# stopped_tokens = [i for i in tokens if not i in en_stop]
			stopped_tokens = []
			for i in tokens:
				if not i in en_stop:
					try:
						stopped_tokens.append(i)
					except UnicodeDecodeError as err:
						print err

			# stem tokens
			# stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
			stemmed_tokens = []
			for i in tokens:
				if not i in en_stop:
					try:
						stemmed_tokens.append(i)
					except UnicodeDecodeError as err:
						print err

			# add tokens to list
			texts.append(stemmed_tokens)
			

	# change list to RDD 
	text_file = sc.parallelize(texts)	

	text_file = text_file.flatMap(lambda x: x) \
						 .filter(lambda x: x in dictionary) \
						 .map(lambda word: (word, 1)) \
		 				 .reduceByKey(lambda a, b: a + b)
	
	return text_file

#load provided word dictionary
def createDictionary():
	file = open('/Users/Sophie/Documents/Courses/BigData/final/code/fdesk/positive-words.txt')
	text1 = file.read().split('\n')
	file.close()

	file = open('/Users/Sophie/Documents/Courses/BigData/final/code/fdesk/negative-words.txt')
	text2 = file.read().split('\n')
	file.close()

	dictionary = []
	for item in text1:
		dictionary.append(item)
	for item in text2:
		dictionary.append(item)
	return dictionary

## main call ##
dictionary = createDictionary()

fileNameDic = {}
dirs = '/Users/Sophie/Documents/Courses/BigData/final/dataset/onlinenews/'
for folder in os.listdir(dirs):
	try:
		filename_list = []
		for filename in os.listdir(dirs + '/' + folder):
			if filename != '.DS_Store':
				filename_list.append(filename)
			fileNameDic[folder] = filename_list
	except OSError as err:
		print err
#print fileNameDic

# Create a spark context 
sc = SparkContext("local", "testWordCountApp")

#initialize an pipeRDD from a single txt file
filename = "/Users/Sophie/Documents/Courses/BigData/final/dataset/init.TXT"
new_text_file0 = changeTextFileToRDD(filename)
new_text_file = new_text_file0

newlist = []
i = 0
for folder in fileNameDic:
	# print folder
	for filename in fileNameDic[folder]:
		#print filename
		filename = ("/Users/Sophie/Documents/Courses/BigData/final/dataset/onlinenews/" 
					+ folder + "/" + filename)
		text_file = changeTextFileToRDD(filename)

		new_text_file = new_text_file.union(text_file)
		new_text_file = new_text_file.reduceByKey(lambda a, b: a + b)
		if i > 100:
			i = 0
			newlist.append(new_text_file)
			new_text_file = new_text_file0
		i = i + 1
	newlist.append(new_text_file)
	break
	print newlist

pipeRDD = newlist[0]
for i in range(1,len(newlist)):
	pipeRDD = pipeRDD.union(newlist[i])
	pipeRDD = pipeRDD.reduceByKey(lambda a, b: a + b)

counts = pipeRDD
output = counts.collect()
wordlist = { wordcount[0]:wordcount[1] for wordcount in output }
print wordlist

sc.stop()

f = open('/Users/Sophie/Documents/Courses/BigData/final/code/wcoutput.csv', "w")
writer = csv.writer(f, delimiter = ',')
data_writer = [ [key, wordlist[key]] for key in wordlist.keys() ]
for row in data_writer:
	writer.writerow(row)
f.close()





