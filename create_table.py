from gc import collect
from tinydb import TinyDB
from tinydb.database import Document
db = TinyDB('db_1.json')
#Create collection 
table1 = db.table('table_1')
table2 = db.table('table_2')
table1.insert({'name': 'John', 'age': 30})
table2.insert({'name': 'codeschool', 'age': 30})