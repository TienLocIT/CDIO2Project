const db = require("../mongoDB");

module.exports={
    view: await function (req,res,next){
        var id=req.params.id;
        var job=async (db.collection("Job").find({id:id}))
        res.render("Jobs/view",{
            Job:job
        })
    }
}   