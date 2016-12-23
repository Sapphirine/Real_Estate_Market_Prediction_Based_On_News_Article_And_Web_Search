# Calculate the sentiment scores

import re
import os


count = {}
score = {}
def parse_txt(filename, keywords, score_list):
	file = open(filename)

	text = file.read()
	result = re.findall(r"[\w']+", text)

	for keyword in keywords:
		count[keyword] += result.count(keyword)
	file.close()

# load the word dictionary from the output of the PySpark WordCount
file = open('/Users/Sophie/Documents/Courses/BigData/final/code/fdesk/wcoutputwords.txt')
text1 = file.read().split('\n')
file.close()
dictionary = []
for item in text1:
	dictionary.append(item)
keywords = dictionary

# load the word score from txt file
file = open('/Users/Sophie/Documents/Courses/BigData/final/code/fdesk/wcoutputscore.txt')
text1 = file.read().split('\n')
file.close()
score_list = []
for item in text1:
	score_list.append(item)

# Traverse the online news txt files
fileNameDic = {}
dirs = '/Users/Sophie/Documents/Courses/BigData/final/dataset/onlinenews/2007-01/'
for folder in os.listdir(dirs):
	try:
		filename_list = []
		for filename in os.listdir(dirs + '/' + folder):
			if filename != '.DS_Store':
				filename_list.append(filename)
			fileNameDic[folder] = filename_list
	except OSError as err:
		print err

for folder in fileNameDic:
	for filename in fileNameDic[folder]:
		filename = ("/Users/Sophie/Documents/Courses/BigData/final/dataset/onlinenews/2007-01/" 
					+ folder + "/" + filename)
		parse_txt(filename, keywords, score_list)


# Calculate the sentiment scores for the online news 
countall = 0
sentiment_score = 0
for keyword in keywords:
	countall += count[keyword]
for keyword in keywords:
	count[keyword] = count[keyword] / float(countall)
	score[keyword] = count[keyword] * score_list[keyword]
	sentiment_score += score[keyword]
print ("sentiment_score of 2007/01 = " + str(sentiment_score))
