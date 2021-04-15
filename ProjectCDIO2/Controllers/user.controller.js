const db = require("../mongoDB");
module.exports={
    index:await function(req,res){
        res.render("users/index",{
            Users:await db.collection("users").findOne({username:req.body.username})
        })
    },
    findJob: await function(req,res,next){
        const hasSkill=false
        const  id=req.signedCookies.UserID
        const  skills=await db.collection("user").findOne({id:id}).skills
        const JobFindUser=[]
        // for(int i=0;i<skills)
        // const Jobs=await db.collection("Job").find({}).toArray()
        // for(int i=0;i<skills.length;i++){
        //     for (int j=0;j<Jobs.length;j++){
        //         for(int k=0;k<(Jobs[j].Skills).length;k++){
        //             if(skills[i]===(Jobs[j].skills)[k]){
        //                 JobFindUser.append(Jobs[j])
        //             }
        //         }
        //     }
        // }
        res.render("user/Job",{
            Jobs:JobFindUser
        })
    }
}