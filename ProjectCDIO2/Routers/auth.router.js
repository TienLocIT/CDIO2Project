const controller=require("../Controllers/auth.controller")
const validate=require("../Validate/auth.roth")
const express=require("express")
const router=express.Router()
router.get("/login",controller.login)
router.post("/login",validate.postLogin,controller.postLogin)
router.get("/logout",controller.logout)
module.exports=router