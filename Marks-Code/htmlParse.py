import pandas as pd 
from html.parser import HTMLParser 

jobs_df = pd.read_csv("job_company_merged_data.csv")
jobContent = jobs_df["contents"]
print(jobContent)
print(jobContent[1])

class htmlParser(HTMLParser):
	def startTags(self, tag,attrs):
		print(f"Starting Tag: {tag}")
	def endTag(self,tag):
		print(f"End Tag: {tag}")
	def parseData(self,data):
		print(f"Data: {data}")

parser = htmlParser()

for x in range(len(jobContent)): 
	htmlToParse = jobContent[x]
	parser.feed(htmlToParse)
