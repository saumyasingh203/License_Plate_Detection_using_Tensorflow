from flask import Flask, request
import sqlite3 as sql
app = Flask('_main_')

dict = {
   "DL4CAU3215" : {
         "Car Number": "DL4CAU3215",
         "Model Name" : "AMAZE 1.2 S MT I-VTEC",
         "Registration Date": "23-Dec-2015",
         "Fitness/REGN" : "13-Jan-2031"
         "PUCC" : "10-Feb-2022",
         "Insurance" : "22-Dec-2022"
      } ,
  "DL12CG6648" : {
         "Car Number": "DL12CG6648",
         "Model Name" : "MAHINDRA SCORPIO S10 2.2 MHAWK",
         "Registration Date": "11-Sep-2015",
         "Fitness/REGN" : "20-Oct-2030"
         "PUCC" : "12-Mar-2022",
         "Insurance" : "20-Sep-2021"
      } ,
   "HR26BR9044" : {
         "Car Number": "HR26BR9044",
         "Model Name" : "INNOVA",
         "Registration Date": "07-May-2012",
         "Fitness/REGN" : "02-Apr-2027"
         "PUCC" : "NA",
         "Insurance" : "18-Mar-2022"
      } ,
    "HR26DK0830" : {
         "Car Number": "HR26DK0830",
         "Model Name" : "SWIFT ZDI AMT",
         "Registration Date": "03-Jan-2018",
         "Fitness/REGN" : "02-Jan-2033"
         "PUCC" : "NA",
         "Insurance" : "25-Dec-2022"
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
