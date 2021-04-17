const { ObjectId } = require("bson");
const db = require("../mongoDB");
const cookieparser=require("cookie-parser");
function testInArray(i,j){
    var dem=0;
        for(const l of j){
            if(l.NameCompany===i){
                dem++;
            }
        }
    return dem;
}
async function userJobs(id){
    const userSkills=(await db.collection("User").findOne({_id:ObjectId(id)})).Skills
        const Jobs=[]
        const listJob=await db.collection("Job").find({}).toArray()
        for (const i of userSkills){
            for(const j of listJob){
                if((j.Skills).indexOf(i)!==-1){
                    if(testInArray(j.NameCompany,Jobs)==0){
                        Jobs.push(j)
                    }   
            }
        }
    return Jobs;
}
}
module.exports={
    findingJob:async function(req,res,next){
        const cookieUser=req.signedCookies.userId;
        const Jobs=(cookieUser===undefined)?await db.collection("Job").find({}).toArray():await userJobs(cookieUser)
        console.log(cookieUser)
        res.render("Work/index",{
            Jobs:Jobs
        })
    },
    searchingJob:async function(req,res){
         var work=req.query.work
        // if(work==""){
        //     Jobs=await db.collection("Job").find({}).toArray()
        // }
        // else{
        //     Jobs=await db.collection("Job").find({Skills:work}).toArray()
        // }
        res.render("Work/index",{
            Jobs:await db.collection("Job").find({Skills:work}).toArray()
        })
    },
    inforJob:async function(req,res,next){
         const Job=await db.collection("Job").findOne({_id:ObjectId(req.params.id)})
         const Jobs=await db.collection("Job").find({NameCompany:Job.NameCompany}).skip(1).toArray()
         const NameCompany=Job.NameCompany.toLowerCase()
        res.render("Work/inforJob",{ 
            Job:Job,
            Jobs:Jobs,
            NameCompany:NameCompany
        })
    },
   
}   