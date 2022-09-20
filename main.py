from tinydb import TinyDB
from tinydb.database import Document
db = TinyDB('db.json')

docs = db.all()

#Get length of documents
print(len(docs))

#Print first document
print(docs[0])

#Print first document's name
print(docs[0]['name'])