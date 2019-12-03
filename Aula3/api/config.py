from pymongo import MongoClient

# FAZENDO CONECXAO COM O MONGODB
mongo_con = MongoClient()
# USAR BANCO
db = mongo_con['flask-app']

