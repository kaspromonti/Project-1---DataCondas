import requests 
import pandas as pd
import json
from pprint import pprint 
from config import api_key 

api_key = api_key
jobs_base_url = f"https://www.themuse.com/api/public/jobs?{api_key}"
category = "category=Data%20Science"
cityList = ['Atlanta','Boston','Chicago','Houston','Philadelphia','Seattle','Washington',"New%20York", "Los%20Angeles","San%20Francisco" ]
stateList = ["GA","MA","IL","TX","PA","WA","DC", "NY", "CA", "CA"]

def getMaxPageCount(base_url,locationString): 
	page = "page=1"
	response = requests.get(f"{base_url}{category}&{locationString}&{page}").json()
	maxPageCount = response["page_count"]
	print(maxPageCount)
	
	return maxPageCount

def buildCitiesString(cityList, stateList):
	seperator = "%2C%20"
	finalCityURLString = ''
	for x in range(len(cityList)):
		finalCityURLString += f"location={cityList[x]}{seperator}{stateList[x]}&"
	return finalCityURLString
 
def getAllResults(base_url, maxPageCount, category, locationString): 
	jobList = []
	pageCount = 1
	page = "&page="
	while pageCount <= maxPageCount:
		resultNum = 0
		
		response = requests.get(f"{base_url}{category}{page}{pageCount}&{locationString}").json()
		print(f"Loading requests from page {pageCount}")
		while resultNum < 20:
			jobs_dict = {"job id": '',
				 "job level": '',
				 "location": '',
				 "job name": '',
				 "post date": '',
				 "landing page": '',
				 "category": '',
				 "company id": '',
				 "company name": '',
				 "content": '',
			}
			try:
				jobs_dict["location"] = response["results"][resultNum]["locations"][0]["name"]
				jobs_dict["job id"] = response["results"][resultNum]["id"]
				jobs_dict["job level"] = response["results"][resultNum]["levels"][0]["name"]
				jobs_dict["job name"] = response["results"][resultNum]["name"]
				jobs_dict["post date"] = response["results"][resultNum]["publication_date"]
				jobs_dict["landing page"] = response["results"][resultNum]["refs"]["landing_page"]
				jobs_dict["category"] = response["results"][resultNum]["categories"][0]["name"]
				jobs_dict["company id"] = response["results"][resultNum]["company"]["id"]
				jobs_dict["company name"] = response["results"][resultNum]["company"]["name"]
				jobs_dict["contents"] = response["results"][resultNum]["contents"]
		
			except (KeyError,IndexError):
				print("Missing Location... skipping")
				pass
			
			

			jobList.append(jobs_dict)
			resultNum += 1
		pageCount += 1
	return jobList

locationString = buildCitiesString(cityList,stateList)
maxPageCount = getMaxPageCount(jobs_base_url,locationString)

jobList = getAllResults(jobs_base_url, maxPageCount, category, locationString)
job_df = pd.DataFrame(jobList)
job_df.to_csv("job_data_science.csv")
print(job_df)