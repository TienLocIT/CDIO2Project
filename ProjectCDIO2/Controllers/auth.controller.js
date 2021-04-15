const db=require("../mongoDB")
module.exports={
    register:(req,res)=>{
        res.render("auth/signup")
    },
    login:(req,res)=>{
        res.render("auth/login")
    },
    postLogin:async (req,res)=>{
        res.redirect("/")
    }
}