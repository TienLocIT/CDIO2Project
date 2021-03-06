
from bs4 import BeautifulSoup
import requests
import pymongo
MyClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDb = MyClient["Findingjob"]
myCol = myDb["Job"]
url = 'https://itviec.com/viec-lam-it'
urlTopDev = "https://topdev.vn/viec-lam-it"


def crawl_Check(nameJob, nameCompany):
    if myCol.find_one({"NameJob": nameJob}) is not None:
        if myCol.find_one({"NameCompany": nameCompany}) is not None:
            return 0
        else:
            return 1
    return 1


def getPageContent(URL):
    page = requests.get(URL, headers={"Accept-Language": "en-US"})
    return BeautifulSoup(page.text, "html.parser")

def TestArray(arrays,value):
    dem=0;
    for array in arrays:
        if(array==value):
            dem+=1
    return dem
def crawl_ITWork():
    global Location
    soup = getPageContent(url)
    divTags = soup.findAll("div", class_="job_content")
    for divTag in divTags:
        NameJob = divTag.find("h2", class_="title").text.strip()
        city = divTag.find("div", class_="city").text.strip()
        ImageCompanyUrl = divTag.find("div", class_="logo-wrapper").find("a").find("img")["data-src"]
        Skills = []
        Skill = divTag.find("div", class_="job-bottom").find("div", class_="tag-list").findAll("a", class_="mkt-track")
        for skills in Skill:
            Skills.append(skills.find("span").text.replace("\n", ""))
        PathURL = "https://itviec.com/" + divTag.find("h2", class_="title").find("a")["href"]
        soup1 = getPageContent(PathURL)
        divTagSoup = soup1.find("div", class_="job-details")
        nameCompany = divTagSoup.find("div", class_="job-details__sub-title").text.strip()
        svgIcon = divTagSoup.find("div", class_="job-details__overview").findAll("div", class_="svg-icon")
        for svgIcons in svgIcon:
            for svgIcons1 in svgIcons.findAll("div", class_="svg-icon__text"):
                if svgIcons1.find("span") is not None:
                    Location = svgIcons1.find("span").text.strip()
        Time = divTagSoup.find("div", class_="job-details__overview").find("div", class_="svg-icon--blue")
        ReallyTime = Time.find("div", class_="svg-icon__text").text.strip()
        jobDetails = divTagSoup.findAll("div", class_="job-details__paragraph")
        DescriptionJob = str(jobDetails[0].findNext())
        RequirementJob = str(jobDetails[1].findNext())
        myDick = {"NameJob": NameJob,
                  "NameCompany": nameCompany,
                  "ImageCompanyUrl": ImageCompanyUrl,
                  "JobDescription": DescriptionJob,
                  "JobRequirements": RequirementJob,
                  "Location": Location,
                  "Skills": Skills,
                  "YearOfExperience":"",
                  "JobType":""
                  }
        if crawl_Check(NameJob, nameCompany) == 1:
            myCol.insert_one(myDick)
        Skills.clear()


def crawl_topDev():
    global JobDescription, YearOfExperience, JobType, JobRequirement, Location
    
    soupTopDev = getPageContent(urlTopDev)
    linkWorkTopDev = soupTopDev.findAll("a", class_="job-title")
    for link in linkWorkTopDev:
        soupDescription = getPageContent(link["href"])
        ImageURL = soupDescription.find("div", class_="card").find("div", class_="logo-com").findNext("img")[
            "src"].strip()
        nameCompany = soupDescription.find("div", class_="card").find("div", class_="wrap-cont").find("p").text.strip()
        NameJob = soupDescription.find("div", class_="card").find("div", class_="logo-com").find("img")["alt"].strip()
        Jobs = soupDescription.find("div", class_="card").find("div", class_="wrap-cont-job").findAll("h2",
                                                                                                      class_="fz17")
        
        for job in Jobs:
            if job.text == "M?? t??? c??ng vi???c":  # N???u Th??? <h2> c?? text l?? m?? t??? c??ng vi???c
                job = job.findNext()  # T??m ti???p theo c???a <h2>M?? t??? c??ng vi???c</h2>
                JobDescription = []
                for i in job.findAll("li"):
                    JobDescription.append(i.text.strip())
                 # M?? t??? c??ng vi???c
                # while job.text != "Y??u c???u c??ng vi???c":  # N???u th??? ti???p theo m?? c?? text l?? y??u c???u c??ng vi???c th?? stop
                #     if job.findChild("") is not None:  # N???u th??? m?? c?? con ??? trong v?? d???:UL-LI
                       
                #         if(TestArray(JobDescription,job.text)==0):
                #             JobDescription.append(job.text.strip())
                #     job = job.findNext()
            if job.text == "Y??u c???u c??ng vi???c":  # Code d?????i n??y c??ng y chang nh?? ??o???n tr??n
                JobRequirement = []
                job = job.findNext()
                # print(job.findAll("li"))
                for i in job.findAll("li"):
                     JobRequirement.append(i.text.strip())
                # while job.name != "div":
                #     if job.findChild() is not None:
                #         JobRequirement += str(job).strip()
                #     job = job.findNext()
        anotherInformation = soupDescription.find("div", class_="card").findAll("dt", class_="fwb")
        # Nh???ng th??ng tin kh??c nh?? Location,Year of experience,v?? n?? c??ng 1 class ,n??n ph???i dung m???ng
        for information in anotherInformation:
            Skills = []
            if information.text == "Location":  # Ki???m tra text c???a th??? m??nh tim ?????n
                Location = information.findNext().text.strip()
            if information.text == "Year of Experience":
                YearOfExperience = information.findNext().text.strip()
            if information.text == "Job Type":
                JobType = information.findNext("a", class_="ilabel").findChild().text.strip()
            # if(information.text=="Level"):
            # Level=information.findNext().text.strip()
            if information.text == "Skills":
                ArraySkills = information.findNext("div",class_="tag-list").findChildren("a")  # Find all next l?? t??m t???t c??? ti???p theo c???a
                # th???
            
                for skill in ArraySkills:
                    Skills.append(skill.findChild().text.strip())  # FindChild l?? t??m con c???a th???
        myDick = {
            "NameJob": NameJob,
            "NameCompany": nameCompany,
            "ImageCompanyUrl": ImageURL,
            "JobDescription": JobDescription,
            "JobRequirements": JobRequirement,
            "Location": Location,
            "Skills": Skills,
            "YearOfExperiece":YearOfExperience,
            "JobType":JobType
        }
        if crawl_Check(NameJob, nameCompany) == 1:
            myCol.insert_one(myDick)
        Skills.clear()
crawl_topDev()
crawl_ITWork()
print("test")
# myDb.Job.delete_many({})