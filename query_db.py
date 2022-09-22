from tinydb import TinyDB,Query
from tinydb.database import Document

#Read database speficied table
db = TinyDB('data.json')
#Collection or table
db.default_table_name = 'Mobile'

#Create query object
query = Query()

#Print all documents by value
print(db.search(query.price>="236")) 