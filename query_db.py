from tinydb import TinyDB,Query
from tinydb.database import Document

#Read database speficied table
db = TinyDB('data.json',indent=4,separators=(',',':'))
#Collection or table
db.default_table_name = 'Mobile'

#Create query object
query = Query()
#Update id=102 price
db.update({'price':810},query.price==800)