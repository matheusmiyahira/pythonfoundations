from pymongo import MongoClients

# FAZENDO CONECXAO COM O MONGODB
mongo_con = MongoClients()
# USAR BANCO
mongo_db = mongo_con['flask-app']

