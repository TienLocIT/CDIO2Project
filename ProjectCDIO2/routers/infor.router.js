var express = require("express");
var router = express.Router();
var controller = require('../controllers/infor.controller')
// var validate = require('../validations/user.validation')
 
// create application/x-www-form-urlencoded parser

router.get("/information/:id", controller.information);
router.post("/information/:id", controller.postInformation);
module.exports = router;