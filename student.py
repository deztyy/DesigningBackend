from flask import jsonify,Flask,request
from pymongo.mongo_client import MongoClient
from flask_basicauth import BasicAuth 

uri = "mongodb+srv://12345:12345@cluster0.h3roqpp.mongodb.net/?retryWrites=true&w=majority"
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'name'
app.config['BASIC_AUTH_PASSWORD'] = 'pass'
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

@app.route("/students",methods =["GET"])
@basic_auth.required
def show_all_student():
    db = client["students"]
    collection = db["std_info"]
    all_students = list(collection.find())
    return jsonify(all_students)

@app.route("/students/<int:stu_id>",methods =["GET"])
@basic_auth.required
def show_student_id(stu_id):
    db = client["students"]
    collection = db["std_info"]
    all_students = list(collection.find())
    stu = next((s for s in all_students if s["_id"] == stu_id), None)
    if(stu):
        return jsonify(stu)
    else:
        return jsonify({"erro":"Student not found"}),404

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)