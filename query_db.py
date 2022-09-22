from tinydb import TinyDB,Query
from tinydb.database import Document

#Read database speficied table
db = TinyDB('data.json')
#Collection or table
db.default_table_name = 'Mobile'

#Create query object
query = Query()


print(db.search((query.price==500) | (query.price<=190))) #OR