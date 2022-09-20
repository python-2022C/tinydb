from tinydb import TinyDB
from tinydb.database import Document
db = TinyDB('db.json')

#Remove document by id
db.remove(doc_ids=[5,6])
