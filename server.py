from flask import Flask, request
import sqlite3 as sql
app = Flask('_main_')

dict = {
   "HR69969" : {
         "Car Number": "HR696969",
         "Registration Date": "23-Jan-2020"
      }
   }

@app.route('/')
def home():
   return "hi"


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   return "hello"         

@app.route('/list')
def list():
    if( request.args['x'] in dict.keys()):
       return dict[request.args['x']]
    return "not found"

app.run(debug = True)
