module.exports.postCreate = function(req,res,next){
    var errors = [];
    if(!req.body.userName){
        errors.push("UserName is requied")
    }
    if(req.body.userName.length > 20){
        errors.push("The user name must not exceed 20 characters!")
    }
    if (!req.body.email){
        errors.push("Email is requied")
    }
    if (!req.body.pass){
        errors.push("Password is requied")
    }
    if (errors.length){
        res.render("user/create",{
            errors: errors,
            valued: req.body
        });
        return;
    }
    next();
}