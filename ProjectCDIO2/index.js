const express=require("express")
const app=express()
const port=5000
const db=require("./mongoDB")
const userRoute = require('./routers/user.router')
const inforRoute = require('./routers/infor.router')
app.use(express.static('public'))
app.set("view engine","pug")
app.set("views","./views")
app.get("/",async (req,res)=>{
    res.render("index",{
       Jobs:await db.collection("Job").find({}).toArray()
    })
})
app.use('/information', inforRoute);
app.use('/users', userRoute);

app.listen(port,()=>{
    console.log("App listening at:"+port)
})