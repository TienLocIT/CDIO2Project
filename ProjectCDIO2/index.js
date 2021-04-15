const { response } = require("express")
require("dotenv").config()
const express=require("express")
const app=express()
const bodyParser=require("body-parser")
const cookieparser=require("cookie-parser")
const port=3000
const db=require("./mongoDB")
const auth=require("./Routers/auth.router")
const { ObjectId } = require("bson")

app.use(express.static("public"))
app.set("view engine","pug")
app.set("views","./views")
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cookieparser(process.env.SessionSecret))
app.get("/", async (req,res)=>{
    res.render("index",{
         Jobs1: await db.collection("Job").find({}).limit(5).toArray(),
         Jobs:await db.collection("Job").find({}).toArray(),
         user:await await db.collection("User").findOne({_id:ObjectId(req.signedCookies.userId)})
    })
})
app.use("/auth",auth)
app.listen(port,()=>{
    console.log("App listening at:"+port)
})