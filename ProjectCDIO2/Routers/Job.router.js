const express=require("express")
const router=express.Router()
const controller=require("../Controllers/Job.controller")
// router.get("/:id",controller.view)
router.get("/",controller.findingJob)
router.get("/search/",controller.searchingJob)
router.get("/:id",controller.inforJob)
module.exports=router