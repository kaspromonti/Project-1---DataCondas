#Logic written by Melissa
#Class creation and alterations to logic by Mark
#There is no reason for this class, I just wanted to get some practice

class CleanData():
    data_scientist_list=["scientist","data science","science"]
    data_engineer_list=["engineer","data engineer", "DBA"]
    data_analyst_list=["analyst","data analyst","business intelligence","analytics","analytic"]
    managerial_data_list=["director","manager","vice, president","head of","lead"]
    quant_list=["quant","research"]

    def renameJobs(self, job_data):
        indexCount = 0
        for job in job_data["job name"].tolist():
           
            job=job.replace("," ,"")
            job=job.replace(")" ,"")
            job=job.replace("(" ,"")
            job=job.replace("-" ,"")
            job_word=job.lower().split(" ")
            other_exists=True
            for word in job_word:
                if word in self.data_scientist_list:
                    job_data.loc[indexCount, "simple name"] = "Data Scientist"
                    other_exists=False
                    indexCount+=1
                    break
                elif word in self.data_engineer_list:
                    job_data.loc[indexCount, "simple name"]  = "Data Engineer"
                    other_exists=False
                    indexCount+=1
                    break
                elif word in self.data_analyst_list:
                    job_data.loc[indexCount, "simple name"]  = "Data Analyst"
                    other_exists=False
                    indexCount+=1
                    break
                elif word in self.managerial_data_list:
                    job_data.loc[indexCount, "simple name"]  = "Managerial"
                    other_exists=False
                    indexCount+=1
                    break
                elif word in self.quant_list:
                    job_data.loc[indexCount, "simple name"]  = "Quantitive/Research"
                    other_exists=False
                    indexCount+=1
                    break
            if other_exists == True:
             job_data.loc[indexCount, "simple name"]  = "Other"
             indexCount+=1
                #print(indexCount)

        return job_data