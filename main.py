import bs4
import requests
import pymongo

Description = []
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["FindingJob"]
mycol = mydb["Job"]
url = 'https://itviec.com/viec-lam-it'


def getpagecontent(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    return BeautifulSoup(page.text, "html.parser")


soup = getpagecontent(url)
divtags = soup.findAll("div", class_="job_content")
for divtag in divtags:
    NameJob = divtag.find("h2", class_="title").text.strip()
    city = divtag.find("div", class_="city").text.strip()
    # NameJob.replace('\r\n', ' $ ')
    Skills = []
    Skill = divtag.find("div", class_="job-bottom").find("div", class_="tag-list").findAll("a", class_="mkt-track")
    for skills in Skill:
        Skills.append(skills.find("span").text.replace("\n", ""))
    PathURL = "https://itviec.com/" + divtag.find("h2", class_="title").find("a")["href"]
    soup1 = getpagecontent(PathURL)
    divtagssoup1 = soup1.find("div", class_="job-details")
    SVGIcon = divtagssoup1.find("div", class_="job-details__overview").findAll("div", class_="svg-icon")
    for svgicon in SVGIcon:
        for svgicon1 in svgicon.findAll("div", class_="svg-icon__text"):
            if (svgicon1.find("span") != None):
                Location = svgicon1.find("span").text
    Location.replace("\n", "")
    Time = divtagssoup1.find("div", class_="job-details__overview").find("div", class_="svg-icon--blue")
    ReallyTime = Time.find("div", class_="svg-icon__text").text.strip()
    Jobdetails = divtagssoup1.findAll("div", class_="job-details__paragraph")
    DescriptionJob = str(Jobdetails[0].find("p"))
    RequirementJob = str(Jobdetails[1].find("p"))
    mydick = {"NameJob": NameJob,
              "JobDescription": DescriptionJob,
              "JobRequirements": RequirementJob,
              "Location": Location,
              "Skills": Skills,
              "Time": ReallyTime,
              "City": city}
    mycol.insert_one(mydick)
