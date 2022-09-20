from tinydb import TinyDB
from tinydb.database import Document
#Read database speficied table
db = TinyDB('db_1.json')
#Print default table
db.default_table_name = 'table_2'
#Create collection
# table1 = db.table('table_1')
# table2 = db.table('table_2')

#Print all documents
# print(table1.all())
print(db.all())


