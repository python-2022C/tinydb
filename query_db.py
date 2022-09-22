from tinydb import TinyDB,Query
from tinydb.database import Document

#Read database speficied table
db = TinyDB('data.json',indent=4,separators=(',',':'))
#Collection or table
db.default_table_name = 'Mobile'

#Create query object
query = Query()

#Add new document
db.insert({'name':'Samsung','price':10000,'model':'Galaxy S10'})
db.insert({'name':'Samsung','price':20000,'model':'Galaxy S20'})
db.insert({'name':'Samsung','price':30000,'model':'Galaxy S30'})



