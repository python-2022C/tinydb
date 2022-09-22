from tinydb import TinyDB,Query
from tinydb.database import Document

#Read database speficied table
db = TinyDB('data.json')
#Collection or table
db.default_table_name = 'Mobile'

#Create query object
query = Query()


print(db.search((query.price==500) | (query.price<=190))) #OR

#Define query where price is less than 500
#Define query where price is greater than 190
#Define query where company is Samsung or Apple
#Define query where company is Samsung and price is less than 500
#Define query where company is Samsung and price is less than 500 and model is A10
#Define query where company is Samsung and price is less than 500 and model is A10 or A20
#Define query where companies are Samsung, Apple and Xiaomi
#Define query where companies are Samsung, Apple and Xiaomi and price is less than 500
#Define query where companies are Samsung, Apple and Xiaomi and price is less than 500 and model is A10
#Define query where companies are Samsung, Apple and Xiaomi and price is less than 500 and model is A10 or A20
#Define query where companies are Samsung, Apple and Xiaomi and color is black or white