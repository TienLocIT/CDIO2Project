const { response } = require("express")
require("dotenv").config()
const express=require("express")
const app=express()
const userRoute = require('./routers/user.router')
const inforRoute = require('./routers/infor.router')

const cookieparser=require("cookie-parser")
const port=3000
const db=require("./mongoDB")
const auth=require("./Routers/auth.router")
const bodyParser=require("body-parser")
const { ObjectId } = require("bson")
const jobRouter=require("./Routers/Job.router")
app.use(express.static("public"))
app.set("view engine","pug")
app.set("views","./views")
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cookieparser(process.env.SessionSecret))
app.get("/", async (req,res)=>{
    var length=(await (db.collection("Job").find({}).toArray())).length
    if(length%2==0){
        length=length
    }
    else{
        length=length+1;
    }
    res.render("index",{
         Jobs: await db.collection("Job").find({}).limit(5).toArray(),
         Jobs1:await db.collection("Job").find({}).limit(length/2).toArray(),
         Jobs2:await db.collection("Job").find({}).skip(length/2).toArray(),
         user:await await db.collection("User").findOne({_id:ObjectId(req.signedCookies.userId)})
    })
})
app.use("/auth",auth)
app.use("/work",jobRouter)
app.use('/information', inforRoute);
app.use('/users', userRoute);
app.listen(port,()=>{
    console.log("App listening at:"+port)
})
    