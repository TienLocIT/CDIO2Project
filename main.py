
<<<<<<< HEAD
import  bs4
import  requests
import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["Findingjob"]
=======
import  bs4;
import  requests;
import pymongo;
Description=[];
myclient=pymongo.MongoClient("mongodb://localhost:27017/");
mydb=myclient["FindingJob"];
>>>>>>> bf44d8663ef0c46bfd09058f3dc7326416e7fc70
mycol=mydb["Job"]
url='https://itviec.com/viec-lam-it'
urltopdev="https://topdev.vn/viec-lam-it"
def getpagecontent(url):
     page=requests.get(url,headers={"Accept-Language":"en-US"})
     return bs4.BeautifulSoup(page.text,"html.parser")
<<<<<<< HEAD
# def craw_Itwork():
#     soup=getpagecontent(url);
#     divtags=soup.findAll("div",class_="job_content")
#     for divtag in divtags:
#           NameJob=divtag.find("h2",class_="title").text;
#           city=divtag.find("div",class_="city").text;
#           NameJob.replace('\r\n', ' $ ');
#           city.replace("\n","");
#           Skills=[];
#           Skill=divtag.find("div",class_="job-bottom").find("div",class_="tag-list").findAll("a",class_="mkt-track")
#           for skills in Skill:
#               Skills.append(skills.find("span").text.replace("\n",""))
#           PathURL="https://itviec.com/"+divtag.find("h2",class_="title").find("a")["href"];
#           soup1=getpagecontent(PathURL);
#           divtagssoup1=soup1.find("div",class_="job-details");
#           SVGIcon=divtagssoup1.find("div",class_="job-details__overview").findAll("div",class_="svg-icon")
#           for svgicon in SVGIcon:
#               for svgicon1 in svgicon.findAll("div",class_="svg-icon__text"):
#                   if(svgicon1.find("span")!=None):
#                     Location=svgicon1.find("span").text;
#           Location.replace("\n","");
#           Time=divtagssoup1.find("div",class_="job-details__overview").find("div",class_="svg-icon--blue")
#           ReallyTime=Time.find("div",class_="svg-icon__text").text
#           ReallyTime.replace("\n","");
#           Jobdetails=divtagssoup1.findAll("div",class_="job-details__paragraph")
#           DescriptionJob=str(Jobdetails[0].find("p"))
#           RequirementJob=str(Jobdetails[1].find("p"))
#           mydick={"NameJob":NameJob,
#                 "JobDescription":DescriptionJob,
#                  "JobRequirements":RequirementJob,
#                 "Location":Location,
#                 "Skills":Skills,
#                 "Time":ReallyTime,
#                 "City":city}
#           mycol.insert_one(mydick)
def crawl_topdev():
    Skills=[]
    soupTopdev=getpagecontent(urltopdev)
    linkWorkTopdev=soupTopdev.findAll("a",class_="job-title")
    for link in linkWorkTopdev:
        NameCompany=[]
        soupDescription=getpagecontent(link["href"])
        ImageURL=soupDescription.find("div",class_="card").find("div",class_="logo-com").findNext("img")["src"].strip()
        AboutCompany=soupDescription.find("div",class_="card").find("div",class_="wrap-cont").findAll("p")
        for company in AboutCompany:
            NameCompany.append(company.text.strip())
        NameJob=soupDescription.find("div",class_="card").find("p",class_="comp-name").text.strip()
        Jobs=soupDescription.find("div",class_="card").find("div",class_="wrap-cont-job").findAll("h2",class_="fz17")
        for job in Jobs:
            if(job.text=="Mô tả công việc"): #Nếu Thẻ <h2> có text là mô tả công việc
                job = job.findNext() #Tìm tiếp theo của <h2>Mô tả công việc</h2>
                JobDescription=""; #Mô tả công việc
                while(job.text!="Yêu cầu công việc"): #Nếu thẻ tiếp theo mà có text là yêu cầu công việc thì stop
                    if (job.findChild() != None):#Nếu thẻ mà có con ở trong ví dụ:UL-LI
                            JobDescription+=str(job).strip()
                    job=job.findNext()
            if(job.text=="Yêu cầu công việc"): #Code dưới này cũng y chang như đoạn trên
                JobRequirement=""
                job=job.findNext();
                while(job.name!="div"):
                    if (job.findChild()!=None):
                       JobRequirement+=str(job).strip()
                    job=job.findNext()
        Anotherinformation=soupDescription.find("div",class_="card").findAll("dt",class_="fwb")
        #Những thông tin khác như Location,Year of experiece,vì nó cùng 1 class ,nên phải dung mảng
        for information in Anotherinformation:
            if(information.text=="Location"):#Kiểm tra text của thẻ mình tim đến
                    Location=information.findNext().text.strip()
            if(information.text=="Year of Experience"):
                    YearOfExperiene=information.findNext().text.strip()
            if(information.text=="Job Type"):
                    JobType=information.findNext("a",class_="ilabel").findChild().text.strip()
            if(information.text=="Level"):
                    Level=information.findNext().text.strip()
            if(information.text=="Skills"):
                ArraySkills=information.find_all_next("a",class_="ilabel") #Find all next là tìm tất cả tiếp theo của thẻ
                for skill in ArraySkills:
                    Skills.append(skill.findChild().text.strip())#FindChild là tìm con của thẻ
        mydick={
            "ImageURL":ImageURL,
            "NameJob":NameJob,
            "JobDescription":JobDescription,
            "JobRequirements":JobRequirement,
=======
soup=getpagecontent(url);
divtags=soup.findAll("div",class_="job_content")
for divtag in divtags:
      NameJob=divtag.find("h2",class_="title").text
      city=divtag.find("div",class_="city").text.strip()
      print(city)
      NameJob.replace('\r\n', ' $ ')
      Skills=[]
      Skill=divtag.find("div",class_="job-bottom").find("div",class_="tag-list").findAll("a",class_="mkt-track")
      for skills in Skill:
          Skills.append(skills.find("span").text.replace("\n",""))
      PathURL="https://itviec.com/"+divtag.find("h2",class_="title").find("a")["href"];
      soup1=getpagecontent(PathURL);
      divtagssoup1=soup1.find("div",class_="job-details");
      SVGIcon=divtagssoup1.find("div",class_="job-details__overview").findAll("div",class_="svg-icon")
      for svgicon in SVGIcon:
          for svgicon1 in svgicon.findAll("div",class_="svg-icon__text"):
              if(svgicon1.find("span")!=None):
                Location=svgicon1.find("span").text;
      Location.replace("\n","");
      Time=divtagssoup1.find("div",class_="job-details__overview").find("div",class_="svg-icon--blue")
      ReallyTime=Time.find("div",class_="svg-icon__text").text.strip()
      print(ReallyTime)
      Jobdetails=divtagssoup1.findAll("div",class_="job-details__paragraph")
      DescriptionJob = str(Jobdetails[0].find("p"))
      RequirementJob = str(Jobdetails[1].find("p"))
      mydick={"NameJob":NameJob,
            "JobDescription":DescriptionJob,
             "JobRequirements":RequirementJob,
>>>>>>> bf44d8663ef0c46bfd09058f3dc7326416e7fc70
            "Location":Location,
            "YearOfExperiene":YearOfExperiene,
            "JobType":JobType,
            "Level":Level,
            "Skills":Skills
        }
        mycol.insert_one(mydick)
crawl_topdev()