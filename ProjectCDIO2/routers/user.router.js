var express = require("express");
var multer  = require('multer');
var router = express.Router();
var controller = require('../controllers/user.controller')
// var validate = require('../validations/user.validation')
 
// create application/x-www-form-urlencoded parser
 
var upload = multer({ dest: './public/uploads/' })

router.get("/create", controller.create);
router.post("/create", upload.single('avatar'),controller.postCreate);

module.exports = router;