const db = require("../mongoDB");
module.exports={
    findJob: async function(req,res,next){
        const hasSkill=false
        const  id=req.signedCookies.UserId
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
    },
    create:function (req, res) {
        res.render("user/create");
    },
    postCreate: async function (req, res) {
        if(!req.file)
          req.body.avatar = "uploads\\26306066987a80ca8a795e384c726bc9";
        else   
          req.body.avatar = req.file.path.split('\\').slice(1).join('\\');
        db.collection("User").insertOne(req.body)
        .catch(error => console.error(error))
        const user= await db.collection("User").findOne({userName:req.body.userName})
        res.redirect("/information/"+user._id);
      }
}