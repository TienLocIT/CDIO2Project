const controller=require("../Controllers/user.controller")
const express=require("express")
const multer=require("multer")
const router=express.Router()
const upload = multer({ dest: './public/uploads/' })
router.get("/create",controller.create);
router.post("/create", upload.single('avatar'),controller.postCreate);

module.exports = router;