const db = require("../mongoDB")
module.exports.postLogin=async function (req,res,next)
{
    var userRequire="",passwordrequire="";
    var user=await db.collection("User").findOne({username:req.body.name})
    if(!req.body.name){
        userRequire="Username is Require"
    }
    if(!req.body.password){
        passwordrequire="Password is Require"
    }
    if(userRequire!==""&& passwordrequire!==""){
        res.render("auth/login",{
            userRequire:userRequire,
            passwordrequire:passwordrequire
        })
    }
    if(!user){
        res.render("auth/login",{
            userError:"User is not exits",
            userRequire:userRequire,
            values:req.body
        })
        return
    }
    if(user.password!==req.body.password||req.body.password===""){
        res.render("auth/login",{
            passworderror:"Wrong Password",
            passwordrequire:passwordrequire,
            values:req.body
        })
        return
    }
    res.cookie("userId",user._id,{
        signed:true
    })
    next()
}