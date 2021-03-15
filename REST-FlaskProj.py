
from flask import Flask, jsonify, request

''' MongoDB modules '''
from pymongo import MongoClient
import pandas as pd
import json

# initialize our Flask application
app= Flask(__name__, template_folder='template')

@app.route("/hello", methods=["GET"])
def hello():
    return "Hello World!"

@app.route("/class/name", methods=["GET"])
def name():
    return"This is CS446! This is Darnel Cristobal's server!"


@app.route("/name", methods=["POST"])
def setName():
    if request.method=='POST':
        posted_data = request.get_json()
        data = posted_data['data']
        return jsonify(str("Successfully stored  " + str(data)))

@app.route("/populate", methods=["POST"])#POST
def populate():
    col=connect(collection="oscars")
    dic={}
    posted_data = request.get_json()
    
    #items for DB
    #Puts it all in a dictionary
    index = posted_data['index']
    dic['index']=index
    
    year = posted_data['year']
    dic['year']=year
    
    age = posted_data['age']
    dic['age']=age
    
    name = posted_data['name']
    dic['name']=name
    
    movie = posted_data['movie']
    dic['movie']=movie
    
    #Inserts into the database
    col.insert_one(dic)
    
    #Lets the client know it was inserted
    return jsonify(str("inserted :)"))
   
@app.route("/movie/<string:theMovie>", methods=["GET"])
def movieIf(theMovie):
    col=connect()
    qList=[]
    
    myquery = {'movie' : {"$regex": theMovie}}
    queryLine = col.find(myquery,{"_id":0})
    
    for query in queryLine:
        qList.append(query)
       
    return json.dumps(qList,indent=1)

@app.route("/movie", methods=["GET"])
def movie():
    col=connect()
    posted_data = request.get_json()
    movie = posted_data['Movie']
    qList=[]
    
    myquery = {'movie' : {"$regex": movie}}
    queryLine = col.find(myquery,{"_id":0})
    
    for query in queryLine:
        qList.append(query)
       
    return json.dumps(qList, indent=1)


@app.route("/age", methods=["GET"])
def age():
    col=connect(collection="oscars")
    qList=[]
    
    posted_data = request.get_json()
    age = posted_data['Age']
    

    myquery = {'age' : age}
    queryLine = col.find(myquery,{"_id":0})
    
    for query in queryLine:
        qList.append(query)
       
    return json.dumps(qList, indent=1)


@app.route("/year", methods=["GET"])
def year():
    col=connect()
    qList=[]
    
    posted_data = request.get_json()
    year = posted_data['Year']
    
    myquery = {'year' : year}
    queryLine = col.find(myquery,{"_id":0})
    
    for query in queryLine:
        qList.append(query)
       
    return json.dumps(qList, indent=1)

@app.route("/index", methods=["GET"])
def index():
    col=connect()
    qList=[]
    
    posted_data = request.get_json()
    index = posted_data['Index']
    
    
    myquery = {'index' : index}
    queryLine = col.find(myquery,{"_id":0})
    
    for query in queryLine:
        qList.append(query)
       
    return json.dumps(qList, indent =1)

#MongoDB stuff
def connect(server="localhost", db="cristobal_skill5", port=27017, collection="oscars"):
    client = MongoClient(server, port)
    db = client[db]
    col = db[collection]
    return col

#  main thread of execution to start the server
if __name__=='__main__':
    '''
    print("Connecting to MongoDB server...")
    collection = connect(collection="123456")
    '''
    app.run(debug=True)