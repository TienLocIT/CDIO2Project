const express = require("express");
const router = express.Router();
const controller = require('../Controllers/infor.controllers')
// var validate = require('../validations/user.validation')
 
// create application/x-www-form-urlencoded parser
router.get("/:id", controller.information);
router.post("/:id",controller.postInformation);
module.exports = router;