from tinydb import TinyDB
from tinydb.database import Document
db = TinyDB('db.json')


# Check if document exists
if db.contains(doc_id=5):
    # Get document
    doc = db.get(doc_id=1)
    # Print document
    print(doc)
else:
    print('Document does not exist')
    
