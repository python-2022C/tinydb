
from tinydb import TinyDB,Query
from tinydb.database import Document

#Read database speficied table
db = TinyDB('data.json',indent=4,separators=(',',':'))
#Collection or table
db.default_table_name = 'Mobile'

#Create query object
query = Query()
#Update id=102 price
product = {
    'model':'Samsung Galaxy S10',
    'price': 1010,
    'color':'Silver',
    'company':'Samsung'
}
db.upsert(product,query.color=='Silver')