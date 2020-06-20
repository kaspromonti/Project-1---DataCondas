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


class MyFrame(wx.Frame): 
	def __init__(self):
		super().__init__(parent=None, title="Data Collection Screen",size=(600,400))
		panel = wx.Panel(self )
		box = wx.BoxSizer(wx.VERTICAL)
		box2 = wx.BoxSizer(wx.HORIZONTAL)
		titleLabel = wx.StaticText(panel,-1,style=wx.ALIGN_CENTER)
		label = wx.StaticText(panel, -1, style=wx.ALIGN_LEFT)
		butt1 = wx.Button(panel, label='Collect Data')
		butt1.Bind(wx.EVT_BUTTON, self.CatagorySelectionPress)
		butt2 = wx.Button(panel, label='Clean Data')
		butt2.Bind(wx.EVT_BUTTON, self.dataCleanPress)

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
		

		box.Add(titleLabel,0,wx.ALIGN_CENTER)
		box.AddSpacer(20)
		box.Add(label,0,wx.ALIGN_LEFT)
		box.AddSpacer(50)
		box2.Add(butt1,0,wx.ALL | wx.CENTER,5)
		box2.Add(butt2,0,wx.ALL | wx.CENTER,5)
		box.Add(box2,wx.ALL | wx.CENTER,5)

		self.Centre()
		self.Show()
	def CatagorySelectionPress(self,event):
		CatagorySelectionScreen()

	def dataCleanPress(self,event):
		DataCleanScreen()

class CatagorySelectionScreen(wx.Frame):
	def __init__(self):
		super().__init__(parent=None, title='Select Catagories to Search', size=(600,400))
		panel = wx.Panel(self)
		box = wx.BoxSizer(wx.VERTICAL)
		box2 = wx.BoxSizer(wx.HORIZONTAL)
		panel.SetSizer(box)
	
		titleLabel = wx.StaticText(panel,0, style=wx.ALIGN_CENTER)

		titleTxt = "Data Collection Screen"
		titleFont = wx.Font(22,wx.ROMAN,wx.BOLD, wx.NORMAL)
		titleLabel.SetFont(titleFont)
		titleLabel.SetLabel(titleTxt)

		self.choice = wx.ComboBox(panel,choices=catViewList)
		jobsButt = wx.Button(panel, label="Pull Jobs Data")
		companyButt = wx.Button(panel,label="Pull Company Data")
		mergeButt = wx.Button(panel,label="Merge Data")
		jobsButt.Bind(wx.EVT_BUTTON, self.onChoiceJobs)
		companyButt.Bind(wx.EVT_BUTTON,self.onChoiceCompany)
		mergeButt.Bind(wx.EVT_BUTTON,self.onMergeData)

		self.log = wx.TextCtrl(panel, -1, size=(500,200), style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
		redir = RedirectText(self.log)
		sys.stdout = redir

		box.Add(titleLabel,0,wx.ALIGN_CENTER)
		box.AddSpacer(15)
		box.Add(self.log,0,wx.ALIGN_CENTER)
		box.AddSpacer(15)
		box2.Add(self.choice,0, wx.ALL | wx.LEFT,5)
		box2.Add(jobsButt,0, wx.ALL | wx.LEFT,5)
		box2.Add(companyButt,0,wx.ALL | wx.LEFT,5)
		box2.Add(mergeButt,0,wx.ALL | wx.LEFT,5)
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
		job_df.to_csv("Resources/job_data.csv")
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
		company_df.to_csv("Resources/company_data.csv")
		print("")
		print(f"{len(company_df)} unique companies loaded")

	def onMergeData(self,event):
		job_df = pd.read_csv("Resources/job_data.csv")
		company_df = pd.read_csv("Resources/company_data.csv")
		job_df = job_df.drop(["Unnamed: 0"],axis=1)
		company_df = company_df.drop(["Unnamed: 0"],axis=1)

		merged_df = job_df.merge(company_df, on="company id", how="left")
		merged_df[["city", "state"]] = merged_df.location.str.split(", ", expand=True,)
		# print(merged_df)

		# merged_df = merged_df[merged_df["job id"] != '']
		merged_df.to_csv("job_company_merged_data.csv")


class DataCleanScreen(wx.Frame):
	def __init__(self):
		super().__init__(parent=None, title='Data Cleaning Screen', size=(600,400))
		panel = wx.Panel(self)
		box = wx.BoxSizer(wx.VERTICAL)
		titleLabel = wx.StaticText(panel,-1, style=wx.ALIGN_CENTER)
		titleTxt = "Define Search Tearms"
		titleFont = wx.Font(22,wx.ROMAN,wx.BOLD, wx.NORMAL)
		titleLabel.SetFont(titleFont)
		titleLabel.SetLabel(titleTxt)

		box.Add(titleLabel,0,wx.ALIGN_CENTER)


		self.Show()

class RedirectText(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)


if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	app.MainLoop()