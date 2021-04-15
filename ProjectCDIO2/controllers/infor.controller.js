const db = require("../mongoDB")

module.exports.information = function (req, res) {
    res.render("index")
//     ,{
//       user:await db.collection("Users").findOne({_id:ObjectId(req.params.id)})
//     })
 }

module.exports.postInformation = async function (req, res) {
    // var id = await db.collection("Users").findOne(ObjectId(req.params.id))
    // db.collection("Users").updateOne({_id:ObjectId(req.params.id)},{
    //   upsert:true},
    //   {writeConcern:req.body},
    //   {collation:req.body
    // })
    // .catch(error => console.error(error))
    console.log(req.body)
    res.redirect("/"); 
  }
  