import wx 
import pandas as pd



class MyFrame(wx.Frame): 
	def __init__(self):
		super().__init__(parent=None, title="Data Collection Screen",size=(600,400))
		panel = wx.Panel(self )
		box = wx.BoxSizer(wx.VERTICAL)
		box2 = wx.BoxSizer(wx.HORIZONTAL)
		titleLabel = wx.StaticText(panel,-1,style=wx.ALIGN_CENTER)
		label = wx.StaticText(panel, -1, style=wx.ALIGN_LEFT)
		butt1 = wx.Button(panel, label='Add Catagories')
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
		lblList = ["Data Science", "Engineering", "Sales", "Education", "Finance", "Editorial"]

		super().__init__(parent=None, title='Select Catagories to Search', size=(600,200))
		panel = wx.Panel(self)
		box = wx.BoxSizer(wx.VERTICAL)
		panel.SetSizer(box)
		
		
		titleLabel = wx.StaticText(panel,0, style=wx.ALIGN_CENTER)

		titleTxt = "Select Categories to Search"
		titleFont = wx.Font(22,wx.ROMAN,wx.BOLD, wx.NORMAL)
		titleLabel.SetFont(titleFont)
		titleLabel.SetLabel(titleTxt)

		self.choice = wx.ComboBox(panel,choices=lblList)
		confirmButt = wx.Button(panel, label='Confirm Choice')
		confirmButt.Bind(wx.EVT_BUTTON, self.onChoice)

		box.Add(titleLabel,0,wx.ALIGN_CENTER)
		box.Add(self.choice,0, wx.ALL | wx.LEFT,5)
		box.Add(confirmButt,0, wx.ALL | wx.LEFT,5)

		self.Centre()
		self.Show()

	def onChoice(self,event):
		cityList = ['Atlanta','Boston','Chicago','Houston','Philadelphia','Seattle','Washington',"New%20York%20", "Los%20Angeles","San%20Francisco" ]
		stateList = ["GA","MA","IL","TX","PA","WA","DC", "NY", "CA", "CA"]
		api_key = "1d977e68e38ae93062c5a39f8f5ae47fdce268345d24684b08609c129a2cbcc6"
		jobs_base_url = f"https://www.themuse.com/api/public/jobs?{api_key}"
		selection = self.choice.GetValue()
		print(selection)
		dataObject = dataPull()
		locationString = dataObject.buildCitiesString(cityList,stateList)
		maxPageCount = dataObject.getMaxPageCount(jobs_base_url,locationString,selection)
		jobList = dataObject.getAllResults(jobs_base_url,maxPageCount,selection,locationString)
		job_df = pd.DataFrame(jobList)
		print(job_df)

	


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

if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	app.MainLoop()