const express=require("express")
const router=express.Router()
const controller=require("../Controllers/Job.controller")
router.get("/:id",controller.view)