const controller=require("../Controllers/auth.controller")
const validate=require("../Validate/auth.roth")
const express=require("express")
const router=express.Router()
router.get("/signup",controller.register)
router.get("/login",controller.login)
router.post("/login",validate.postLogin,controller.postLogin)
module.exports=router