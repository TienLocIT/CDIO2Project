const { ObjectId } = require("bson");
const db = require("../mongoDB")

module.exports={
information:async function (req, res) {
    res.render("user/information",{
      user:await db.collection("User").findOne({_id:ObjectId(req.params.id)})
    })
 },
postInformation:async function (req, res) {
     var skill=[]
     const user=await db.collection("User").findOne({_id:ObjectId(req.params.id)})
    for (const i of req.body.skill){
      if(i!=""){
        skill.push(i)
      }
    }
    req.body.skill=skill;
     await db.collection("User").updateOne({_id:ObjectId(req.params.id)},{
       $set:req.body},{multi:true}).catch(error => console.error(error))
    res.cookie("userId",user._id,{
        signed:true
    })
    res.redirect("/"); 
  }
}