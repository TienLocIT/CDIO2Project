const express=require("express")
const app=express()
const port=3000
const db=require("./mongoDB")
app.set("view engine","pug")
app.set("views","./views")
app.get("/",async (req,res)=>{
    res.render("index",{
       Jobs:await db.collection("Job").find({}).toArray()
    })
})
app.listen(port,()=>{
    console.log("App listening at:"+port)
})