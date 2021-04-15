const { ObjectID, ObjectId } = require("bson");
const db = require("../mongoDB")

module.exports.create = function (req, res) {
    res.render("user/create");
}

module.exports.postCreate = async function (req, res) {
  if(!req.file)
    req.body.avatar = "uploads\\26306066987a80ca8a795e384c726bc9";
  else   
    req.body.avatar = req.file.path.split('\\').slice(1).join('\\');
  db.collection("Users").insertOne(req.body)
  .catch(error => console.error(error))
  const user= await db.collection("Users").findOne({userName:req.body.userName})
  res.redirect("/information/"+user._id);
}
