const db=require("../mongoDB")
module.exports={
    login:(req,res)=>{
        res.render("auth/login")
    },
    postLogin:async (req,res)=>{
        res.redirect("/")
    },
    logout:async (req,res)=>{
        res.clearCookie("userId")
        res.redirect("/")
    }
}