import wx 
import pandas as pd
import sys
from listFile import jobs_base_url
from listFile import cityList
from listFile import stateList
from listFile import catViewList
from listFile import catSendList
from listFile import jobs_base_url
from listFile import company_base_url
from museDataPull import dataPuller
from dataCleaner import ProcessData
from htmlParse import Parser

class MyFrame(wx.Frame): 
	def __init__(self):
		super().__init__(parent=None, title="Data Collection Screen",size=(800,600))
		panel = wx.Panel(self )
		box = wx.BoxSizer(wx.VERTICAL)
		box2 = wx.BoxSizer(wx.HORIZONTAL)
		titleLabel = wx.StaticText(panel,-1,style=wx.ALIGN_CENTER)
		label = wx.StaticText(panel, -1, style=wx.ALIGN_LEFT)

		panel.SetSizer(box)

		titleTxt = "The Data Condas Data Collection Tool!"
		txt1 = 'Welcome to the Data condas data collection tool'
		txt2 = "This tool collects data from the website themuse.com" 
		txt3 = "Data is pulled in through their API, processed then cleaned"
		txt = txt1 + "\n" + txt2 + "\n" + txt3
		
		titleFont = wx.Font(22, wx.ROMAN,wx.BOLD, wx.NORMAL)
		font = wx.Font(12, wx.ROMAN, wx.ITALIC, wx.NORMAL)

		titleLabel.SetFont(titleFont)
		label.SetFont(font)
		titleLabel.SetLabel(titleTxt)
		label.SetLabel(txt)

		self.choice = wx.ComboBox(panel,choices=catViewList)
		jobsButt = wx.Button(panel, label="Pull Jobs Data")
		companyButt = wx.Button(panel,label="Pull Company Data")
		processButt = wx.Button(panel,label="Process Data")
		jobsButt.Bind(wx.EVT_BUTTON, self.onChoiceJobs)
		companyButt.Bind(wx.EVT_BUTTON,self.onChoiceCompany)
		processButt.Bind(wx.EVT_BUTTON,self.onProcessData)

		self.log = wx.TextCtrl(panel, -1, size=(500,200), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
		redir = RedirectText(self.log)
		sys.stdout = redir

		box.Add(titleLabel,0,wx.ALIGN_CENTER)
		box.AddSpacer(20)
		box.Add(label,0,wx.ALIGN_LEFT)
		box.AddSpacer(50)
		box.Add(self.log,0,wx.ALIGN_CENTER)
		box.AddSpacer(15)
		box2.Add(self.choice,0, wx.ALL | wx.LEFT,5)
		box2.Add(jobsButt,0, wx.ALL | wx.LEFT,5)
		box2.Add(companyButt,0,wx.ALL | wx.LEFT,5)
		box2.Add(processButt,0,wx.ALL | wx.LEFT,5)
		box.AddSpacer(10)
		box.Add(box2,0,wx.ALL | wx.CENTER,5)

		self.Centre()
		self.Show()

	def onChoiceJobs(self,event):
		selection = self.choice.GetSelection()
		print(f"Loading job posts for category {catViewList[selection]}")
		dataObject = dataPuller()
		locationString = dataObject.buildCitiesString(cityList,stateList)
		maxPageCount = dataObject.getMaxPageCount(jobs_base_url,locationString, catSendList[selection])
		jobList = dataObject.getAllResultsJobs(jobs_base_url,maxPageCount,catSendList[selection],locationString)
		job_df = pd.DataFrame(jobList)
		job_df.to_csv("Archive/job_data.csv")
		print("")
		print(f"{len(job_df)} unique jobs loaded")
		print("")


	def onChoiceCompany(self,event):
		selection = self.choice.GetSelection()
		print(f"Loading company data for category {catViewList[selection]}")
		dataObject = dataPuller()
		locationString = dataObject.buildCitiesString(cityList,stateList)
		maxPageCount = dataObject.getMaxPageCount(jobs_base_url,locationString, catSendList[selection])
		companyList = dataObject.getAllResultsCompanies(company_base_url,maxPageCount,locationString,catSendList[selection])
		company_df = pd.DataFrame(companyList)
		company_df.to_csv("Archive/company_data.csv")
		print("")
		print(f"{len(company_df)} unique companies loaded")

	def onProcessData(self,event):
		cleaner = ProcessData()
		parser = Parser()
		print("")
		print("Merging Files....")
		print("")
		job_df = pd.read_csv("Archive/job_data.csv")
		company_df = pd.read_csv("Archive/company_data.csv")
		
		job_df = cleaner.dropUnwantedColumns(job_df)
		company_df = cleaner.dropUnwantedColumns(company_df)

		merged_df = cleaner.mergeAndSplitLocation(job_df, company_df)
		clean_merged_df = cleaner.renameJobs(merged_df)
		clean_merged_df = parser.parseHtml(clean_merged_df)
		clean_merged_df = cleaner.cleanValues(clean_merged_df)
		clean_merged_df = parser.parseHtml(clean_merged_df)
		clean_merged_df.to_csv("job_company_merged_data.csv")

class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)


if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	app.MainLoop()