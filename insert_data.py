import firebase_admin
from firebase_admin import db
from firebase_admin import firestore
#Library used to test limit values before insert data into firebase
#from itertools import islice 

def insert():
    db = firestore.client()

    #Get the JSON with the data
    with open("./data/data.json","r") as f:
        json_db = json.load(f)

    #Insert the data into firestore
    for value in json_db:
        #Convert InvoiceDate to Python datetime
        value['InvoiceDate'] = datetime.datetime.strptime(value['InvoiceDate'],"%m/%d/%Y %H:%M") 

        #print(value)
        db.collection('sales').add(value)
