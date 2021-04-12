const mongoClient=require("mongodb").MongoClient
const url="mongodb://localhost:27017/"
const client=new mongoClient(url,{useUnifiedTopology:true})
client.connect()
const db=client.db("Fidingjob")
module.exports=db