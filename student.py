from flask import jsonify,Flask,request
from pymongo.mongo_client import MongoClient


uri = "mongodb+srv://12345:12345@cluster0.h3roqpp.mongodb.net/?retryWrites=true&w=majority"
app = Flask(__name__)

basic_auth = BasicAuth(app)

try:
    client = MongoClient(uri)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"



if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)