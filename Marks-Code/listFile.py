# This file contains all the lists needed along with URLS needed to pull data
from config import api_key

api_key = api_key
jobs_base_url = f"https://www.themuse.com/api/public/jobs?{api_key}&"
company_base_url = f"https://www.themuse.com/api/public/companies?{api_key}&"

cityList = ['Atlanta','Boston','Chicago','Houston','Philadelphia','Seattle','Washington',"New%20York", "Los%20Angeles","San%20Francisco" ]
stateList = ["GA","MA","IL","TX","PA","WA","DC", "NY", "CA", "CA"]
data_scientist_list=["scientist","data science","science"]
data_engineer_list=["engineer","data engineer", "DBA"]
data_analyst_list=["analyst","data analyst","business intelligence","analytics","analytic"]
managerial_data_list=["director","manager","vice, president","head of","lead"]
quant_list=["quant","research"]
catSendList = ["Account%20Management","Business%20Strategy", "Creative%20&%20Design", "Customer%20Service", "Data%20Science", "Editorial",
		   "Education", "Engineering", "Finance", "Fundraising%20%26%20Development","Healthcare", "Medicine", "HR%20%26%20Recruiting",
		   "Legal", "Marketing%20%26%20PR", "Operations", "Project%20%26%20Product Management", "Retail", "Sales" "Social%20Media%20%26Community"]

catViewList = ["Account Management","Business Strategy", "Creative Design", "Customer Service", "Data Science", "Editorial",
		   "Education", "Engineering", "Finance", "Fundraising & Development","Healthcare", "Medicine", "HR & Recruiting",
		   "Legal", "Marketing & PR", "Operations", "Project & Product Management", "Retail", "Sales", "Social Media & Community"]


