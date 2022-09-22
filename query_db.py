from tinydb import TinyDB
from tinydb.database import Document

#Read database speficied table
db = TinyDB('data.json')
db.default_table_name = 'Mobile'




