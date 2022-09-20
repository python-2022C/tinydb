from tinydb import TinyDB
from tinydb.database import Document
db = TinyDB('db_1.json')
#Create collection
table1 = db.table('table_1')

#Print all documents
print(table1.all())



