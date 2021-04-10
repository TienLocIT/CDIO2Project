import bs4
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
    return bs4.BeautifulSoup(page.text, "html.parser")


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
                  "Time": ReallyTime,
                  "City": city}
        if crawl_Check(NameJob, nameCompany) == 1:
            myCol.insert_one(myDick)


def crawl_topDev():
    global JobDescription, YearOfExperience, JobType, JobRequirement, Location
    Skills = []
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
            if job.text == "Mô tả công việc":  # Nếu Thẻ <h2> có text là mô tả công việc
                job = job.findNext()  # Tìm tiếp theo của <h2>Mô tả công việc</h2>
                JobDescription = ""  # Mô tả công việc
                while job.text != "Yêu cầu công việc":  # Nếu thẻ tiếp theo mà có text là yêu cầu công việc thì stop
                    if job.findChild() is not None:  # Nếu thẻ mà có con ở trong ví dụ:UL-LI
                        JobDescription += str(job).strip()
                    job = job.findNext()
            if job.text == "Yêu cầu công việc":  # Code dưới này cũng y chang như đoạn trên
                JobRequirement = ""
                job = job.findNext()
                while job.name != "div":
                    if job.findChild() is not None:
                        JobRequirement += str(job).strip()
                    job = job.findNext()
        anotherInformation = soupDescription.find("div", class_="card").findAll("dt", class_="fwb")
        # Những thông tin khác như Location,Year of experience,vì nó cùng 1 class ,nên phải dung mảng
        for information in anotherInformation:
            if information.text == "Location":  # Kiểm tra text của thẻ mình tim đến
                Location = information.findNext().text.strip()
            if information.text == "Year of Experience":
                YearOfExperience = information.findNext().text.strip()
            if information.text == "Job Type":
                JobType = information.findNext("a", class_="ilabel").findChild().text.strip()
            # if(information.text=="Level"):
            # Level=information.findNext().text.strip()
            if information.text == "Skills":
                ArraySkills = information.find_all_next("a",
                                                        class_="ilabel")  # Find all next là tìm tất cả tiếp theo của
                # thẻ
                for skill in ArraySkills:
                    Skills.append(skill.findChild().text.strip())  # FindChild là tìm con của thẻ
        JobDescription += "<p>" + "YearOfExperience:" + YearOfExperience + "</p>" + "<p>" + "JobType:" + JobType + "</p>"
        myDick = {
            "NameJob": NameJob,
            "NameCompany": nameCompany,
            "ImageCompanyUrl": ImageURL,
            "JobDescription": JobDescription,
            "JobRequirements": JobRequirement,
            "Location": Location,
            "Skills": Skills
        }
        if crawl_Check(NameJob, nameCompany) == 1:
            myCol.insert_one(myDick)
crawl_topDev()
crawl_ITWork()
# myDb.Job.delete_many({})
