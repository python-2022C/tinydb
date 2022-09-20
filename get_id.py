from tinydb import TinyDB
from tinydb.database import Document
db = TinyDB('db.json')

# Check if document exists
if db.contains(doc_id=1):
    print("Document exists")
    