from tinydb import TinyDB
from tinydb.database import Document

#Read database speficied table
db = TinyDB('data.json')
#Collection or table
db.default_table_name = 'Mobile'

#Read all documents
table=db.all()
for row in table:
    #Print only Samsung
    if row['company'] == 'Samsung':
        print(row)
    







